
// global variables for configuration
// variable number of ellipses drawn per frame
let numberEllipses = 100;
// variable for maximum diameter of ellipses
let maxDiameter = 50;
// variable for controlling framerate
let speed = 10;

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
}

// declaration of draw() function
// draw() is executed after setup(), on a loop, 60 fps
function draw() {

  // for loop to draw many ellipses per frame
  for (let i = 0; i < numberEllipses; i++) {

    // color for filling of 2d shapes
    // random amount of red, green, blue, alpha
    fill(random(255), random(255), random(255), random(255));

    // random diameter
    let diam = random(maxDiameter);

    //draw ellipse, random position, random diameter
    ellipse(random(width), random(width), diam, diam);
  }



}

// function triggered when mouse is clicked
function mouseClicked() {
  // paint the background white
  background(255);
}

// function triggered when window is resized
function windowResized() {
  // resize the canvas to make it full window again
  resizeCanvas(windowWidth, windowHeight);
}
