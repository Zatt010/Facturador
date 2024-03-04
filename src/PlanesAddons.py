def generar_proforma(monto, nombre_plan):
    return f"Proforma para {nombre_plan} por {monto} Bs"

def agregar_addon(plan, addon):
    plan["addons"].append(addon)