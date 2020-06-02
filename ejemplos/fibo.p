programa patito;

funcion void fibo(int cont) {
    var int fibo1, fibo2, aux, i;
    fibo1 = 0;
    fibo2 = 1;
    desde i = 0 hasta cont hacer {
        quackout(fibo1);
        aux = fibo1 + fibo2;
        fibo1 = fibo2;
        fibo2 = aux;
    }
}

principal() {
    var int cont;
    quackin(cont);
    fibo(cont);
}