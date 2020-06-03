    
    
    

%% Ciclos

    programa patito;  %% Se inicia el programa asignando un nombre

    %%Variables globales tipo int
    %%Pueden ser accesadas desde cualquier función

    var int input, matriz[5];

    %%Función tipo void que asigna valores a index en matriz
    funcion void asigna(int n) { 
        var int i; %%variable local a función
        desde i = 0 hasta n hacer { %%Ciclo que va desde 0 hasta n
            matriz[i] = i; %%Asigna a matriz
            quackout(matriz[i]); %%Imprime index
        }
    }
    
    %%Función print a matriz
    funcion void imprime(){
        %%Ciclo mientras
        var int i;
        i = 0;
        quackout("Valores");
        mientras (i<=4) haz { %% mientras no se cumpla la condición
            quackout(matriz[i]); %%imprime
            i = i + 1; %% incrementa variable de control
        }
    }

    %%Función tipo bool para buscar valor en matriz
    funcion bool buscar(int valor){
        var int i; %%Variable local a buscar
        i = 0;
        mientras (i<=4) haz { %% mientras no se cumpla la condición
            
            si(matriz[i] == valor) entonces {
                retorna true;
            }

            i = i + 1; %% incrementa variable de control
        }

        retorna false;
    }
    
    %% Inicio de función principal
    principal() {
        var int i, busca; %%Variable local a principal
        quackout("Introducir número:"); %%print
        quackin(input); %% read
        asigna(input); %%Llamada a función
        
        %%Como la variable matriz es global, puede ser cambiada desde cualquier
        %%scope, por lo que podemos separar la función de imprimir
        %%y se tendrán los mismos resultados
        imprime();

        %% Patito++ también cuenta con condicionales, por lo que podríamos
        %% buscar algún valor almacenado en la matriz
        quackout("Introduce un valor a buscar");
        quackin(busca);
        quackout(buscar(busca));


    }