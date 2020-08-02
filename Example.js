function testFunction(){


    console.log('hit this?');
    myUL = document.getElementById("document-list");

    li = document.createElement('li');
    li.className += 'list-group-item';
    li.id += 'WI-82-001';

    // Creating the Image portion
    var iconDiv = document.createElement('div');
    iconDiv.className += 'li-icon'

    var iconAnchor = document.createElement('a');
    iconAnchor.setAttribute("href", "Git.pdf");
    iconAnchor.setAttribute("targer", "_blank");

    var iconImg = document.createElement('img');
    iconImg.setAttribute("src", "pdf-icon.png");
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


    li.appendChild(iconDiv);
    li.appendChild(wiNameDiv);
    li.appendChild(wiLabelDiv);

    myUL.appendChild(li)
}