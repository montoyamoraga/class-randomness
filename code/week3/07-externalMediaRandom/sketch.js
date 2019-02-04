// global variables for configuration
// variable number of ellipses drawn per frame
let numberShapes = 10;
// variable for maximum diameter of ellipses
let maxSize = 50;
// variable for controlling framerate
let speed = 10;
// variable for variation of position
let delta = 100;

// variables for storing images
let broccoli = null;
let lettuce = null;
let tomato = null;

// declaration of preload() function
// preload() is executed once, before setup()
// it waits for its execution to end before continuing to setup()
// preload() is useful for loading external media
function preload() {
  broccoli = loadImage("assets/broccoli.jpg");
  lettuce = loadImage("assets/lettuce.jpg");
  tomato = loadImage("assets/tomato.jpg");
}

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

  // place images on the canvas
  // image(buffer, posX, posY, sizeX, sizeY);


}

// declaration of draw() function
// draw() is executed after setup(), on a loop, 60 fps
function draw() {

  // random number between 0 and 1
  let result = Math.random();

  // place images in random places with random sizes
  if (result < 1/3) {
    image(broccoli, random(width), random(height), random(maxSize), random(maxSize));
  } else if (result < 2/3) {
    image(lettuce, random(width), random(height), random(maxSize), random(maxSize));
  } else {
    image(tomato, random(width), random(height), random(maxSize), random(maxSize));
  }




}
