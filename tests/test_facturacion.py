import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.Facturacion import calcular_total_factura, aplicar_descuento

def test_calcular_total_factura():
    assert calcular_total_factura(50, 1.5) == 75.0

def test_aplicar_descuento():
    assert aplicar_descuento(100, 10) == 90
