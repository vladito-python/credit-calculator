import pandas as pd
import os
import math

def cargar_comisiones_fondos():
    archivo = 'COMISIONES FONDOS.xlsx'
    if not os.path.exists(archivo):
        print(f"Error: El archivo '{archivo}' no se encuentra en el directorio actual.")
        return None
    datos = pd.read_excel(archivo, sheet_name=None)
    return datos


def obtener_comision_global(monto, datos):
    if datos is None or 'GLOBAL' not in datos:
        return None
    df = datos['GLOBAL']
    for index, row in df.iloc[1:].iterrows():
            val_min = float(row.iloc[1])
            val_max = float(row.iloc[2])
            if val_min <= monto <= val_max:
                comision = row.iloc[0]
                return comision
    return None


def obtener_comision_epm023(plazo, datos):
    if datos is None or 'EMP023' not in datos:
        return None
    df = datos['EMP023']
    for index, row in df.iloc[1:].iterrows():
        val_plazo = int(row.iloc[0])
        if val_plazo == plazo:
            comision = round(row.iloc[2], 6)
            return comision
    return None


def obtener_comision_antioquia(monto, plazo, datos):
    if datos is None:
        return None
    sheet_name = None
    if 3500001 <= monto <= 5600000:
        sheet_name = 'FGA01'
    elif 5600001 <= monto <= 8600000:
        sheet_name = 'FGA02'
    elif 8600001 <= monto <= 39000000:
        sheet_name = 'FGA03'
    else:
        return None
    if sheet_name not in datos:
        return None
    df = datos[sheet_name]
    for index, row in df.iloc[2:].iterrows():
        try:
            val_plazo = int(row.iloc[0])
            if val_plazo == plazo:
                comision = round(row.iloc[2], 3)
                return comision, sheet_name
        except (ValueError, TypeError):
            continue
    return None

def obtener_credito_total(seguro, monto, comision):
    val = (monto + seguro) / (1 - comision)
    credito_total = math.ceil(val / 1000) * 1000
    return int(credito_total)


def programa_principal():
    datos = cargar_comisiones_fondos()
    if datos is None:
        return
    try:
        monto = float(input("Ingrese el monto solicitado: "))
        if monto < 1500000:
            print("Error: El monto mínimo es de $1,500,000.")
            return
        plazo = int(input("Ingrese el plazo en meses: "))
        if not (1 <= plazo <= 36):
            print("Error: El plazo debe estar entre 1 y 36 meses.")
            return
        seguro = float(input("Ingrese el valor del seguro: "))
        seguro_total = seguro * plazo
    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")
        return
    comision_global = obtener_comision_global(monto, datos)
    comision_antioquia_info = obtener_comision_antioquia(monto, plazo, datos)
    comision_emp023 = obtener_comision_epm023(plazo, datos)
    opciones = []
    if comision_global is not None:
        opciones.append({'nombre': 'FONDO GLOBAL', 'tasa': comision_global})
    if comision_antioquia_info is not None:
        tasa_ant, nombre_ant = comision_antioquia_info
        opciones.append({'nombre': f'FONDO DE ANTIOQUIA ({nombre_ant})', 'tasa': tasa_ant})
    if comision_emp023 is not None:
        opciones.append({'nombre': 'FONDO EMP023', 'tasa': comision_emp023})
    if not opciones:
        print("No se encontró ningún fondo válido para los datos ingresados.")
        return
    opciones.sort(key=lambda x: x['tasa'])
    seleccion = opciones[0]
    if ('FONDO GLOBAL' in seleccion['nombre'] or 'FONDO DE ANTIOQUIA' in seleccion['nombre']) and comision_emp023 is not None:
        if seleccion['nombre'] != 'FONDO EMP023':
            print(f"El fondo sugerido es {seleccion['nombre']} con una comisión de {seleccion['tasa']*100:.4f}%")
            print(f"Sin embargo, el fondo EMP023 también está disponible con una comisión de {comision_emp023*100:.4f}%")
            respuesta = input("¿Desea cambiar al fondo EMP023? (s/n): ").lower()
            if respuesta == 's':
                seleccion = {'nombre': 'EMP023', 'tasa': comision_emp023}
    print(f"Fondo seleccionado: {seleccion['nombre']} (Tasa: {seleccion['tasa']*100:.4f}%)")
    credito_total = obtener_credito_total(seguro_total, monto, seleccion['tasa'])
    if credito_total > 39000000:
        print(f"Error: El valor del crédito total (${credito_total:,.0f}) supera el máximo de $39,000,000.")
        return
    print("Resultados:")
    print(f"Monto solicitado: ${monto:,.0f}")
    print(f"Plazo: {plazo} meses")
    print(f"Seguro total: ${seguro_total:,.0f}")
    print(f"Comisión: ${round(seleccion['tasa']*credito_total, 2):,.0f}")
    print(f"El valor del crédito total es: ${credito_total:,.0f}")

if __name__ == '__main__':
    programa_principal()
