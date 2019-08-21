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

long data[3];

void setup()
{
    Serial.begin(9600);
    randomSeed(analogRead(0));
}

void loop()
{
    data[1] = random(0, 100);
    data[2] = random(11, 100);
    data[3] = random(21, 100);
    data[4] = random(0, 100);

    // Create JSON as a message.
    String jsonString = "{\"s1\":\"";
    jsonString += data[1];
    jsonString +="\",\"s2\":\"";
    jsonString += data[2];
    jsonString +="\",\"s3\":\"";
    jsonString += data[3];
    jsonString +="\",\"s4\":\"";
    jsonString += data[4];
    jsonString +="\"}";

    // Send message.
    Serial.println(jsonString);

    delay(1000);
}
