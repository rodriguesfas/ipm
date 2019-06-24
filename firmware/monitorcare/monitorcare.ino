/**

*/
#include "HX711.h"

#define DOUT A0
#define CLK A1

HX711 bau;                        // instancia Balança HX711
float calibration_factor = 34730; // fator de calibração aferido na Calibração

void setup()
{
  Serial.begin(9600);
  bau.begin(DOUT, CLK);              // inicializa a balança
  bau.set_scale(calibration_factor); // ajusta fator de calibração
  bau.tare();                        // zera a Balança
}
void loop()
{
  Serial.print("Peso: ");
  Serial.print(bau.get_units(), 3); // imprime peso na balança com duas casas decimais
  Serial.println(" kg");            // imprime no monitor serial

  delay(500);

  if (Serial.available()) // se a serial estiver disponivel
  {
    char temp = Serial.read();      // le carcter da serial
    if (temp == 't' || temp == 'T') // se pressionar t ou T
    {
      bau.tare();                        // zera a balança
      Serial.println(" Balança zerada"); // imprime no monitor serial
    }
  }
}
