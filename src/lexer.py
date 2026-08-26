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

            

def lexer(string):
    output = []
    pos = 0
    #print(string)
    num = ""
    while pos < len(string):
        #print(len(string))
        #if string[pos] != " ":    
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
            elif string[pos] == " ":
                        pass
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

#algo = Interprete()
#algo.eva(((Parser(lexer("2+3*4")).parse())))

#print(Interprete().eva(Parser(lexer("2+3*4")).parse()))