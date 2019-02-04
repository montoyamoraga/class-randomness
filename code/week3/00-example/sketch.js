// declaration of setup() function
// setup() is executed once, at the beginning
function setup() {
  createCanvas(400, 400);
}

// declaration of draw() function
// draw() is executed after setup(), on a loop, 60 fps
function draw() {
  background(220);
  ellipse(mouseX, mouseY, 50, 50);
}
