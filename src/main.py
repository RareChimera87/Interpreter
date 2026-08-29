from src.lexer import lexer
from src.parser_ import Parser
from src.interprete import Interprete

def run(text, interpre=None):
    if interpre is None:
        interpre = Interprete()
    lista = lexer(text)
    parseado = Parser(lista).parse()
    Interpret = interpre
    output = Interpret.eva(parseado)
    if output is None:
        return ""
    
    return output



if __name__ == "__main__":
    print("Escriba 'salir' para salir")
    magia = Interprete()
    while True:
        try:
            entrada = input(">>>    ")
            if entrada == "salir":
                break
            if entrada.strip() != "":
                print(run(entrada, magia))
        except ValueError as e:
            print(e)
        except ZeroDivisionError as e:
            print("Operacion Prohibida: ", e)
        except NameError as e:
            print("Unkown Variable: ", e)