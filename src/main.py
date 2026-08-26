from src.lexer import lexer
from src.parser_ import Parser
from src.interprete import Interprete

def run(text):
    lista = lexer(text)
    parseado = Parser(lista).parse()
    Interpre = Interprete()
    output = Interpre.eva(parseado)
    
    return output



if __name__ == "__main__":
    print("Escriba 'salir' para salir")
    while True:
        try:
            entrada = input(">>>    ")
            if entrada == "salir":
                break
            if entrada.strip() != "":
                print(run(entrada))
        except ValueError as e:
            print(e)
        except ZeroDivisionError as e:
            print("Operacion Prohibida: ", e)