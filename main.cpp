#include <IRremote.hpp>
/*
# list of aviable codes
#To be send by IrSender.()

#Sony: (sendSony)
#2    VOL up: (0x10, 0x12, 2, 12)
#3    VOL down: (0x10, 0x13, 2, 12)
#1    power: (0x10, 0x15, 2, 12)
#4    PC: (0x10, 0x69, 2, 12)
#5    TV: (0x10, 0x7D, 2, 12)
#6    AUX: (0x10, 0x25, 2, 12)

#Epson: (sendNEC/ sednNEC2)
#7    power: (0x5583, 0x90, <numberOfRepeats>)

#Klima: (sendNEC)
#8    power: (0xE710, 0x0, <numberOfRepeats>)
*/
const int IR_SEND_PIN = 3;   // pin, do którego podłączona jest dioda IR (TX)

void setup() {
  Serial.begin(9600);
  IrSender.begin(IR_SEND_PIN);  // inicjalizacja nadajnika
  Serial.println("Nadajnik IR gotowy.");
  
  delay(2000); // chwila przerwy po starcie
}

void loop() {
  if (Serial.available()) {
    String cmd = Serial.readStringUntil('\n'); // czytamy do końca linii
    cmd.trim(); // usuwamy spacje/znaki końca linii
    
    if (cmd == "1") funkcja1();
    else if (cmd == "2") funkcja2();
    else if (cmd == "3") funkcja3();
    else if (cmd == "4") funkcja4();
    else if (cmd == "5") funkcja5();
    else if (cmd == "6") funkcja6();
    else if (cmd == "7") funkcja7();
    else if (cmd == "8") funkcja8();
    else if (cmd == "9") funkcja9();
    else if (cmd == "10") funkcja10();
    else Serial.println("Nieznana komenda.");
  }
}

// ----- przykładowe funkcje -----
void funkcja1() //Sony power on/off
{
  Serial.println("Uruchomiono funkcję 1");
  IrSender.sendSony(0x10, 0x15, 2, 12);
}
void funkcja2()
{
  Serial.println("Uruchomiono funkcję 2");
  IrSender.sendSony(0x10, 0x12, 2, 12);
}
void funkcja3()
{
  Serial.println("Uruchomiono funkcję 3");
  IrSender.sendSony(0x10, 0x13, 2, 12);
}
void funkcja4()
{
  Serial.println("Uruchomiono funkcję 4");
  IrSender.sendSony(0x10, 0x69, 2, 12);
}
void funkcja5()
{
  Serial.println("Uruchomiono funkcję 5");
  IrSender.sendSony(0x10, 0x7D, 2, 12);
}
void funkcja6()
{
  Serial.println("Uruchomiono funkcję 6");
  IrSender.sendSony(0x10, 0x25, 2, 12);
}
void funkcja7()
{
  Serial.println("Uruchomiono funkcję 7");
  IrSender.sendNEC(0x5583, 0x90, 2);
}
void funkcja8()
{
  Serial.println("Uruchomiono funkcję 8");
  IrSender.sendNEC(0xE710, 0x0, 2);
}
void funkcja9()
{
  Serial.println("Uruchomiono funkcję 9");
}
void funkcja10()
{
  Serial.println("Uruchomiono funkcję 10");
}
