#from lexer import lexer

class Num:
    def __init__(self, value):
          self.value = value
    
    def __repr__(self):
          return f"Num(Value={self.value!r})"
      
    def get_value(self):
        return self.value
   
      
class BinOp:
    def __init__(self, izq, op, der):
          self.izq = izq
          self.op = op
          self.der = der
          
    def __repr__(self):
          return f"BinOp(Izquierda={self.izq}, Operador={self.op!r}, Derecha={self.der})"
    
    def get_izq(self):
            return self.izq
        
    def get_op(self):
            return self.op
    
    def get_der(self):
            return self.der
    
class Var:
    def __init__(self, name):
          self.name = name
    
    def __repr__(self):
          return f"Var(Name={self.name!r})"
       
    def get_name(self):
        return self.name

class Asignacion:
    def __init__(self, name, value):
              self.value = value
              self.name = name
        
    def __repr__(self):
            return f"Asignacion(Name={self.name!r}, Value={self.value!r})"
    
    def get_value(self):
            return self.value
    
    def get_name(self):
            return self.name

class Parser:
    def __init__(self, lista, posicion=0):
        self.lista=lista
        self.posicion=posicion
    
    def actual(self):
        if self.posicion < len(self.lista):
            #print(self.lista[self.posicion])
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
            return Num(act.get_value())
        elif self.es_tipo("LPAREN"):
            self.procesar()
            res = self.expresion()
            if not self.es_tipo("RPAREN"):
                raise ValueError("Falta un parantesis de cierre")
            self.procesar()
            return res
        elif self.es_tipo("IDENT"):
            act = self.procesar()
            return Var(act.get_value())
        else:
            raise ValueError("Se esperaba un numero o parentesis")
    
    def termino(self):
        izq = self.factor()
        while self.es_tipo("POR", "DIVIDE"): 
            operador = self.procesar().get_type()
            der = self.factor()
            izq = BinOp(izq, operador, der)
            
        return izq

    def expresion(self):
        izq = self.termino()
        while self.es_tipo("MAS", "MENOS"): 
            operador = self.procesar().get_type()
            der = self.termino()
            izq = BinOp(izq, operador, der)
            
        return izq
    
    def asignacion(self):
        izq = self.expresion()
        if not self.es_tipo("ASIGNAR"):
            return izq
        if isinstance(izq,Var):
            self.procesar()
            der = self.asignacion()
            return Asignacion(izq.get_name(), der)
        else:
            raise ValueError("Erro de operacion")

    
    def es_tipo(self, *tipos):
        actual = self.actual()
        return actual is not None and actual.get_type() in tipos
    
    
    def parse(self):
        res = self.asignacion()
        if self.actual() is not None:
            raise ValueError("Hay argumentos de mas")
        return res


# Prueba=Parser(lexer("x=5")).parse()
# print(Prueba)