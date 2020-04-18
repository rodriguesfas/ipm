# DashBoard

![dashboard]()

## Tecnologias utilizadas na construção do DashBoard

Todas essas tecnologias a seguir, foram empregadas na criação da Interface Gráfica do Usuário (GUI) do sistema IPM.

[Flask](http://flask.pocoo.org/) é um pequeno framework web escrito em Python e baseado na biblioteca WSGI Werkzeug e na biblioteca de Jinja2. Flask está disponível sob os termos da Licença BSD. Flask tem a flexibilidade da linguagem de programação Python e provê um modelo simples para desenvolvimento web.

Outras tecnologia empregadas na consturção do IPM foram as linguagens de programação [Python]() e [JavaScript]() e as linguagens de marcação [HTML]() e [CSS]().

- [Python](https://www.python.org/): é uma linguagem de programação de alto nível, interpretada, de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991. [Site Oficial](https://www.python.org/)

- [JavaScript](https://pt.wikipedia.org/wiki/JavaScript): JavaScript, frequentemente abreviado como JS, é uma linguagem de programação interpretada de alto nível, caracterizada também, como dinâmica, fracamente tipificada, prototype-based e multi-paradigma. Juntamente com HTML e CSS, o JavaScript é uma das três principais tecnologias da World Wide Web. [Site Oficial](https://www.javascript.com/)

- [HTML](https://pt.wikipedia.org/wiki/HTML): é uma linguagem de marcação utilizada na construção de páginas na Web. Documentos HTML podem ser interpretados por navegadores. A tecnologia é fruto da junção entre os padrões HyTime e SGML. HyTime é um padrão para a representação estruturada de hipermídia e conteúdo baseado em tempo. [Site Oficial](https://www.w3.org/html/)

- [CSS](https://pt.wikipedia.org/wiki/Cascading_Style_Sheets): do inglês "Cascading Style Sheets" é um mecanismo para adicionar estilo a um documento web. O código CSS pode ser aplicado diretamente nas tags ou ficar contido dentro de tags. Também é possível, em vez de colocar a formatação dentro do documento, criar um link para um arquivo CSS que contém os estilos. [Site Oficial](https://www.w3.org/Style/CSS/Overview.en.html)


## Instalação das Bibliotecas Dependentes para o DashBoard
Execute o comando a seguir dentro do diretório dashboard.

    sudo pip install -r requirements.txt

    ou

    pip3 install cffi

## Configuração da Porta Arduino no Servidor

Acesse o arquivo serial_monitor.py nodiretório /dashboard/app/arduino , localize o bloco de código abaixo, e altere o nome da porta Serial conforme a porta USB do seu computador. 

Exemplos: /dev/ttyUSB0 , /dev/ttyUSB1, /dev/ttyACM0 , entre outros.

    port = "/dev/ttyACM0"

# Iniciando o Servidor
Para iniciar o servidor que executa o DashBoard do IPM, é necessário acessar o diretório dashboard e executar no terminal o seguinte comando:

    python run.py

Após executado o comando anterior, abra qualquer navegador de internet (recomendado usar o navegador [Google Chrome](https://www.google.com/intl/pt-BR/chrome/)) e digite na URL o seguinte endereço para acessar a pagina:

    http://localhost:9000
    ou
    http://127.0.0.1:9000

# Parando o Servidor
Para parar a execução do servidor do DashBoard use o comando:

    Crtl + c