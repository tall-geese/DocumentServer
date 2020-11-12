
// In the order of fields that we care about:  
//     DOC_NUM, DOC_NAME, File_Path, Revison
var unipointProductionIndex = [1,2,6,4];
var iqsTestIndex = [0,1,15,6];

// Switch here for testing vs production code
var columnIndex = iqsTestIndex;


function getInput(getEditDistance, documentList){
    var inputField = document.getElementById('document-input');
    searchValue = inputField.value;
    
    var rowCount = 0;

    var ul = document.getElementById('document-list');
    while (ul.firstChild){
        ul.removeChild(ul.firstChild);
    }

    if (searchValue.length >= 2){
        var compareField;

        if (searchValue.length == 2) {
            console.log('hit the 2 char only');
            switch(searchValue.toUpperCase()){
                case 'PR':
                case 'FO':
                case 'WI':
                case 'VD':
                case 'SA':
                case 'RE':
                case 'TG':
                case 'QM':
                case 'JD':
                    compareField = columnIndex[0];
                    break;
                default:
                    compareField = columnIndex[1];
            }            
        } else if (searchValue.indexOf('-') !== -1) {
            compareField = columnIndex[0];
            console.log('hit the - doc_num one');
        } else {
            compareField = columnIndex[1];
            console.log('hit the doc_name one')
        }


        if (compareField == columnIndex[1]){
        orderList = [];

            documentList.forEach((element, index) => {
                var leastDistance = 100;
                
                element[compareField].split(" ").forEach(word =>{
                    var distance = getEditDistance(searchValue, word.substring(0,searchValue.length));
                    if (distance < leastDistance){
                        leastDistance = distance;
                    } 
                });
                orderList.push([index, leastDistance]);
            });

            //TODO: in addition to this sorting by the leven distance, maybe we can create a sub-list out of
            // the first 5 items (or however many it has) and sort alphabetically or by the document number alphatbetically
            // but only rearrange in groups of equal levenshtein distance
            orderList.sort( (a,b) =>{
                return a[1] - b[1];
            });

            orderList.forEach(element =>{
                if (element[1] <= 1 && rowCount < 5){
                    console.log(documentList[element[0]][1] + ' index:' + element[0] + ' edit dist:' + element[1])
                    createListItem(documentList[element[0]]);
                    rowCount++;
                } 
            });

        } else if (compareField == columnIndex[0]) {
            documentList.sort( (a,b) =>{
                return getEditDistance(searchValue, a[compareField].substr(0,searchValue.length)) - 
                getEditDistance(searchValue, b[compareField].substr(0,searchValue.length));
            });

            //TODO: like above, even after we factor out doc numbers that we don't want by their edit distance,
            // we should still sort these alphabetically

            // ok there should be no need to sort the documents further, since its captured by the "ORDER BY clause"

            documentList.forEach(element => {
            if (getEditDistance(searchValue, element[compareField].substr(0,searchValue.length)) <=1 && rowCount < 5){
                createListItem(element);
                rowCount++;
                console.log(element[compareField] + 'index: ' + getEditDistance(searchValue, element[compareField].substr(0,searchValue.length)));
            }           
            });
        }

    //     // TODO: put an if/else here, we can keep the normal process if we are using the Doc_ID,
    //     // but if we are using the Doc_Name then we need a way to split and compare each word of the Doc_Name
    //     // to the search field.
    //     documentList.sort( (a,b) =>{
    //         // sort our list of documents by comparing the first x characters of the desired 
    //         // field (doc_name or doc_num) to the search string where x is the 
    //         // length of the search string
    //         return getEditDistance(searchValue, a[compareField].substr(0,searchValue.length)) - 
    //         getEditDistance(searchValue, b[compareField].substr(0,searchValue.length));
    //     });

    //     documentList.forEach(element => {
    //        if (getEditDistance(searchValue, element[compareField].substr(0,searchValue.length)) <=1 && rowCount < 5){
    //            createListItem(element);
    //             rowCount++;
    //        }
           
    //     });
    }
}

function createListItem(documentRow){
    
    myUL = document.getElementById("document-list");

    li = document.createElement('li');
    li.className += 'list-group-item';
    li.id += 'WI-82-001';

    // Creating the Image portion
    var iconDiv = document.createElement('div');
    iconDiv.className += 'li-icon';

    var iconAnchor = document.createElement('a');
    escapedString = documentRow[columnIndex[2]].replace(/\\/g,'/'); 

    // In the SQL query we're asking to pull the file location for the pdf
    // attachment if the document has one. Here we are splitting the string 
    // differently becuase the directories for documents and attachments are not common
    if (documentRow[columnIndex[2]].indexOf('Attachments') == -1) {
        iconAnchor.setAttribute("href", '/documents/Doc_Control/' + escapedString.split('Doc_Control/')[1]);
        // console.log('/documents/Doc_Control/' + escapedString.split('Doc_Control/')[1]);
        
    } else {
        iconAnchor.setAttribute("href", '/documents/Attachments/' + escapedString.split('Attachments/')[1]);
        // console.log('/documents/Attachments/' + escapedString.split('Attachments/')[1]);
    }

    iconAnchor.setAttribute("target", "_blank");
    // iconAnchor.setAttribute("href", "static/git.pdf");
    // iconAnchor.setAttribute("target", "_blank");

    var iconImg = document.createElement('img');

    // test databse documentRow[6]
    // IQS database documentRow[15]    
    switch(documentRow[columnIndex[2]].split('.')[1]){
        case 'pdf':
            iconImg.setAttribute("src", "static/images/pdf-icon.png");
            break;
        case 'docx':
            iconImg.setAttribute("src", "static/images/word-doc-icon.png");
            break;
        case 'doc':
            iconImg.setAttribute("src", "static/images/word-doc-icon.png");
            break;
        case 'dotm':
            iconImg.setAttribute("src", "static/images/word-doc-icon.png");
            break;
        case 'xlsm':
            iconImg.setAttribute("src", "static/images/excel-xls-icon.png");
            break;
        case 'xlsx':
            iconImg.setAttribute("src", "static/images/excel-xls-icon.png");
            break;
        case 'xls':
            iconImg.setAttribute("src", "static/images/excel-xls-icon.png");
            break;
        case 'pptx':
            iconImg.setAttribute("src", "static/images/ppt-icon.png");
            break;
        default:
            iconImg.setAttribute("src", "static/images/pdf-icon.png");
    }
    iconImg.setAttribute("width", "40px");
    iconImg.setAttribute("height", "40px");

    iconAnchor.appendChild(iconImg);
    iconDiv.appendChild(iconAnchor);

    // Creating the WI-name div
    var wiNameDiv = document.createElement('div');
    wiNameDiv.className += "WI-name";

    nameSmall = document.createElement('small');
    // test database documentRow[1]
    // IQS database documentRow[0]
    nameSmall.textContent += documentRow[columnIndex[0]];

    wiNameDiv.appendChild(nameSmall);

    // Create the label for the Doc ID
    var wiLabelDiv = document.createElement('div');
    wiLabelDiv.className += "WI-label";
    
    wiLabel = document.createElement('label');
    wiLabel.setAttribute("for", "WI-82-001");

    wiLabelHeader = document.createElement("h6");
    // test database documentRow[2]
    // IQS database documentRow[1]
    wiLabelHeader.textContent += documentRow[columnIndex[1]];

    wiLabel.appendChild(wiLabelHeader);
    wiLabelDiv.appendChild(wiLabel);


    wiRevDiv = document.createElement('div');
    wiRevDiv.className += 'WI-rev';
    
    revSmall = document.createElement('small');
    // test database documentRow[4]
    // IQS database documentRow[6]
    revSmall.textContent += 'Rev' + documentRow[columnIndex[3]];
    wiRevDiv.appendChild(revSmall);
    

    // Append our created subdivisions to the list element
    li.appendChild(iconDiv);
    li.appendChild(wiNameDiv);
    li.appendChild(wiLabelDiv);
    li.appendChild(wiRevDiv);

    // append the list element to the unordered list
    myUL.appendChild(li)
}

function openWindow() {
    // window.open("C:\\uniPoint_Vault\\JPMC_TEST_UP\\Doc_Control\\SAMPLE 3\\SAMPLE 3_A.pptx", "_self");

}