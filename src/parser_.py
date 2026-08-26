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
    
    def Get_izq(self):
            return self.izq
        
    def Get_op(self):
            return self.op
    
    def Get_der(self):
            return self.der
    


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
    
    
    def parse(self):
        res = self.expresion()
        if self.actual() is not None:
            raise ValueError("Hay argumentos de mas")
        return res
