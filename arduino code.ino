#include<Servo.h>
Servo s1;
Servo s2;
Servo s3;
int deg[3];
void setup()
{
  Serial.begin(9600);
  s1.attach(3);
  s1.write(0);
  s2.attach(6);
  s2.write(0);
  s3.attach(9);
  s3.write(0);
}
void loop() {
  if (Serial.available() >= 3) {
    for (int i = 0; i < 3; i++) {
      deg[i] = Serial.read();
    }
  s1.write(deg[0]);
  s2.write(deg[1]);
  //s2.write(deg[2]);
}
}