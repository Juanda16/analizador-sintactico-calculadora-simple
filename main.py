import lexer as AL
import parser as AS


while True:
    try:
        userInput = input("\nIngrese una operación simple: ")
        if userInput == "":
            print("Cadena vacía, ingrese una operación simple válida:")
            continue
        Lexer = AL.Lexer(userInput)
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
    print("Desea ingresar otra operación? (S/n)")
    wantToContinue = input()
    if wantToContinue == "n":
        break
    else:
        continue

