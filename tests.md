============================= test session starts ==============================
platform linux -- Python 3.14.7, pytest-9.1.1, pluggy-1.6.0
rootdir: /home/rarechimera87/Server/Projects/Interprete
collected 27 items

src/tests/test_interprete.py FFFFFFFFFFFFFFFF.FFFF.F.                    [ 88%]
src/tests/test_lexer.py ...                                              [100%]

=================================== FAILURES ===================================
__________________________________ test_suma ___________________________________

    def test_suma():
>       assert run("29+86") == 115
               ^^^^^^^^^^^^

src/tests/test_interprete.py:6: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

text = '29+86', interpre = None

    def run(text, interpre=None):
        lista = lexer(text)
        parseado = Parser(lista).parse()
        Interpret = interpre
>       output = Interpret.eva(parseado)
                 ^^^^^^^^^^^^^
E       AttributeError: 'NoneType' object has no attribute 'eva'

src/main.py:9: AttributeError
__________________________________ test_resta __________________________________

    def test_resta():
>       assert run("85-30") == 55
               ^^^^^^^^^^^^

src/tests/test_interprete.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

text = '85-30', interpre = None

    def run(text, interpre=None):
        lista = lexer(text)
        parseado = Parser(lista).parse()
        Interpret = interpre
>       output = Interpret.eva(parseado)
                 ^^^^^^^^^^^^^
E       AttributeError: 'NoneType' object has no attribute 'eva'

src/main.py:9: AttributeError
_____________________________ test_multiplicacion ______________________________

    def test_multiplicacion():
>       assert run("7*8") == 56
               ^^^^^^^^^^

src/tests/test_interprete.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

text = '7*8', interpre = None

    def run(text, interpre=None):
        lista = lexer(text)
        parseado = Parser(lista).parse()
        Interpret = interpre
>       output = Interpret.eva(parseado)
                 ^^^^^^^^^^^^^
E       AttributeError: 'NoneType' object has no attribute 'eva'

src/main.py:9: AttributeError
________________________________ test_division _________________________________

    def test_division():
>       assert run("115/2") == pytest.approx(57.5)
               ^^^^^^^^^^^^

src/tests/test_interprete.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

text = '115/2', interpre = None

    def run(text, interpre=None):
        lista = lexer(text)
        parseado = Parser(lista).parse()
        Interpret = interpre
>       output = Interpret.eva(parseado)
                 ^^^^^^^^^^^^^
E       AttributeError: 'NoneType' object has no attribute 'eva'

src/main.py:9: AttributeError
_____________________________ test_suma_luego_mult _____________________________

    def test_suma_luego_mult():
>       assert run("2+3*4") == 14
               ^^^^^^^^^^^^

src/tests/test_interprete.py:19: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

text = '2+3*4', interpre = None

    def run(text, interpre=None):
        lista = lexer(text)
        parseado = Parser(lista).parse()
        Interpret = interpre
>       output = Interpret.eva(parseado)
                 ^^^^^^^^^^^^^
E       AttributeError: 'NoneType' object has no attribute 'eva'

src/main.py:9: AttributeError
_____________________________ test_mult_luego_suma _____________________________

    def test_mult_luego_suma():
>       assert run("2*3+4") == 10
               ^^^^^^^^^^^^

src/tests/test_interprete.py:22: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

text = '2*3+4', interpre = None

    def run(text, interpre=None):
        lista = lexer(text)
        parseado = Parser(lista).parse()
        Interpret = interpre
>       output = Interpret.eva(parseado)
                 ^^^^^^^^^^^^^
E       AttributeError: 'NoneType' object has no attribute 'eva'

src/main.py:9: AttributeError
________________________________ test_rest_mult ________________________________

    def test_rest_mult():
>       assert run("10-2*3") == 4
               ^^^^^^^^^^^^^

src/tests/test_interprete.py:25: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

text = '10-2*3', interpre = None

    def run(text, interpre=None):
        lista = lexer(text)
        parseado = Parser(lista).parse()
        Interpret = interpre
>       output = Interpret.eva(parseado)
                 ^^^^^^^^^^^^^
E       AttributeError: 'NoneType' object has no attribute 'eva'

src/main.py:9: AttributeError
_________________________________ test_restass _________________________________

    def test_restass():
>       assert run("10-3-2") == 5
               ^^^^^^^^^^^^^

src/tests/test_interprete.py:29: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

text = '10-3-2', interpre = None

    def run(text, interpre=None):
        lista = lexer(text)
        parseado = Parser(lista).parse()
        Interpret = interpre
>       output = Interpret.eva(parseado)
                 ^^^^^^^^^^^^^
E       AttributeError: 'NoneType' object has no attribute 'eva'

src/main.py:9: AttributeError
_______________________________ test_divisioness _______________________________

    def test_divisioness():
>       assert run("100/5/2") == pytest.approx(10)
               ^^^^^^^^^^^^^^

src/tests/test_interprete.py:32: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

text = '100/5/2', interpre = None

    def run(text, interpre=None):
        lista = lexer(text)
        parseado = Parser(lista).parse()
        Interpret = interpre
>       output = Interpret.eva(parseado)
                 ^^^^^^^^^^^^^
E       AttributeError: 'NoneType' object has no attribute 'eva'

src/main.py:9: AttributeError
_______________________________ test_mas_restass _______________________________

    def test_mas_restass():
>       assert run("20-5-3-2") == 10
               ^^^^^^^^^^^^^^^

src/tests/test_interprete.py:35: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

text = '20-5-3-2', interpre = None

    def run(text, interpre=None):
        lista = lexer(text)
        parseado = Parser(lista).parse()
        Interpret = interpre
>       output = Interpret.eva(parseado)
                 ^^^^^^^^^^^^^
E       AttributeError: 'NoneType' object has no attribute 'eva'

src/main.py:9: AttributeError
______________________ test_parentesis_cambia_precedencia ______________________

    def test_parentesis_cambia_precedencia():
>       assert run("(2+3)*4") == 20
               ^^^^^^^^^^^^^^

src/tests/test_interprete.py:39: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

text = '(2+3)*4', interpre = None

    def run(text, interpre=None):
        lista = lexer(text)
        parseado = Parser(lista).parse()
        Interpret = interpre
>       output = Interpret.eva(parseado)
                 ^^^^^^^^^^^^^
E       AttributeError: 'NoneType' object has no attribute 'eva'

src/main.py:9: AttributeError
_________________________ test_parentesis_a_la_derecha _________________________

    def test_parentesis_a_la_derecha():
>       assert run("2*(3+4)") == 14
               ^^^^^^^^^^^^^^

src/tests/test_interprete.py:42: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

text = '2*(3+4)', interpre = None

    def run(text, interpre=None):
        lista = lexer(text)
        parseado = Parser(lista).parse()
        Interpret = interpre
>       output = Interpret.eva(parseado)
                 ^^^^^^^^^^^^^
E       AttributeError: 'NoneType' object has no attribute 'eva'

src/main.py:9: AttributeError
___________________________ test_parentesis_anidados ___________________________

    def test_parentesis_anidados():
>       assert run("((1+2)*(3+4))") == 21
               ^^^^^^^^^^^^^^^^^^^^

src/tests/test_interprete.py:45: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

text = '((1+2)*(3+4))', interpre = None

    def run(text, interpre=None):
        lista = lexer(text)
        parseado = Parser(lista).parse()
        Interpret = interpre
>       output = Interpret.eva(parseado)
                 ^^^^^^^^^^^^^
E       AttributeError: 'NoneType' object has no attribute 'eva'

src/main.py:9: AttributeError
__________________________ test_anidamiento_profundo ___________________________

    def test_anidamiento_profundo():
>       assert run("2*(3+(4-1))") == 12
               ^^^^^^^^^^^^^^^^^^

src/tests/test_interprete.py:48: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

text = '2*(3+(4-1))', interpre = None

    def run(text, interpre=None):
        lista = lexer(text)
        parseado = Parser(lista).parse()
        Interpret = interpre
>       output = Interpret.eva(parseado)
                 ^^^^^^^^^^^^^
E       AttributeError: 'NoneType' object has no attribute 'eva'

src/main.py:9: AttributeError
_________________________ test_parentesis_numero_solo __________________________

    def test_parentesis_numero_solo():
>       assert run("(5)") == 5
               ^^^^^^^^^^

src/tests/test_interprete.py:51: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

text = '(5)', interpre = None

    def run(text, interpre=None):
        lista = lexer(text)
        parseado = Parser(lista).parse()
        Interpret = interpre
>       output = Interpret.eva(parseado)
                 ^^^^^^^^^^^^^
E       AttributeError: 'NoneType' object has no attribute 'eva'

src/main.py:9: AttributeError
___________________________ test_dos_grupos_hermanos ___________________________

    def test_dos_grupos_hermanos():
>       assert run("(2+3)*(4-1)") == 15
               ^^^^^^^^^^^^^^^^^^

src/tests/test_interprete.py:54: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

text = '(2+3)*(4-1)', interpre = None

    def run(text, interpre=None):
        lista = lexer(text)
        parseado = Parser(lista).parse()
        Interpret = interpre
>       output = Interpret.eva(parseado)
                 ^^^^^^^^^^^^^
E       AttributeError: 'NoneType' object has no attribute 'eva'

src/main.py:9: AttributeError
________________________ test_asignacion_devuelve_valor ________________________

    def test_asignacion_devuelve_valor():
>       assert run("x = 5") == 5
               ^^^^^^^^^^^^

src/tests/test_interprete.py:62: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

text = 'x = 5', interpre = None

    def run(text, interpre=None):
        lista = lexer(text)
        parseado = Parser(lista).parse()
        Interpret = interpre
>       output = Interpret.eva(parseado)
                 ^^^^^^^^^^^^^
E       AttributeError: 'NoneType' object has no attribute 'eva'

src/main.py:9: AttributeError
________________________ test_asignacion_con_expresion _________________________

    def test_asignacion_con_expresion():
>       assert run("x = 2 + 3 * 4") == 14
               ^^^^^^^^^^^^^^^^^^^^

src/tests/test_interprete.py:65: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

text = 'x = 2 + 3 * 4', interpre = None

    def run(text, interpre=None):
        lista = lexer(text)
        parseado = Parser(lista).parse()
        Interpret = interpre
>       output = Interpret.eva(parseado)
                 ^^^^^^^^^^^^^
E       AttributeError: 'NoneType' object has no attribute 'eva'

src/main.py:9: AttributeError
__________________________ test_variable_no_definida ___________________________

    def test_variable_no_definida():
        with pytest.raises(NameError):
>           run("y + 1")

src/tests/test_interprete.py:69: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

text = 'y + 1', interpre = None

    def run(text, interpre=None):
        lista = lexer(text)
        parseado = Parser(lista).parse()
        Interpret = interpre
>       output = Interpret.eva(parseado)
                 ^^^^^^^^^^^^^
E       AttributeError: 'NoneType' object has no attribute 'eva'

src/main.py:9: AttributeError
__________________________ test_asignacion_encadenada __________________________

    def test_asignacion_encadenada():
>       assert run("x = y = 8") == 8
               ^^^^^^^^^^^^^^^^

src/tests/test_interprete.py:72: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

text = 'x = y = 8', interpre = None

    def run(text, interpre=None):
        lista = lexer(text)
        parseado = Parser(lista).parse()
        Interpret = interpre
>       output = Interpret.eva(parseado)
                 ^^^^^^^^^^^^^
E       AttributeError: 'NoneType' object has no attribute 'eva'

src/main.py:9: AttributeError
____________________ test_entornos_separados_estan_aislados ____________________

    def test_entornos_separados_estan_aislados():
        interp = Interprete()
        run("x = 5", interp)
        with pytest.raises(NameError):
>           run("x")          # sin intérprete: entorno nuevo, x no existe
            ^^^^^^^^

src/tests/test_interprete.py:83: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

text = 'x', interpre = None

    def run(text, interpre=None):
        lista = lexer(text)
        parseado = Parser(lista).parse()
        Interpret = interpre
>       output = Interpret.eva(parseado)
                 ^^^^^^^^^^^^^
E       AttributeError: 'NoneType' object has no attribute 'eva'

src/main.py:9: AttributeError
=========================== short test summary info ============================
FAILED src/tests/test_interprete.py::test_suma - AttributeError: 'NoneType' o...
FAILED src/tests/test_interprete.py::test_resta - AttributeError: 'NoneType' ...
FAILED src/tests/test_interprete.py::test_multiplicacion - AttributeError: 'N...
FAILED src/tests/test_interprete.py::test_division - AttributeError: 'NoneTyp...
FAILED src/tests/test_interprete.py::test_suma_luego_mult - AttributeError: '...
FAILED src/tests/test_interprete.py::test_mult_luego_suma - AttributeError: '...
FAILED src/tests/test_interprete.py::test_rest_mult - AttributeError: 'NoneTy...
FAILED src/tests/test_interprete.py::test_restass - AttributeError: 'NoneType...
FAILED src/tests/test_interprete.py::test_divisioness - AttributeError: 'None...
FAILED src/tests/test_interprete.py::test_mas_restass - AttributeError: 'None...
FAILED src/tests/test_interprete.py::test_parentesis_cambia_precedencia - Att...
FAILED src/tests/test_interprete.py::test_parentesis_a_la_derecha - Attribute...
FAILED src/tests/test_interprete.py::test_parentesis_anidados - AttributeErro...
FAILED src/tests/test_interprete.py::test_anidamiento_profundo - AttributeErr...
FAILED src/tests/test_interprete.py::test_parentesis_numero_solo - AttributeE...
FAILED src/tests/test_interprete.py::test_dos_grupos_hermanos - AttributeErro...
FAILED src/tests/test_interprete.py::test_asignacion_devuelve_valor - Attribu...
FAILED src/tests/test_interprete.py::test_asignacion_con_expresion - Attribut...
FAILED src/tests/test_interprete.py::test_variable_no_definida - AttributeErr...
FAILED src/tests/test_interprete.py::test_asignacion_encadenada - AttributeEr...
FAILED src/tests/test_interprete.py::test_entornos_separados_estan_aislados
========================= 21 failed, 6 passed in 0.06s =========================
