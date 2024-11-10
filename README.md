# Practica7 - TeoriaDeLenguajes

##Integrantes:

##Laura Tobón
##Juan David Arismendy

Elaborar un analizador sintáctico que responda a la sintaxis de una calculadora simple. Además de admitir los tokens correctos, presentará también el resultado de la operación. Cuando ocurra un error de sintaxis deberá indicar cuál es el error.

Lenguajes: C, C++, C#, Javascript, Java, Kotlin o Python.

#Informe

1. Introducción

Este informe presenta el diseño y la implementación de un analizador sintáctico para una calculadora simple. El objetivo de este analizador es evaluar expresiones matemáticas que incluyen operaciones de suma, resta, multiplicación y división, así como paréntesis y llaves para agrupar operaciones. El analizador garantiza una evaluación precisa y proporciona mensajes de error claros y descriptivos en caso de errores de sintaxis.

2. Diseño del analizador sintáctico

El analizador sintáctico consta de varios componentes:

Lexer (Analizador léxico): Tokeniza la entrada, identificando números, operadores, paréntesis y llaves.

Parser (Analizador sintáctico): Analiza la estructura de la expresión matemática utilizando una gramática recursiva descendente. Se encarga de evaluar las operaciones y gestionar los paréntesis y llaves.

3. Funcionalidades del analizador

El analizador puede:

Evaluar expresiones matemáticas que incluyen suma, resta, multiplicación,división, paréntesis y llaves.

Manejar números negativos dentro de las expresiones.

Detectar y reportar errores de sintaxis de forma precisa y detallada, no acepta espacio entre caracteres.

Soporte para paréntesis y llaves para agrupar operaciones y alterar la precedencia de las operaciones.

Las variables pueden ser asignadas con valores numéricos y utilizadas en expresiones posteriores

4. Conclusiones

El analizador sintáctico implementado proporciona una solución robusta para evaluar expresiones matemáticas simples que incluyen operaciones básicas y paréntesis/llaves. Los mensajes de error claros facilitan la identificación y corrección de problemas en las expresiones ingresadas.

Este analizador sintáctico puede ser extendido para incluir más operaciones matemáticas y funciones, según las necesidades del básicas del usuario.