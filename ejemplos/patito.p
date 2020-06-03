    
    programa patito;  %% Se inicia el programa asignando un nombre
    var int contador, matriz[5][5];
    funcion void asigna(int n) { %% función tipo int para hacer los cálculos
        var int i;
        desde i = 0 hasta n haz{
            matriz[i][i] = i*n;
        }
    }

    %% Inicio de función principal
    principal() {
        var int i;
        quackout("Introducir número:"); %%print
        quackin(contador); %% read
        quackout(asigna(n)); %%print

        desde i = 0 hasta n haz{
            quackout(matriz[i][i]);
        }
    }