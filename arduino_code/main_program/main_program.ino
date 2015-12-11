#include <Servo.h>

char nums[6];
int i = 0;
int val[2][2];
Servo servo[2];
int CATCH_PIN = 6, RELEASE_PIN = 7;

int home_pos[2] = {
  0, 0
};

void setup(){
   Serial.begin(9600);
   servo[0].attach(8);
   servo[1].attach(9);
   pinMode(CATCH_PIN, OUTPUT);
   pinMode(RELEASE_PIN, OUTPUT);
}

void loop(){
  
  digitalWrite(CATCH_PIN, LOW);
  digitalWrite(RELEASE_PIN, LOW);
  servo[0].write(home_pos[0]);
  servo[1].write(home_pos[1]);
  
  if(Serial.available()){
    
    nums[i] = Serial.read() - '0';
    i++;
    if(i > 5) {
      i = 0;
      val[0][0] = 100 * nums[0] + 10 * nums[1] + 1 * nums[2];
      val[0][1] = 100 * nums[3] + 10 * nums[4] + 1 * nums[5];
      Serial.println(val[0][0]);
      Serial.println(val[0][1]);
      
      digitalWrite(CATCH_PIN, HIGH);
      digitalWrite(RELEASE_PIN, LOW);
      delay(1000);
      
      servo[0].write(val[0][0]);
      servo[1].write(val[0][1]);
      delay(500);
      
      digitalWrite(CATCH_PIN, LOW);
      digitalWrite(RELEASE_PIN, HIGH);
      delay(500);
      
      digitalWrite(CATCH_PIN, LOW);
      digitalWrite(RELEASE_PIN, LOW);
      servo[0].write(home_pos[0]);
      servo[1].write(home_pos[1]);
      delay(500);
    }
  }
}
