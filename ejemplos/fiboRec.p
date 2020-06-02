programa patito;

funcion int fibo(int n) {
    si (n == 0) entonces {
        retorna 0;
    }
    si (n <= 2) entonces {
        retorna 1;
    }
    sino {
        retorna fibo(n-1) + fibo(n-2);
    }
}

principal() {
    var int N;
    quackout("Cuantos?");
    quackin(N);
    quackout(fibo(N));
}