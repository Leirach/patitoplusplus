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
si(<condicion>) entonces {
    %% bloque true
}sino{
    %% bloque false
}

```
### Ciclos

Mientras:
```
mientras (<condicion>) haz { %% mientras no se cumpla la condición
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

### 

### Input / Output

```
    var int input;
    quackout("Introducir número:"); %% output
    quackin(input); %% input

```

## Autores

Juan Carlos De León Álvarez

Blanca Leticia Badillo Guzmán

## Links

[Documentacion Patito++](http://www.example.com)
