char nums[6];
int i = 0;
int val_base, val_end;

void setup(){
   Serial.begin(9600);
}

void loop(){
  
  if(Serial.available()){
    nums[i] = Serial.read() - '0';
    i++;
    if(i > 5) {
      i = 0;
      val_base = 100 * nums[0] + 10 * nums[1] + 1 * nums[2];
      val_end = 100 * nums[3] + 10 * nums[4] + 1 * nums[5];
      Serial.println(val_base);
      Serial.println(val_end);
    }
  }
}
