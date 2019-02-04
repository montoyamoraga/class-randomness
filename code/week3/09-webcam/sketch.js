// global variables for configuration
// variable number of ellipses drawn per frame
let numberShapes = 10;
// variable for maximum diameter of ellipses
let maxSize = 50;
// variable for controlling framerate
let speed = 30;
// variable for variation of position
let delta = 100;

// declaration of setup() function
// setup() is executed once, at the beginning
function setup() {
  // create a canvas for p5.js to draw in
  // createCanvas(width, height), measured in pixels
  // width and height are p5.js variable
  createCanvas(windowWidth, windowHeight);

  capture = createCapture(VIDEO);
  capture.hide();

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

  console.log("setup finished");





}

// declaration of draw() function
// draw() is executed after setup(), on a loop, 60 fps
function draw() {
  // place images on the canvas
  image(capture, 0, 0, width, height);

}

// function triggered when key is clicked
function keyPressed() {
  // check if key is up arrow
  if (keyCode == UP_ARROW) {
    // save canvas
    saveCanvas('myCanvas', 'jpg');
  }

}

// function triggered when window is resized
function windowResized() {
  // resize the canvas to make it full window again
  resizeCanvas(windowWidth, windowHeight);
}
