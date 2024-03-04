from src.Clientes import Cliente

def test_cliente_creacion():
    cliente = Cliente("John Doe", "john@example.com")
    assert cliente.nombre == "John Doe"
    assert cliente.correo == "john@example.com"