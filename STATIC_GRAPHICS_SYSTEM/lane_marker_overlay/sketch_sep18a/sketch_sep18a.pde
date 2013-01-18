import processing.opengl.*;

PImage b;


int y_val = 384;
int oldY;
int diff;
void setup() {

  size(1024, 768, OPENGL);
  b = loadImage("helloworld.jpg");
  smooth();
  
}

void draw() {
    background(0,255, 33); 
    image(b, 0, 0);
    camera(125, 500, 300, 125, y_val, 0.0, 0.0, 1.0, 0.0);
    // camera(eyeX, eyeY, eyeZ, centerX, centerY, centerZ, upX, upY, upZ)
    ellipse(512, y_val, 5,5);
  tint(255, 240); 
 
 // exit();
 println(y_val);

}


void mousePressed() {
  oldY = mouseY;
}

void mouseDragged() {
    if(diff-mouseY!=0) {
         y_val+=diff/20;

    }
    diff = mouseY-oldY;

}

void mouseReleased() {
 oldY = 0; 

}
 
























