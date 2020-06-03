# Patito ++

Compilador para el lenguaje Patito++. Proyecto final de clase de compiladores.


## Uso

Es neceseraio tener un ambiente de Python >3.7 y haber instalado **ply** en la carpeta del 
proyecto

Para instalar ply: 
```
pip install ply
```

Para compilar codigo fuente escrito en Patito++:

```
<PYTHON> patitoParser.py <filename.p>
```

Para ejecutar el código objeto generado por el compilador:

```
<PYTHON> VirtualMachine.py <filename.obj>
```

Se puede compilar y correr el archivo patito.p incluido en el repo de la siguiente manera:
```
python patitoParser.py patito.p
python VirtualMachine.py patito.obj
```

## Ejemplos

Programa helloworld.p en Patito++:
```
programa hello_world;

principal() {
    quackout("Hello World!")
}
```

## Especificaciones del lenguaje

### Estructura

Un programa tipico de patito se estructura de la siguiente forma
```
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
```

### Condicionales

```

%% declaracion de funcion
funcion bool esPar(num) {
    var int aux;
    aux = num/2;
    si(aux == 0) entonces {
        retorna true;
    }sino{
        retorna false;
    }
}

```
### Ciclos

Mientras:
```
%%Función print a matriz
funcion void imprime(limite){
    %%Ciclo mientras
    var int i;
    i = 0;
    mientras (i<=limite) haz { %% mientras no se cumpla la condición
        quackout(matriz[i]); %%imprime
        i = i + 1; %% incrementa variable de control
    }
}
```

Desde:
```
%%Función tipo void que asigna valores a index en matriz
funcion void asigna(int n) { 
    var int i; %%variable local a función
    desde i = 0 hasta n hacer { %%Ciclo que va desde 0 hasta n
        matriz[i] = i; %%Asigna a matriz
    }
}
```

### 

### Input / Output

```
%% Inicio de función principal
principal() {
    var int i, busca; %%Variable local a principal
    quackout("Introducir número:"); %% output
    quackin(input); %% input
    asigna(input); %%Llamada a función
}
```

## Autores

Juan Carlos De León Álvarez

Blanca Leticia Badillo Guzmán

## Links

[Documentacion Patito++](http://www.example.com)
