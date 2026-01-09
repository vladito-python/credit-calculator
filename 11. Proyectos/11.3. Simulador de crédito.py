import math

print("\n--- Simulador de Crédito ---")

def simulador_credito():
    while True:
        monto_solicitado = 0
        plazo_meses = 0
        tasa_anual = 0
        valor_seguro_mensual = 12000
        comision_fondo = 0.0119
        try:
            monto_solicitado = int(input("\nIngrese el monto solicitado (entre $1.500.000 y $80.000.000): "))
            if monto_solicitado not in range(1500000, 80000001):
                print("\nEl monto debe estar entre $1.500.000 y $80.000.000")
                continue
            plazo_meses = int(input("\nIngrese el plazo en meses (entre 12 y 60 meses): "))
            if plazo_meses not in range(12, 61):
                print("\nEl plazo debe estar entre 12 y 60 meses\n")
                continue
            tasa_anual = float(input("\nIngrese la tasa de interés anual (en porcentaje): "))
            tasa_mensual = (tasa_anual / 100) / 12
            valor_seguro_total = valor_seguro_mensual * plazo_meses
            valor_credito = math.ceil(((monto_solicitado + valor_seguro_total) / (1 - comision_fondo)) / 1000) * 1000
            valor_fondo = valor_credito * comision_fondo
            print(f"\n--- Detalle del Crédito ---\n")
            print(f"Monto Solicitado:               ${monto_solicitado:,}")
            print(f"Plazo:                          {plazo_meses} meses")
            print(f"Seguro Total:                   ${valor_seguro_total:,} (12.000 por mes)")
            print(f"Comisión Fondo (11.9%):         ${valor_fondo:,.0f}")
            print(f"Tasa mensual:                   {tasa_mensual*100:.2f}%")
            print(f"----------------------------------------")
            print(f"VALOR TOTAL CRÉDITO:            ${valor_credito:,}")
            def calcular_cuota(monto, plazo, tasa):
                return monto * (tasa / (1 - (1 + tasa) ** - plazo))
            cuota = calcular_cuota(valor_credito, plazo_meses, tasa_mensual)
            return f"CUOTA MENSUAL:                  ${cuota:,.0f}\n"
        except ValueError:
            print("\nError: Ingrese solo números válidos")

if __name__ == "__main__":
    print(simulador_credito())

while True:
    continuar = ""
    try:
        continuar = input("¿Desea realizar otra simulación? escriba 's' para continuar o 'n' para salir: ")
    except ValueError:
        print("\nError: Ingrese solo 's' para continuar o 'n' para salir.\n")
    if continuar.lower() == "n":
        print("\nGracias por usar el simulador de crédito. Hasta luego!\n")
        break
    elif continuar.lower() == "s":
        print(simulador_credito())
    else:
        print("\nError: Ingrese solo 's' para continuar o 'n' para salir.\n")