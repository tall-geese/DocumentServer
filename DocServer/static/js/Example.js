function testFunction(){
    // var myArray = [['hi','hey','yo'],['bye','cya','k']]
    // myArray.forEach((innArray,i) => {
    //    innArray.forEach((word) =>{
    //         console.log(word);
    //    }); 
    // });

    // while(node.firstChild) {
    //     node.removeChild(node.firstChild);
    // }

    // var myArray = [];
    // myArray.push(['WI-82-001','Creation of a Document','Git.pdf']);
    // myArray.push(['PR-80-001','Cleaning some tanks','data.doc']);
    // myArray.push(['WI-85-020','Im Testing Stuff','Git.pdf']);
    // myArray.push(['FO-82-015','This is a form','Git.pdf']);

    // console.log(myArray.toString());

    myUL = document.getElementById("document-list");

    li = document.createElement('li');
    li.className += 'list-group-item';
    li.id += 'WI-82-001';

    // Creating the Image portion
    var iconDiv = document.createElement('div');
    iconDiv.className += 'li-icon'

    var iconAnchor = document.createElement('a');
    iconAnchor.setAttribute("href", "static/data.doc");
    // iconAnchor.setAttribute("target", "_blank");

    var iconImg = document.createElement('img');
    iconImg.setAttribute("src", "static/images/pdf-icon.png");
    iconImg.setAttribute("width", "40px");
    iconImg.setAttribute("height", "40px");

    iconAnchor.appendChild(iconImg);
    iconDiv.appendChild(iconAnchor);

    // Creating the WI-name div
    var wiNameDiv = document.createElement('div');
    wiNameDiv.className += "WI-name"

    nameSmall = document.createElement('small');
    nameSmall.textContent += "WI-82-001";

    wiNameDiv.appendChild(nameSmall);

    // Create the label for the Doc ID
    var wiLabelDiv = document.createElement('div');
    wiLabelDiv.className += "WI-label"
    
    wiLabel = document.createElement('label');
    wiLabel.setAttribute("for", "WI-82-001");

    wiLabelHeader = document.createElement("h6");
    wiLabelHeader.textContent += "Creation of a Document"

    wiLabel.appendChild(wiLabelHeader);
    wiLabelDiv.appendChild(wiLabel);

    // Append our created subdivisions to the list element
    li.appendChild(iconDiv);
    li.appendChild(wiNameDiv);
    li.appendChild(wiLabelDiv);

    // append the list element to the unordered list
    myUL.appendChild(li)
}