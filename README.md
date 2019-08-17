# Injury Prevention Monitor - IPM / Monitor de Prevenção de Lesões - MPL

![dashboard](https://github.com/rodriguesfas/Injury-Prevention-Monitor/blob/master/user-guide/screenshot/dashboard.png)

# DashBoard

O DashBoard do Injury Prevention Monitor (IPM) no portugês Monitor de Prevenção de Lesões (MPL), foi construido utilizando o Micro-framework [Flask](http://flask.pocoo.org/). 

Flask é um pequeno framework web escrito em Python e baseado na biblioteca WSGI Werkzeug e na biblioteca de Jinja2. Flask está disponível sob os termos da Licença BSD. Flask tem a flexibilidade da linguagem de programação Python e provê um modelo simples para desenvolvimento web.

Outras tecnologia empregadas na consturção do IPM foram as linguagens de programação [Python]() e [JavaScript]() e as linguagens de marcação [HTML]() e [CSS]().

- [Python](https://www.python.org/): é uma linguagem de programação de alto nível, interpretada, de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991. [Site Oficial](https://www.python.org/)

- [JavaScript](https://pt.wikipedia.org/wiki/JavaScript): JavaScript, frequentemente abreviado como JS, é uma linguagem de programação interpretada de alto nível, caracterizada também, como dinâmica, fracamente tipificada, prototype-based e multi-paradigma. Juntamente com HTML e CSS, o JavaScript é uma das três principais tecnologias da World Wide Web. [Site Oficial](https://www.javascript.com/)

- [HTML](https://pt.wikipedia.org/wiki/HTML): é uma linguagem de marcação utilizada na construção de páginas na Web. Documentos HTML podem ser interpretados por navegadores. A tecnologia é fruto da junção entre os padrões HyTime e SGML. HyTime é um padrão para a representação estruturada de hipermídia e conteúdo baseado em tempo. [Site Oficial](https://www.w3.org/html/)

- [CSS](https://pt.wikipedia.org/wiki/Cascading_Style_Sheets): do inglês "Cascading Style Sheets" é um mecanismo para adicionar estilo a um documento web. O código CSS pode ser aplicado diretamente nas tags ou ficar contido dentro de tags. Também é possível, em vez de colocar a formatação dentro do documento, criar um link para um arquivo CSS que contém os estilos. [Site Oficial](https://www.w3.org/Style/CSS/Overview.en.html)

Todas essas tecnologias foram empregadas na criação da Interface Gráfica do Usuário (GUI) do sistema IPM.

## Instalação de Bibliotecas Dependentes do DashBoard
Execute o comando a seguir dentro do diretório dashboard.

    pip install flask
    pip install flask_socketio
    pip install socketio
    pip install gevent
    pip install pyserial

### Configuração da Porta Arduino no Servidor

Acesse o arquivo server.js nodiretório /dashboard/server.js , localize o bloco de código abaixo, e altere o nome da porta Serial conforme a porta do do seu computador. Exemplo: /dev/ttyUSB0 , /dev/ttyUSB1, /dev/ttyACM0 , entre outros.

    arduino = serial.Serial("/dev/ttyACM0", timeout=1)

# Firmware
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
	or
    sudo chmod a+rw /dev/ttyUSB0

# Inicar o Servidor DashBoard
Para iniciar o servidor que executa o DashBoard do IPM, é necessário acessar o diretório dashboard e executar no terminal o seguinte comando:

    export FLASK_APP=dashboard
    export FLASK_DEBUG=1
    
    flask run

Após executado o comando anterior, abra qualquer navegador de internet (recomendado usar o navegador [Google Chrome](https://www.google.com/intl/pt-BR/chrome/)) e digite na URL o seguinte endereço para acessar a pagina:

    http://localhost:9000
    
    ou
    
    http://127.0.0.1:9000

# Parar o Servidor DashBoard
Para parar a execução do servidor do DashBoard use o comando:

    Crtl + c

# Lista de Componentes do Protótipo

      Quant.  |            Item            |   Valor  |   Link 
    :-------: | :------------------------: | :------: | :------: 
        2     |  Sensor de Carga           | R$       | 
        1     |  Módulo Conversor HX711    | R$       |  
        1     |  Arduino Uno R3            | R$       |  
        N     |  Fios e Jumpers            | R$       |  

# Desenho Esquemático Do Protótipo

O desenho esquemático do protótipo foi construido utilizando a ferramenta de modelagem [Fretzing](https://fritzing.org/home/).

# Referências

## Artigos
- [Sistema Automático de Prevençãode Úlceras por Pressão](https://repositorio.uma.pt/handle/10400.13/75)

## Paginas Web

### Tutoriais Arduino
- [Conversor HX711: Balança Digital com Sensor de Peso e Arduino Uno](http://blog.baudaeletronica.com.br/conversor-hx711-para-balanca-eletronica/)

- [Criando uma Balança com o Arduino](https://www.robocore.net/tutoriais/celula-de-carga-hx711-com-arduino?fbclid=IwAR2aD6KqunSnPPSsosWZVWt0Pk9HB9HtG3jASjT7Ue2qxKIl7NotRoJ8ZkA)

- [SENSOR DE PESO COM ARDUINO – A VARIAÇÃO DE UM STRAIN GAGE](https://blog.usinainfo.com.br/sensor-de-peso-com-arduino-variacao-de-um-strain-gage/)


- [O Arduino funciona como uma balança? Sim! Ele é capaz! - Módulo HX711](https://www.youtube.com/watch?v=-qLfybfvsHw&feature=push-u-sub&attr_tag=cvjlzRGy3V1M0wxC%3A6)

- [Arduíno Gerando Gráficos Com Socket.io](http://clubedosgeeks.com.br/programacao/arduino-gerando-graficos-com-socket-io)

### Desing Corpo Humando
- [Humanan Atomy Illustrations Template](https://www.humananatomyillustrations.com/)

### Gráficos
- [ChartJS](https://www.chartjs.org/)
- [How to use Chart.js](https://medium.com/javascript-in-plain-english/exploring-chart-js-e3ba70b07aa4)

###

https://www.johnpreston.co.uk/blog/2017/09/29/pressure-map-technology-seats-mattresses-feet/

https://hackaday.io/project/12314-insole-pressure-system-for-mass-customised-shoes/log/40283-first-hardware-prototype

http://www.joewrightmusic.co.uk/blog.php?title=Home%20Made%20FSRs

http://labdegaragem.com/profiles/blogs/tutorial-de-como-utilizar-o-sensor-de-fo-ar-resistivo-com-arduino

https://www.filipeflop.com/produto/sensor-de-forca-resistivo-0-5-sparkfun/

http://home.roboticlab.eu/pt/examples/sensor/force

https://www.autocorerobotica.com.br/sensor-de-forca-resistivo-05

https://www.sensorprod.com/bodymapping.php

[Construir o Sensor de Força Resistiva](https://www.elprocus.com/force-sensing-resistor-technology/)

https://edisciplinas.usp.br/pluginfile.php/2376898/mod_resource/content/0/Sensores%20Piezel%C3%A9tricos.pdf

https://pt.wikipedia.org/wiki/Sensor_de_press%C3%A3o_piezoel%C3%A9trico

http://blogmasterwalkershop.com.br/arduino/como-usar-com-arduino-modulo-piezoeletrico-sensor-de-vibracao-e-toque/

https://www.researchgate.net/publication/309359183_DISPOSITIVO_PARA_ANALISE_DE_PRESSAO_PLANTAR_EM_PALMILHAS_UTILIZANDO_PIEZOELETRICOS_DE_BAIXO_CUSTO

http://www.smar.com/newsletter/marketing/index23.html

# Sensor Piezo Eletrico
https://pt.wikipedia.org/wiki/Piezoeletricidade
http://www.farnell.com/datasheets/43406.pdf
http://icp3d.50webs.com/sp4.htm

# Créditos

- [Jennifer Cabral](#)
- [Francisco Rodrigues](https://rodriguesfas.com.br)
- [Alex Ferreira](#)