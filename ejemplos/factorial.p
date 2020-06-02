programa patito;

funcion void factorial(int num) {
    var int aux, i;
    aux = 1;
    desde i = 2 hasta num hacer {
        aux = aux*i;
    }
    quackout(aux);
}

principal() {
    var int cont;
    quackout("Calcular factorial de: ");
    quackin(cont);
    factorial(factorial(2));
}