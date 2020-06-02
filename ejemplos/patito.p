programa patito;
var int i[10];

funcion void init() {
    var int cont;
    desde cont = 0 hasta 9 hacer {
        i[cont] = cont + 1;
    }
}

principal() {
    var int cont;
    init();
    desde cont = 0 hasta 9 hacer {
        quackout(i[cont]); %% esto es un patito-comentario cuack
    }
}