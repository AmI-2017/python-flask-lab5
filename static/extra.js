/**
 * Created by 7217238 on 27/04/2017.
 */
function myfocus() {
    document.getElementById("submitbutton").removeAttribute("disabled") ;
}

function copydown(element) {
    var text = element.parentNode.textContent.trim() ;
    document.getElementById("inputdescription").value=text ;

}
