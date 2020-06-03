programa patito;

funcion int factorial(int num) {
    si (num == 0) entonces {
        retorna 1;
    }sino{
        retorna num*factorial(num-1);
    }
}

principal() {
    var int cont;
    quackout("Calcular factorial de:");
    quackin(cont);
    quackout(factorial(cont));
}