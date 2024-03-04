from src.PlanesAddons import generar_proforma, agregar_addon

def test_generar_proforma():
    assert generar_proforma(30, "Plan B") == "Proforma para Plan B por 30 Bs"

def test_agregar_addon():
    plan = {"nombre": "Plan C", "addons": []}
    agregar_addon(plan, {"nombre": "Addon X", "precio": 15})
    assert len(plan["addons"]) == 1