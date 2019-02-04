// declaration of setup() function
// setup() is executed once, at the beginning
function setup() {
  // create a canvas for p5.js to draw in
  // createCanvas(width, height), measured in pixels
  createCanvas(400, 400);

  // change framerate, measured in frames per second
  frameRate(10);
}

// declaration of draw() function
// draw() is executed after setup(), on a loop, 60 fps
function draw() {
  // paint the background with a color
  // color by default is 8 bit resolution and is
  // 1 value: grayscale, 0 is black, 255 black
  // 2 values: grayscale + alpha, 0 transparent, 255 solid
  // 3 values: RGB, 0 is minimum, 255 is maximum
  // 4 values: RGBA, RGB + alpha
  background(220, 255);

  // no border
  noStroke();
  // color for filling of 2d shapes
  // random amount of red
  fill(random(255), 0, 0);

  // ellipse that follows mouse, 50x50 px
  ellipse(mouseX, mouseY, 50, 50);
}
