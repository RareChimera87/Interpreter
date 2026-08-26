from src.parser_ import Num

class Interprete:
    
    def eva(self, arbol):
        if not isinstance(arbol, Num):
            izq = self.eva(arbol.Get_izq())
            
            der = self.eva(arbol.Get_der())
            
            op = arbol.Get_op()
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
            
        else:
            return arbol.get_value()
        


    