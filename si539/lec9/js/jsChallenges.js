// Challenge 1
// Update the toggleEmail() function so that when the checkbox is checked
// the email field is displayed.

function toggleEmail() {
  document.getElementById("email").style.display = "block";
}


// Challenge 2
// Update the toggleAddress() function so that when the checkbox is checked
// the home address field is hidden.

function toggleAddress() {
  document.getElementById("home").style.display = "none";
}


// Challenge 3
// Update the checkForm() function so that it checks whether or not you
// have selected a radio button.

function checkForm() {
  // First, create a variable for each button so we don't have to keep typing
  // document.getElementById
  var optStrawberry = document.getElementById("optstraw");
  var optBlueberry = document.getElementById("optblue");

  // Check the value of both variables to see if they're checked
  if (!optStrawberry.checked && !optBlueberry.checked) {
    window.alert("Please select your favourite berry!");
    return false;
  }
  return true;
}
