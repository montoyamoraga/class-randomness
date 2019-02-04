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

}

// declaration of draw() function
// draw() is executed after setup(), on a loop, 60 fps
function draw() {

  // if mouse is pressed, draw ellipses
  // in other cases, draw rectangles
  if (mouseIsPressed) {

    for (let i = 0; i < numberShapes; i++) {
      // color for filling of 2d shapes
      // random amount of red, green, blue, alpha
      fill(random(255), random(255), random(255), random(255));

      // random size
      let size = random(maxSize);

      // draw ellipse surrounding mouse
      let posX = mouseX + random(-delta, delta);
      let posY = mouseY + random(-delta, delta);
      ellipse(posX, posY, size, size);
    }
  } else {
    for (let i = 0; i < numberShapes; i++) {
      // color for filling of 2d shapes
      // random amount of red, green, blue, alpha
      fill(random(255), random(255), random(255), random(255));

      // random size
      let size = random(maxSize);

      // draw rectangle surrounding mouse
      let posX = mouseX + random(-delta, delta);
      let posY = mouseY + random(-delta, delta);
      rect(posX, posY, size, size);
    }
  }
}

// function triggered when key is clicked
function keyPressed() {
  // check if key is up arrow
  if (keyCode == UP_ARROW) {
    // paint the background white
    background(255);
  }

}

// function triggered when window is resized
function windowResized() {
  // resize the canvas to make it full window again
  resizeCanvas(windowWidth, windowHeight);
}
