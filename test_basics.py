import pytest
from basics import (
    limpiar_lista,
    contar_pares_impares,
    generar_tabla_multiplicar,
    filtrar_por_longitud
)


class TestLimpiarLista:
    
    def test_eliminar_duplicados_orden(self):
        resultado = limpiar_lista([1, 2, 2, 3, 1, 4])
        assert resultado == [1, 2, 3, 4]
    
    def test_lista_sin_duplicados(self):
        resultado = limpiar_lista([1, 2, 3, 4, 5])
        assert resultado == [1, 2, 3, 4, 5]
    
    def test_lista_vacia(self):
        resultado = limpiar_lista([])
        assert resultado == []
    
    def test_todos_iguales(self):
        resultado = limpiar_lista([5, 5, 5, 5])
        assert resultado == [5]
    
    def test_lista_desordenada(self):
        resultado = limpiar_lista([9,11,1,1,3,9,4,5,12,3])
        assert resultado == [1, 3, 4, 5, 9, 11, 12]


class TestContarParesImpares:
    def test_mezcla_pares_impares(self):
        resultado = contar_pares_impares([1, 2, 3, 4, 5, 6])
        assert resultado == {"pares": 3, "impares": 3}
    
    def test_solo_pares(self):
        resultado = contar_pares_impares([2, 4, 6, 8])
        assert resultado == {"pares": 4, "impares": 0}
    
    def test_solo_impares(self):
        resultado = contar_pares_impares([1, 3, 5, 7])
        assert resultado == {"pares": 0, "impares": 4}
    
    def test_lista_vacia(self):
        resultado = contar_pares_impares([])
        assert resultado == {"pares": 0, "impares": 0}
    
    def test_incluye_cero(self):
        resultado = contar_pares_impares([0, 1, 2])
        assert resultado == {"pares": 2, "impares": 1}


class TestGenerarTablaMultiplicar:
    def test_tabla_basica(self):
        resultado = generar_tabla_multiplicar(3, 5)
        assert resultado == [3, 6, 9, 12, 15]
    
    def test_tabla_por_defecto(self):
        resultado = generar_tabla_multiplicar(2)
        esperado = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
        assert resultado == esperado
    
    def test_multiplicar_por_uno(self):
        resultado = generar_tabla_multiplicar(1, 3)
        assert resultado == [1, 2, 3]
    
    def test_limite_uno(self):
        resultado = generar_tabla_multiplicar(5, 1)
        assert resultado == [5]
    
    def test_multiplicar_por_cero(self):
        resultado = generar_tabla_multiplicar(0, 3)
        assert resultado == [0, 0, 0]


class TestFiltrarPorLongitud:
    def test_filtro_basico(self):
        palabras = ["casa", "auto", "programación", "sol"]
        resultado = filtrar_por_longitud(palabras, 4)
        assert resultado == ["casa", "auto", "programación"]
    
    def test_todas_cumplen(self):
        palabras = ["python", "javascript", "programming"]
        resultado = filtrar_por_longitud(palabras, 6)
        assert resultado == ["python", "javascript", "programming"]
    
    def test_ninguna_cumple(self):
        palabras = ["a", "be", "si"]
        resultado = filtrar_por_longitud(palabras, 5)
        assert resultado == []
    
    def test_lista_vacia(self):
        resultado = filtrar_por_longitud([], 3)
        assert resultado == []
    
    def test_longitud_exacta(self):
        palabras = ["test", "word", "code"]
        resultado = filtrar_por_longitud(palabras, 4)
        assert resultado == ["test", "word", "code"]

