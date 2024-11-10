import lexical_analyzer as AL
import parser as AS


while True:
    try:
        userInput = input("\nIngrese una operación simple: ")
        Lexer = AL.LexicalAnalyzer(userInput)
        Lexer.generarTokens()
        tokens = Lexer.getListaTokens()

        print("Tokens generados por el analizador léxico: ")
        print(tokens)
        print(
            "Resultado (si retorna un número, es una cadena válida):"
        )
    
        Parser = AS.Parser(tokens)
        print(Parser.parse())
    except ZeroDivisionError:
        print("Error matemático, división entre cero")
    except ValueError as e:
        print(e)
    except Exception as e:
        print("Expresión Inválida: ", e)
    print("Desea ingresar otra operación? (s/n)")
    wantToContinue = input()
    if wantToContinue == "n":
        break
    else:
        continue

