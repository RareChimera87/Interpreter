from src.parser_ import Num, Var, BinOp, Asignacion, Programa

class Interprete:
    def __init__(self):
        self.environment = {}

    def assign(self, name, value):
        self.environment[name] = value
        
    def get(self, name):
        if name in self.environment:
            return self.environment[name]
        raise NameError(f"Variable '{name}' not defined")
    
    def num_type(self, num):
        return num.get_value()
    
    def var_type(self, var):
        return self.get(var.get_name())
    
    def asignacion_type(self, asignacion):
        name = asignacion.get_name()
        value = self.check_type(asignacion.get_value())
        
        self.assign(name, value)
        return self.get(name)
    
    def programa_type(self, programa):
        value = None
        for i in programa.get_value():
            value = self.check_type(i)
        return value
        
    
    def binOp_type(self, binop):
    
        izq = self.check_type(binop.get_izq())
        
        der = self.check_type(binop.get_der())
        
        op = binop.get_op()
        if op == "MAS":
            return izq + der
        elif op == "MENOS":
            return izq - der
        elif op == "POR":
            return izq * der
        elif op == "DIVIDE":
            return izq / der
        else:
            raise ValueError("Operador no conocido") 
        
        
    def check_type(self, value):
        if isinstance(value, Num):
            value = self.num_type(value)
        elif isinstance(value, Var):
            value = self.var_type(value)
        elif isinstance(value, BinOp):
            value = self.binOp_type(value)
        elif isinstance(value, Asignacion):
            value = self.asignacion_type(value)
        elif isinstance(value, Programa):
            value = self.programa_type(value)
        else:
            raise ValueError("Unkown type")
        
        return value

    def eva(self, arbol):
        return self.check_type(arbol)
        
        


    