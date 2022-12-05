// This function is set up so that it takes one parameter, a number,
// and squares it, then returns the squared value.
function squareNumber(number) {
    var squaredNumber = number * number;
    return squaredNumber;
}

// This function is set up so that it takes one parameter, a number,
// and divides it by 2, then returns the halved value.
function halfNumber(number) {
    var half = number / 2;
    return half;
}

// The button with id "square-button" is what we will click when we
// want to calculate the squared number. Let's save it into a varible
// that we'll use to add an event listener.
var squareButton = document.getElementById("square-button");

// Adding the event listener, we want to look for a "click" action -
// this will run when the user clicks the button.
squareButton.addEventListener("click", function() {
  // The input with id "square-input" is the field the user entered their
  // number into. We can get the value of the field so we can use the number.
  var number = document.getElementById("square-input").value;

  // We can square our number by passing it as a parameter to our
  // squareNumber() function.
  var squaredNumber = squareNumber(number);

  // Now that we have squaredNumber, which is the value of the number the
  // user entered squared, we can set the innerHTML of our "solution" div
  // to equal the squaredNumber. This will display our result.
  document.getElementById("solution").innerHTML = squaredNumber;
});

// The button with id "half-button" is what we will click when we
// want to calculate the squared number. Let's save it into a varible
// that we'll use to add an event listener.
var halfButton = document.getElementById("half-button");

// Adding the event listener, we want to look for a "click" action -
// this will run when the user clicks the button.
halfButton.addEventListener("click", function() {
  // The input with id "half-input" is the field the user entered their
  // number into. We can get the value of the field so we can use the number.
  var number = document.getElementById("half-input").value;

  // We can half our number by passing it as a parameter to our
  // halfNumber() function.
  var halvedNumber = halfNumber(number);

  // Now that we have halvedNumber, which is the value of the number the
  // user entered halved, we can set the innerHTML of our "solution" div
  // to equal the halvedNumber. This will display our result.
  document.getElementById("solution").innerHTML = halvedNumber;
});
