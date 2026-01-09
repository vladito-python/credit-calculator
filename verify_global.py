
import pandas as pd
from pruebas import cargar_comisiones_fondos, obtener_comision_global

def verify():
    print("Cargando datos...")
    datos = cargar_comisiones_fondos()
    
    # Test cases based on Excel content:
    # GLOBAL sheet: Min 1,500,000, Max 3,500,000, Commission 0.0119
    test_cases = [
        1000000,   # Below min (Should range be inclusive or handle errors?) -> Expect None based on logic
        1500000,   # At min -> Expect 0.0119
        2000000,   # Middle -> Expect 0.0119
        3500000,   # At max -> Expect 0.0119
        4000000    # Above max -> Expect None
    ]

    for monto in test_cases:
        res = obtener_comision_global(monto, datos)
        print(f"Monto: {monto}, Comision: {res}")

if __name__ == "__main__":
    verify()
