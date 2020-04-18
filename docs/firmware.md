## Código Arduino

[É um software interpolado num dispositivo de hardware que permite a leitura e execução de software, porém não permite modificação. O termo firmware foi originado para indicar um substituinte de hardware em microcontroladores. Em outras palavras, o firmware é um controlador de entrada e saída de baixo nível que gerencia dispositivos de hardware. No computador, ele permite a comunicação entre software e hardware. A linguagem de programação dos firmwares é, primordialmente, a linguagem de máquina, mas hoje alguns microcontroladores interpretam também, funções da linguagem C.](http://www.sbpcnet.org.br/livro/62ra/arquivos/jovem/THA%C3%8DSA%20ALVES%20ANDRADE.pdf)

O código fonte do embarcado foi escrito na linguagem [Arduino](https://www.arduino.cc/reference/pt/). Esse firmware pode ser localizado no diretório: firmware.
Dentro da pasta firmware, contem três outros três diretórios: calibration, monitorcare e tests.

- calibration: nesse diretório contem o código fonte para calibrar os sensores de carga. 

- monitorcare: nesse diretório contem o código principal do embarcado. Resulmidamente esse sistema realiza a leitura dos dados brutos dos sensores de carga e envia para o sistema IPM Dashboard.

- tests: nesse diretório contem o código de teste do sistema. Esse código basicamente gera numeros aleatorios dentro de uma faixa definida, que são enviados para o sistema IPM simulando os dados dos sensores, para testar o sistema de aquisição de dados do DashBoard.

## Instalação de Bibliotecas Dependentes do Firmware Arduino   

[HX711 - Uma biblioteca Arduino para fazer a interface entre o Conversor Analógico para Digital (ADC) 24-Bit HX711 da Avia Semiconductor para balanças de peso.](https://github.com/bogde/HX711)

### Configurações da Placa Arduino
    ttyUSB0 = "Your Port USB"

    sudo chmod 777 /dev/ttyUSB0
	ou
    sudo chmod a+rw /dev/ttyUSB0