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
    print(run("2+3*4"))