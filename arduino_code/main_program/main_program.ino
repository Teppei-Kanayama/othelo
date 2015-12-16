#include <Servo.h>
#include <math.h>

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
   digitalWrite(CATCH_PIN,  LOW);
   digitalWrite(RELEASE_PIN, LOW);
   servo[0].write(home_pos[0]);
   servo[1].write(home_pos[1]);   
}


void loop(){
  int data_num;
  int phase = 0;
  
  
  while((data_num = Serial.available()) >= 6){
    int val[2] = {0, 0};
    for(int i = 0; i < 6; i++){
      val[int(i/3)] += (Serial.read() - '0') * pow(10, 2 - i%3);  
    }
    if(phase == 0){
      digitalWrite(CATCH_PIN, HIGH);
      digitalWrite(RELEASE_PIN, LOW);
      Serial.print("catch\n");
      delay(1000);
      
      servo[0].write(val[0]);
      servo[1].write(val[1]);
      Serial.print("val[0] = ");
      Serial.print(val[0]);
      Serial.print(" and val[1] = ");
      Serial.print(val[1]);
      Serial.print('\n');
      delay(500);
      
      digitalWrite(CATCH_PIN, LOW);
      digitalWrite(RELEASE_PIN, HIGH);
      Serial.print("release\n");
      delay(3000);
      
      digitalWrite(CATCH_PIN, LOW);
      digitalWrite(RELEASE_PIN, LOW);
      Serial.print("power off\n");
      phase = 1;
    }else if(phase == 1){
        servo[0].write(val[0]);
        servo[1].write(val[1]);
        Serial.print("val[0] = ");
        Serial.print(val[0]);
        Serial.print(" and val[1] = ");
        Serial.print(val[1]);
        Serial.print('\n');
        delay(500);
        
        digitalWrite(CATCH_PIN, HIGH);
        digitalWrite(RELEASE_PIN, LOW);
        Serial.print("catch\n");
        delay(3000);
        
        servo[0].write(release_pos[0]);
        servo[1].write(release_pos[1]);
        Serial.print("go to release_pos\n");
        delay(500);
        
        digitalWrite(CATCH_PIN, LOW);
        digitalWrite(RELEASE_PIN, HIGH);
        Serial.print("release\n");
        delay(1000);
        
        digitalWrite(CATCH_PIN, LOW);
        digitalWrite(RELEASE_PIN, LOW);
        Serial.print("power off\n");
        
        servo[0].write(home_pos[0]);
        servo[1].write(home_pos[1]);
        Serial.print("go to home_pos\n");
        
        digitalWrite(CATCH_PIN, HIGH);
        digitalWrite(RELEASE_PIN, LOW);
        Serial.print("catch\n");
        delay(3000);
        
        servo[0].write(val[0]);
        servo[1].write(val[1]);
        Serial.print("val[0] = ");
        Serial.print(val[0]);
        Serial.print(" and val[1] = ");
        Serial.print(val[1]);
        Serial.print('\n');
        delay(500);
        
        digitalWrite(CATCH_PIN, LOW);
        digitalWrite(RELEASE_PIN, HIGH);
        Serial.print("release\n");
        delay(1000);
        
        digitalWrite(CATCH_PIN, LOW);
        digitalWrite(RELEASE_PIN, LOW);
        Serial.print("power off\n");
      }
      Serial.print("----------\n");
  }
  if(phase == 1){
  servo[0].write(home_pos[0]);
  servo[1].write(home_pos[1]);
  Serial.print("go to home_pos\n");
  }
}
