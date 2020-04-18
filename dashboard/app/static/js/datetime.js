function exibeDataHora(div) {

    //cria um objeto do tipo date
    var data = new Date();

    // obtem o dia, mes e ano
    dia = data.getDate();
    mes = data.getMonth() + 1;
    ano = data.getFullYear();

    //obtem as horas, minutos e segundos
    horas = data.getHours();
    minutos = data.getMinutes();
    segundos = data.getSeconds();

    //converte as horas, minutos e segundos para string
    str_horas = new String(horas);
    str_minutos = new String(minutos);
    str_segundos = new String(segundos);

    //se tiver menos que 2 digitos, acrescenta o 0
    if (str_horas.length < 2)
        str_horas = 0 + str_horas;
    if (str_minutos.length < 2)
        str_minutos = 0 + str_minutos;
    if (str_segundos.length < 2)
        str_segundos = 0 + str_segundos;

    //converte o dia e o mes para string
    str_dia = new String(dia);
    str_mes = new String(mes);

    //se tiver menos que 2 digitos, acrescenta o 0
    if (str_dia.length < 2)
        str_dia = 0 + str_dia;
    if (str_mes.length < 2)
        str_mes = 0 + str_mes;

    //cria a string que sera exibida na div
    data = str_dia + '/' + str_mes + '/' + ano + ' - ' + str_horas + ':' + str_minutos + ':' + str_segundos;

    //exibe a string na div
    document.getElementById(div).innerHTML = data;

    //executa a funcao com intervalo de 1 segundo
    setTimeout("exibeDataHora('hora')", 1000);
}