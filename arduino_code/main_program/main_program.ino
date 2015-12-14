#include <Servo.h>
#include <math.h>

int val[16];
Servo servo[2];
int CATCH_PIN = 6, RELEASE_PIN = 7;

int home_pos[2] = {
  0, 0
};

int release_pos[2] = {
  170, 90
};

void setup(){
   Serial.begin(9600);
   servo[0].attach(8);
   servo[1].attach(9);
   pinMode(CATCH_PIN, OUTPUT);
   pinMode(RELEASE_PIN, OUTPUT);
}

void loop(){
  int data_num;
  digitalWrite(CATCH_PIN,  LOW);
  digitalWrite(RELEASE_PIN, LOW);
  servo[0].write(home_pos[0]);
  servo[1].write(home_pos[1]);
  
  if(data_num = Serial.available()){
    for(int i = 0; i < data_num; i++){
      val[i%3] += (Serial.read() - '0') * pow(10, 2 - i%3);  
    }
      digitalWrite(CATCH_PIN, HIGH);
      digitalWrite(RELEASE_PIN, LOW);
      delay(1000);
      
      servo[0].write(val[0]);
      servo[1].write(val[1]);
      delay(500);
      
      digitalWrite(CATCH_PIN, LOW);
      digitalWrite(RELEASE_PIN, HIGH);
      delay(3000);
      
      digitalWrite(CATCH_PIN, LOW);
      digitalWrite(RELEASE_PIN, LOW);
      
      for(int i = 2; i < data_num % 6; i += 2){
        servo[0].write(val[i]);
        servo[1].write(val[i+1]);
        delay(500);
        digitalWrite(CATCH_PIN, HIGH);
        digitalWrite(RELEASE_PIN, LOW);
        delay(3000);
        servo[0].write(release_pos[0]);
        servo[1].write(release_pos[1]);
        delay(500);
        digitalWrite(CATCH_PIN, HIGH);
        digitalWrite(RELEASE_PIN, LOW);
        delay(1000);
        digitalWrite(CATCH_PIN, LOW);
        digitalWrite(RELEASE_PIN, LOW);
      }
  }
}
