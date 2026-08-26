from lexer import lexer
from parser_ import Parser
from interprete import Interprete

def run(text):
    lista = lexer(text)
    parseado = Parser(lista).parse()
    Interpre = Interprete()
    output = Interpre.eva(parseado)
    
    return output



if __name__ == "__main__":
    print(run("2+3*4"))