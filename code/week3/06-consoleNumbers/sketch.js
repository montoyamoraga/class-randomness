// global variables for configuration
// variable number of ellipses drawn per frame
let numberShapes = 10;
// variable for maximum diameter of ellipses
let maxSize = 50;
// variable for controlling framerate
let speed = 10;
// variable for variation of position
let delta = 100;

// declaration of setup() function
// setup() is executed once, at the beginning
function setup() {
  // create a canvas for p5.js to draw in
  // createCanvas(width, height), measured in pixels
  // width and height are p5.js variable
  createCanvas(windowWidth, windowHeight);

  // change framerate, measured in frames per second
  frameRate(speed);

  // no border
  noStroke();

  // paint the background with a color
  // color by default is 8 bit resolution and is
  // 1 value: grayscale, 0 is black, 255 black
  // 2 values: grayscale + alpha, 0 transparent, 255 solid
  // 3 values: RGB, 0 is minimum, 255 is maximum
  // 4 values: RGBA, RGB + alpha
  background(255);

  // mode for drawing
  ellipseMode(CENTER);
  rectMode(CENTER);

  console.log("setup finished");

}

// declaration of draw() function
// draw() is executed after setup(), on a loop, 60 fps
function draw() {

  // random number between 0 and 1
  console.log("Math.random(): " + Math.random());

  // random number between min and maximum
  let min = 5;
  let max = 10;
  let inBetween = min + (max-min)*Math.random();
  console.log("between " + min + " - " + max + ": " + inBetween);

  // convert to integer
  let inBetweenInt = inBetween.toFixed(0);
  console.log("integer: " + inBetweenInt);

  // random coin flip
  let coin = Math.random();
  let coinResult = "";
  if (coin < 0.5) {
    coinResult = "heads";
  } else {
    coinResult = "tails";
  }
  console.log("coin flip: " + coinResult);
}
