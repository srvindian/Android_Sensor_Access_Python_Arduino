#include <Servo.h>
Servo myservo;  // create servo object to control a servo
              // a maximum of eight servo objects can be created
int pos = 0;    // variable to store the servo position
void setup() {
 myservo.attach(9);  // attaches the servo on pin 9 to the servo object  //orange pin for data
 Serial.begin(9600);
}
String data;
int angle;
void loop() {
 if (Serial.available())
 {
   data=Serial.readString();
   angle=data.toInt();
   //angle=Serial.parseInt();
   //Serial.println(angle);
   myservo.write(angle);
 }
}