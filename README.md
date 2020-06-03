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
    var int X; %% vars locales a principal
    quackout("Hello World!");
    prueba(6);
}
```

### Condicionales

```
si(<CONDICIÓN>) entonces {
    %% bloque true
}sino{
    %% bloque false
}

```
### Ciclos

Mientras:
```
mientras (<CONDICIÓN>) haz { %% mientras condición sea true
    %% Código del ciclo
}
```

Desde:
```
var int i; %% variable local a función
desde i = 0 hasta n hacer {     %%Ciclo que va desde 0 hasta n inclusivo
    %% codigo del ciclo
}
```

### Input / Output

```
var int input;
quackout("Introducir número:"); %% output
quackin(input); %% input
```

### Funciones

Funcion Void:

```
funcion void <NOMBRE> () {
    %% código de la función
}
```

Funcion con retorno:

```
funcion <TIPO> <NOMBRE> () {
    %% código de la función
    retorna <EXPRESION>; 
}
```

## Autores

Juan Carlos De León Álvarez

Blanca Leticia Badillo Guzmán

## Links

[Documentacion Patito++](https://docs.google.com/document/d/1qS5o_JG0cAdLHrY_L1FT6wISGaL4imzIBd7v90zgFJk/edit?usp=sharing)

[Video demo](https://drive.google.com/file/d/1eqE3nnBPwNpmLMyvsGBt0BhUYHGA9kkN/view?usp=sharing)