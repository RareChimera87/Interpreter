from src.lexer import lexer
import pytest

def test_identificador_con_digitos():
    tokens = lexer("x1")
    assert len(tokens) == 1
    assert tokens[0].get_type() == "IDENT"
    assert tokens[0].get_value() == "x1"

def test_identificador_largo():
    tokens = lexer("variable")
    assert len(tokens) == 1
    assert tokens[0].get_value() == "variable"

def test_identificador_no_empieza_con_digito():
    with pytest.raises(ValueError):
        lexer("1x")