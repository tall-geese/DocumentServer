function testFunction(){
    console.log('hit this?');
    var myUL;
    myUL = document.getElementById("document-list");
    li = document.createElement('li');
    li.className += 'list-group-item'
    myUL.appendChild(li)
}