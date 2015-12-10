#include <Servo.h>
// 変数の定義
#define LED_PIN 13
 
 Servo servo_base;
 Servo servo_end;
// 初期化
void setup(){
  servo_base.attach(9);
  servo_end.attach(8);
  // シリアルポートを9600 bps[ビット/秒]で初期化 
  Serial.begin(9600);
}
 
 int phase = 0;
// 繰り返し処理
void loop(){
  char input;
  int val;
  //int phase = 0;
  //Serial.print("a");
  // シリアルポートより1文字読み込む
  input = Serial.read();
  if(input != -1 ){
    // 読み込んだデータが -1 以外の場合　以下の処理を行う
    Serial.print(phase);
    val = (input - '0') * 10;
    if(val == 50){
      val = 180;
    }else if(val == 60){
      val = 0;
    }
    Serial.print(val);
    Serial.print('\n');
    if(phase == 0){
    servo_base.write(val);
    }else{
    servo_end.write(val);
    }
    delay(500);
    phase = 1 - phase;
  }
}
