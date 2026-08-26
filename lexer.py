class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value
    
    def __repr__(self):
          return f"Token(type={self.type!r}, value={self.value!r})"


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
                else:
                    raise ValueError(f"Caracter Invalido '{string[pos]}' en posicion {pos}")
        pos += 1                                    
    if num != "":            
        s = Token('NUMBER', int(num))
        output.append(s)
            
            
    return(output)
        
#print(lexer("12+2+3"))

arbol = BinOp(Num(5), "MAS", BinOp(Num(3), "POR", Num(4)))

print(arbol)