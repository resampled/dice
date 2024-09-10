function replyToggler(target, btn, usual, alt) {
    showHide(target);
    replaceInnerHTML(btn, usual, alt);
}

function showHide(target) {
    var x = document.getElementById(target);
    if (x.style.display === "none") {
        x.style.display = "";
    } else {
        x.style.display = "none";
    }
}
function replaceInnerHTML(target, usual, alt) {
    var x = document.getElementById(target);
    if (x.innerHTML === usual) {
        x.innerHTML = alt;    
    } else {
        x.innerHTML = usual;
    }
}
