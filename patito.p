programa hello_world; %% Comentarios

%% Variables globales
var int single, array[10], matrix[5][5];
    float precise;
    char letter;
    bool check;

%% declaracion de funciones
funcion void prueba(int val) {
    %% variables locales
    var bool test;
    %% print = quackout, read = quackin
    si (val > 5) entonces {
        quackout("cuack!");
    }
    sino {
        quackout("cuack :c");
    }
}

%% funcion principal
principal() {
    %% vars locales a principal
    quackout("Hello World!");
    prueba(6);
}