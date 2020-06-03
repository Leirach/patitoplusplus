programa hello_world; %% Comentarios

%% Variables globales
var int array[10], matrix[5][5];

%% declaracion de funciones
funcion void init() {
    var int i;
    desde i = 0 hasta 4 hacer {
        matrix[i][i] = i;
    }
}

%% funcion principal
principal() {
    var int i, limite;
    i = 1/0;
    quackin(limite);
    desde i = 0 hasta limite hacer {
        quackout(matrix[i][i]);
    }
}