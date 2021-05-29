int trig_pin = 11;
int echo_pin = 10;
long duration;
float distance;
const int buzzer = 9;

void setup()
{
  pinMode(trig_pin, OUTPUT);
  pinMode(echo_pin, INPUT);
  pinMode(buzzer, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
 digitalWrite(trig_pin, LOW);
  delayMicroseconds(2);
  
  digitalWrite(trig_pin, HIGH);
  delayMicroseconds(10); 
  digitalWrite(trig_pin, LOW);
  
  duration = pulseIn(echo_pin,HIGH);
  distance = 0.00017*duration;
  
  Serial.print("The object is at: ");
  Serial.print(distance);
  Serial.println(" meters");
  
  if(distance < 200)
  {
  	tone(buzzer, 1000); 
  	delay(1000);       
  	noTone(buzzer);  
  	delay(1000);  
  }
  delayMicroseconds(1);
}