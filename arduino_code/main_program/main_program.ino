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


void pick_up(){
  digitalWrite(CATCH_PIN, HIGH);
  digitalWrite(RELEASE_PIN, LOW);
  Serial.print("pick up\n");
  return;
}


void relinquish(){
  digitalWrite(CATCH_PIN, LOW);
  digitalWrite(RELEASE_PIN, HIGH);
  Serial.print("relinquish\n");
  return;
}

void power_off(){
  digitalWrite(CATCH_PIN, LOW);
  digitalWrite(RELEASE_PIN, LOW);
  Serial.print("power off\n");
  return;
}

void drive_servo(int *val){
  servo[0].write(val[0]);
  servo[1].write(val[1]);
  Serial.print("val[0] = ");
  Serial.print(val[0]);
  Serial.print(" and val[1] = ");
  Serial.print(val[1]);
  Serial.print('\n');
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

      pick_up();
      delay(1000);
      
      drive_servo(val);
      delay(500);
      
      relinquish();
      delay(3000);
      
      power_off();
      phase = 1;

    }else if(phase == 1){
        
        drive_servo(val);
        delay(500);
        
        pick_up();
        delay(3000);
        
        drive_servo(release_pos);
        delay(500);
        
        relinquish();
        delay(1000);
        
        power_off();
        
        drive_servo(home_pos);
        
        pick_up();
        delay(3000);
        
        drive_servo(val);
        delay(500);
        
        relinquish();
        delay(1000);
        
        power_off();
      }
  }
  if(phase == 1){
  drive_servo(home_pos);
  Serial.print("----------\n");
  }
}
