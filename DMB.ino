#include <Servo.h>    // 声明调用Servo.h库
#define Trig 2 //引脚Tring 连接 IO D2
#define Echo 3 //引脚Echo 连接 IO D3   
float cm; //距离变量 
int pinBuzzer = 4; //管脚D3连接到蜂鸣器模块的信号脚
float temp;
int warning = 80;
Servo myservo;        // 创建一个舵机对象
int pos = 0;          // 变量pos用来存储舵机位置
void setup() { 
  myservo.attach(10);  // 将引脚10上的舵机与声明的舵机对象连接起来
  Serial.begin(9600);  
  pinMode(Trig, OUTPUT);  
  pinMode(Echo, INPUT);
  pinMode(pinBuzzer, OUTPUT); //设置pinBuzzer脚为输出状态

} 

void loop() { 
  long frequency = 300; //频率, 单位Hz
   for(pos = 0; pos < 180; pos+=45){    // 舵机从0°转到180°，每次增加45°          
      myservo.write(pos);           // 给舵机写入角度
  digitalWrite(Trig, LOW); //给Trig发送一个低电平  
  delayMicroseconds(2);    //等待 2微妙  
  digitalWrite(Trig,HIGH); //给Trig发送一个高电平  
  delayMicroseconds(10);    //等待 10微妙  
  digitalWrite(Trig, LOW); //给Trig发送一个低电平  
  temp = float(pulseIn(Echo, HIGH)); //存储回波等待时间,    
  cm = (temp * 17 )/1000; //把回波时间换算成cm  
  Serial.print("Distance = ");  
  Serial.print(cm);//串口输出距离换算成cm的结果  
  Serial.println("cm");
   if (cm < warning) {
  Serial.print("warning \n");
  tone(pinBuzzer, frequency );
   delay(500); //等待1000毫秒
   noTone(pinBuzzer);//停止发声
  }    
      delay(800);
   }
   for(pos = 180; pos>=1; pos-=45) {    // 舵机从180°转回到0°，每次减小45°                               
       myservo.write(pos);        // 写角度到舵机
  digitalWrite(Trig, LOW); //给Trig发送一个低电平  
  delayMicroseconds(2);    //等待 2微妙  
  digitalWrite(Trig,HIGH); //给Trig发送一个高电平  
  delayMicroseconds(10);    //等待 10微妙  
  digitalWrite(Trig, LOW); //给Trig发送一个低电平  
  temp = float(pulseIn(Echo, HIGH)); //存储回波等待时间,    
  cm = (temp * 17 )/1000; //把回波时间换算成cm  
  Serial.print("Distance = ");  
  Serial.print(cm);//串口输出距离换算成cm的结果  
  Serial.println("cm");
   if (cm < warning) {
    tone(pinBuzzer, frequency );
   delay(500); //等待1000毫秒
   noTone(pinBuzzer);//停止发声
  Serial.print("warning \n");
  }       
  delay(800);
    } 

    } 
