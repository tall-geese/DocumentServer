
function getInput(getEditDistance, documentList){
    var inputField = document.getElementById('document-input');
    searchValue = inputField.value;
    
    var rowCount = 0;

    var ul = document.getElementById('document-list');
    while (ul.firstChild){
        ul.removeChild(ul.firstChild);
    }

    if (searchValue.length >= 2){
        // test database DOC_NUM = 1
        // IQS database DOC_NUM = 0
        const DOC_NUM = 1;
        // test database DOC_NAME = 2
        // IQS database DOC_NAME = 1
        const DOC_NAME = 2;
        var compareField;

        switch(searchValue.substr(0,2).toUpperCase()){
            case 'PR':
            case 'FO':
            case 'WI':
            case 'VD':
            case 'SA':
            case 'RE':
            case 'TG':
            case 'QM':
            case 'JD':
                compareField = DOC_NUM;
                break;
            default:
                compareField = DOC_NAME;
        }


        documentList.sort( (a,b) =>{

            return getEditDistance(searchValue, a[compareField].substr(0,searchValue.length)) - 
            getEditDistance(searchValue, b[compareField].substr(0,searchValue.length));
        });

        documentList.forEach(element => {
           if (getEditDistance(searchValue, element[compareField].substr(0,searchValue.length)) <=1 && rowCount < 5){
               createListItem(element);
                rowCount++;
           }
           
        });
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
    iconAnchor.setAttribute("href", "static/git.pdf");
    iconAnchor.setAttribute("target", "_blank");

    var iconImg = document.createElement('img');
    // test databse documentRow[6]
    // IQS database documentRow[15]
    console.log(documentRow[6]);
    switch(documentRow[6].split('.')[1]){
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
    nameSmall.textContent += documentRow[1];

    wiNameDiv.appendChild(nameSmall);

    // Create the label for the Doc ID
    var wiLabelDiv = document.createElement('div');
    wiLabelDiv.className += "WI-label";
    
    wiLabel = document.createElement('label');
    wiLabel.setAttribute("for", "WI-82-001");

    wiLabelHeader = document.createElement("h6");
    // test database documentRow[2]
    // IQS database documentRow[1]
    wiLabelHeader.textContent += documentRow[2];

    wiLabel.appendChild(wiLabelHeader);
    wiLabelDiv.appendChild(wiLabel);

    // Append our created subdivisions to the list element
    li.appendChild(iconDiv);
    li.appendChild(wiNameDiv);
    li.appendChild(wiLabelDiv);

    // append the list element to the unordered list
    myUL.appendChild(li)
}