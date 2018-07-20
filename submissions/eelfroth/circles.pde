final float S = 1;    //step
final float W = 10;   //weight
final float A = 255;  //alpha
final float R = PI/3; //rotation
final float M = 0;    //modulo
final float Z = 0.9;  //zoom

float i;

void setup() {
    size(1000, 1000);
    background(0);
    noFill();
    ellipseMode(CENTER);
    i = 1 / S;
}

void draw() {
    float t = i * S;
    float w = max(W / t, 1);
    float r = (Z*height + w) / t;
    float a = A / (1 + t/10);

    stroke(255, a);
    strokeWeight(w);
    translate(width/2, height/2);
    rotate(R * (t-1) / S);

    if (r < 1 || a < 1) noLoop();
    if (floor(t) % M == 0) t -= 1;

    for (int k = 0; k < floor(t); k++) {
        float x = (k*r) - (r/2)*(t-1) + (r/2)*(t%1);
        ellipse(x, 0, r, r);
    }

    i++;
}
