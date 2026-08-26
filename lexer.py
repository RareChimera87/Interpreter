class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value
    
    def __repr__(self):
          return f"Token(type={self.type!r}, value={self.value!r})"
      
    def Get_type(self):
        return self.type
    
    def Get_value(self):
            return self.value


class Num:
    def __init__(self, value):
          self.value = value
    
    def __repr__(self):
          return f"Num(Value={self.value!r})"
      
class BinOp:
    def __init__(self, izq, op, der):
          self.izq = izq
          self.op = op
          self.der = der
          
    def __repr__(self):
          return f"BinOp(Izquierda={self.izq}, Operador={self.op!r}, Derecha={self.der})"

class Parser:
    def __init__(self, lista, posicion=0):
        self.lista=lista
        self.posicion=posicion
    
    def actual(self):
        if self.posicion < len(self.lista):
            return self.lista[self.posicion]
        else:
            return None
    
    def procesar(self):
        act = self.actual()
        self.posicion += 1
        return act
    
    def factor(self):
        
        if self.es_tipo("NUMBER"):
            act = self.procesar()
            return Num(act.Get_value())
        elif self.es_tipo("LPAREN"):
            self.procesar()
            res = self.expresion()
            if not self.es_tipo("RPAREN"):
                raise ValueError("Falta un parantesis de cierre")
            self.procesar()
            return res
        else:
            raise ValueError("Se esperaba un numero o parentesis")
    
    def termino(self):
        izq = self.factor()
        while self.es_tipo("POR", "DIVIDE"): 
            operador = self.procesar().Get_type()
            der = self.factor()
            izq = BinOp(izq, operador, der)
            
        return izq

    def expresion(self):
        izq = self.termino()
        while self.es_tipo("MAS", "MENOS"): 
            operador = self.procesar().Get_type()
            der = self.termino()
            izq = BinOp(izq, operador, der)
            
        return izq
    
    def es_tipo(self, *tipos):
        actual = self.actual()
        return actual is not None and actual.Get_type() in tipos
             

            


                

def lexer(string):
    output = []
    pos = 0
    #print(string)
    num = ""
    while pos < len(string):
        #print(len(string))
        if string[pos] != " ":    
            #print(string[pos])
            if string[pos].isdigit():
                #print("eeeeeeeeeeee")
                num += string[pos]
                #print(num)
            else:
                
                #print("num: " + num)
                if num != "":
                    s = Token('NUMBER', int(num))
                    output.append(s)
                    num = ""
                if string[pos] == "+":
                    s = Token("MAS")
                    output.append(s)
                elif string[pos] == "-":
                            s = Token("MENOS")
                            output.append(s)
                elif string[pos] == "/":
                            s = Token("DIVIDE")
                            output.append(s)
                elif string[pos] == "*":
                            s = Token("POR")
                            output.append(s)
                elif string[pos] == "(":
                            s = Token("LPAREN")
                            output.append(s)
                elif string[pos] == ")":
                            s = Token("RPAREN")
                            output.append(s)
                else:
                    raise ValueError(f"Caracter Invalido '{string[pos]}' en posicion {pos}")
        pos += 1                                    
    if num != "":            
        s = Token('NUMBER', int(num))
        output.append(s)
            
            
    return(output)
        

#arbol = BinOp(Num(5), "MAS", BinOp(Num(3), "POR", Num(4)))

#print(arbol)

#Prueba=Parser(lexer("2*3+4")).expresion()
#print(lexer("(1+2)"))
print(Parser(lexer("(2+3)*4")).expresion())