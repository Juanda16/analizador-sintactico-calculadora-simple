import lexical_analyzer as AL
import parser as AS


while True:
    userInput = input("Ingrese una operación simple: ")
    Lexer = AL.LexicalAnalyzer(userInput)
    Lexer.generarTokens()
    tokens = Lexer.getListaTokens()

    print("Estos son los tokens generados por el analizador léxico ")
    print(tokens)
    print(
        "Este es el resultado del análisis sintáctico de los tokens(si retorna un número, es una cadena válida)"
    )
    try:
        Parser = AS.Parser(tokens)
        print(Parser.parse())
    except ZeroDivisionError:
        print("Error matemático, división entre cero")
    except Exception:
        print("Expresión Inválida")
    print("Desea ingresar otra operación? (s/n)")
    wantToContinue = input()
    if wantToContinue == "n":
        break
    else:
        continue

