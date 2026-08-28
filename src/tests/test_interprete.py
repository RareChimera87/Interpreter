from src.main import run
from src.interprete import Interprete
import pytest

def test_suma():
    assert run("29+86") == 115
    
def test_resta():
    assert run("85-30") == 55
    
def test_multiplicacion():
    assert run("7*8") == 56
    
def test_division():
    assert run("115/2") == pytest.approx(57.5)
    
    
def test_suma_luego_mult():
    assert run("2+3*4") == 14

def test_mult_luego_suma():
    assert run("2*3+4") == 10
    
def test_rest_mult():
    assert run("10-2*3") == 4
    
    
def test_restass():
    assert run("10-3-2") == 5

def test_divisioness():
    assert run("100/5/2") == pytest.approx(10)

def test_mas_restass():
    assert run("20-5-3-2") == 10
    

def test_parentesis_cambia_precedencia():
    assert run("(2+3)*4") == 20

def test_parentesis_a_la_derecha():
    assert run("2*(3+4)") == 14

def test_parentesis_anidados():
    assert run("((1+2)*(3+4))") == 21

def test_anidamiento_profundo():
    assert run("2*(3+(4-1))") == 12

def test_parentesis_numero_solo():
    assert run("(5)") == 5

def test_dos_grupos_hermanos():
    assert run("(2+3)*(4-1)") == 15
    

def test_caracter_invalido():
    with pytest.raises(ValueError):
        run("1@2")
        
def test_asignacion_devuelve_valor():
    assert run("x = 5") == 5

def test_asignacion_con_expresion():
    assert run("x = 2 + 3 * 4") == 14

def test_variable_no_definida():
    with pytest.raises(NameError):
        run("y + 1")

def test_asignacion_encadenada():
    assert run("x = y = 8") == 8
    
def test_entorno_persiste_entre_llamadas():
    interp = Interprete()
    run("x = 5", interp)
    assert run("x + 1", interp) == 6

def test_entornos_separados_estan_aislados():
    interp = Interprete()
    run("x = 5", interp)
    with pytest.raises(NameError):
        run("x")          # sin intérprete: entorno nuevo, x no existe

def test_reasignacion():
    interp = Interprete()
    run("x = 5", interp)
    run("x = 10", interp)
    assert run("x", interp) == 10