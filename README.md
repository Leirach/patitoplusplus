# Patito ++

Compilador para el lenguaje Patito++. Proyecto final de clase de compiladores.


### Uso

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

## Specificaciones del lenguaje

Un programa tipico de patito se estructura de la siguiente forma
```

```


## Autores

Juan Carlos De León Álvarez

Blanca Leticia Badillo Guzmán

[Documentacion Patito++](http://www.example.com)
