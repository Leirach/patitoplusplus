programa patito;

funcion int factorial(int num) {
    var int aux, i;
    aux = 1;
    desde i = 2 hasta num hacer {
        aux = aux*i;
    }
    return aux;
}

principal() {
    var int cont;
    quackout("Calcular factorial de: ");
    quackin(cont);
    quackout(factorial(factorial(cont)));
}