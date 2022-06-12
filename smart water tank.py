#define BLYNK_PRINT Serial
           #include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>
#define trigger_pin 12
#define Echo_pin 14
#define LED 2

long duration;
int distance;

char auth[] = "TJ6ez88H7E4UFTpC74fAd8DoRMFxq0FU";
char ssid[] = "DIR-615-208B";
char pass[] = "vvsnsastry@1967";


void setup() {


 Blynk.begin(auth, ssid, pass);
pinMode(trigger_pin, OUTPUT); 
pinMode(LED, OUTPUT); 
pinMode(Echo_pin, INPUT); 
Serial.begin(9600); 
}

void loop() {

   Blynk.run();
  
digitalWrite(trigger_pin, LOW); 
delayMicroseconds(2);


digitalWrite(trigger_pin, HIGH);  
delayMicroseconds(10);            
digitalWrite(trigger_pin, LOW);   


duration = pulseIn(Echo_pin, HIGH); 
distance= duration*0.034/2; 

if ( distance < 10)
digitalWrite(LED, HIGH);
else 
digitalWr…
[0:07 am, 30/05/2022] Surya Prakash: #define BLYNK_PRINT Serial


#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>
#define trigger_pin 12
#define Echo_pin 14
#define LED 2

long duration;
int distance;

char auth[] = "TJ6ez88H7E4UFTpC74fAd8DoRMFxq0FU";
char ssid[] = "DIR-615-208B";
char pass[] = "vvsnsastry@1967";


void setup() {


 Blynk.begin(auth, ssid, pass);
pinMode(trigger_pin, OUTPUT); 
pinMode(LED, OUTPUT); 
pinMode(Echo_pin, INPUT); 
Serial.begin(9600); 
}

void loop() {


  
digitalWrite(trigger_pin, LOW); 
delayMicroseconds(2);


digitalWrite(trigger_pin, HIGH);  
delayMicroseconds(10);            
digitalWrite(trigger_pin, LOW);   


duration = pulseIn(Echo_pin, HIGH); 
distance= duration*0.034/2; 

if ( distance < 10)
digitalWrite(LED, HIGH);
else 
digitalWrite(LED, LOW);

Serial.print("TANK LEVEL: ");
Serial.print(distance);
Serial.println(" cm");
Blynk.virtualWrite(V0,distance);
   Blynk.run();
delay(1000);
}
