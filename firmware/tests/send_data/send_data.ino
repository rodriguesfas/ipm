/**
    Descrição: Esse código, envia dados aleatórios para o 
               DashBoard, para testar o painel de vizualização.
               A ideia principal é simular os valores lidos pelo 
               sensor de carga e exibir os resutados em um gráfico
               e na imagem do corpo humano, simulando uma possível lesão.
    
    Data: 19/07/2019
    Autor: RodriguesFAS
    Versão: 0.0.1 

    Tutorial base: https://www.arduino.cc/reference/pt/language/functions/random-numbers/random/
*/

long randNumber;

void setup()
{
    Serial.begin(9600);
    randomSeed(analogRead(0));
}

void loop()
{
    randNumber = random(0, 10);
    Serial.println(randNumber);
    delay(1000);
}