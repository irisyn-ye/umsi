// Challenge 4
// Update the checkForm() function so that it checks whether or not you
// have filled out the name and address fields. If not, display the appropriate
// error message.

// Extra challenge: Update the function so that if you fill out the field and
// hit the button again, the error message is hidden again.

function checkForm() {
    var fullName = document.getElementById("fullname");
    var streetAddr = document.getElementById("streetaddr");

    if (fullName.value === "") {
        document.getElementById("nameerrormsg").style.display = "block";
    }
    else {
        document.getElementById("nameerrormsg").style.display = "none";
    }

    if (fullName.value === "") {
        document.getElementById("addrerrormsg").style.display = "block";
    }
    else {
        document.getElementById("addrerrormsg").style.display = "none";
    }

    return false;
}


// Challenge 5
// Update the checkNum() function so that it checks whether or not you
// have filled out the field using a number. If not, display the error message.
// Then update the function to hide the error message if a number was entered.
// HINT: look up the isNaN() function!

function checkNum() {
    var personalNum = document.getElementById("age");

    if (isNaN(personalNum.value)) {
        document.getElementById("ageerrormsg").style.display = "block";
    }
    else {
        document.getElementById("ageerrormsg").style.display = "none";
    }

    return false;

}


// Challenge 6
// We know how to use pseudo classes to change styling when we hover over something.
// Try using JavaScript to do the same thing. When you hover over an image, display
// the alt text.

function displayText(image) {
    // var imgHover = document.getElementsByClassName("img");

    var text = image.alt;
    document.getElementById("displaytext").innerHTML = text;
}
