import pandas as pd
import os
import math

def cargar_datos_comisiones():
    """Carga los datos del archivo Excel"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'comisiones_de_fondo.xlsx')
    df = pd.read_excel(file_path, sheet_name='COMISIONES')
    return df

def obtener_comision_epm023(plazo, df):
    """
    Obtiene la comisión del FONDO GARANTIAS EPM023 según el plazo
    
    Args:
        plazo: Número de meses (1-36)
        df: DataFrame con los datos del Excel
        
    Returns:
        Comisión en porcentaje (ya incluye IVA)
    """
    # La columna 'PLAZO' está en la fila 1 como encabezado, los datos empiezan en fila 2
    # Buscar el plazo en las filas 2-37 (índices 2-37)
    fila = df.iloc[plazo + 1]  # +1 porque la fila 2 es plazo 1
    
    # La comisión con IVA está en la columna 'Unnamed: 3'
    comision_con_iva = fila['Unnamed: 3']
    
    # Convertir a porcentaje
    return comision_con_iva * 100

def obtener_comision_global(monto):
    """
    Obtiene la comisión del FONDO GLOBAL
    
    Args:
        monto: Monto del crédito
        
    Returns:
        Comisión en porcentaje o None si no aplica
    """
    if 1500000 <= monto <= 3500000:
        return 1.19
    return None

def obtener_comision_antioquia(monto):
    """
    Obtiene la comisión del FONDO NACIONAL DE ANTIOQUIA
    
    Args:
        monto: Monto del crédito
        
    Returns:
        Comisión en porcentaje o None si no aplica
    """
    if 3500001 <= monto <= 5600000:
        return 3.094
    elif 5600001 <= monto <= 8600000:
        return 3.808
    elif 8600001 <= monto <= 15000000:
        return 4.522
    return None

def calcular_comision(monto, plazo):
    """
    Calcula la comisión total según el monto y plazo
    
    Args:
        monto: Monto del crédito
        plazo: Plazo en meses (1-36)
        
    Returns:
        Tupla (nombre_fondo, comision_porcentaje)
    """
    # Cargar datos
    df = cargar_datos_comisiones()
    
    # Validar plazo y monto
    if plazo < 1 or plazo > 36:
        return None, "El plazo debe estar entre 1 y 36 meses\n"
    if monto < 1500000 or monto > 40000000:
        return None, "El monto debe estar entre $1.500.000 y $40.000.000\n"
    
    # Lista para guardar las opciones aplicables: (nombre_fondo, tasa)
    candidatos = []
    
    # 1. Evaluar FONDO GARANTIAS EPM023 (Siempre evaluamos este si el plazo es válido)
    try:
        comision_epm = obtener_comision_epm023(plazo, df)
        candidatos.append(("FONDO GARANTÍAS EPM023", comision_epm))
    except Exception:
        # Si falla (por ejemplo indice fuera de rango en df), no lo agregamos
        pass
    
    # 2. Evaluar FONDO GLOBAL
    comision_global = obtener_comision_global(monto)
    if comision_global is not None:
        candidatos.append(("FONDO GLOBAL", comision_global))
    
    # 3. Evaluar FONDO NACIONAL DE ANTIOQUIA
    comision_antioquia = obtener_comision_antioquia(monto)
    if comision_antioquia is not None:
        candidatos.append(("FONDO NACIONAL DE ANTIOQUIA", comision_antioquia))
        
    # Si no hay candidatos
    if not candidatos:
        return None, "No se encontró ningún fondo aplicable para este monto y plazo."
        
    # Ordenar por comisión (menor a mayor) para obtener la más económica
    # x[1] es la tasa
    candidatos.sort(key=lambda x: x[1])
    
    # Retornar la lista de candidatos
    return candidatos

def calcular_credito(monto, plazo, comision):
    seguro = int(input("\nIngrese el valor del seguro (12.000 ó 8.800): $ "))
    if seguro != 12000 and seguro != 8800:
        return None, "El valor del seguro debe ser 12.000 ó 8.800"
    seguro_total = seguro * plazo
    credito = math.ceil((seguro_total + monto) / (1 - comision / 100) / 1000)*1000
    return credito, seguro_total

def main():
    print("\nCALCULADORA DE CRÉDITO TOTAL\n")
    try:
        monto = float(input("Ingrese el monto solicitado: $ "))
        plazo = int(input("Ingrese el plazo en meses: "))
        resultado = calcular_comision(monto, plazo)
        if isinstance(resultado, tuple) and resultado[0] is None:
            print(f"\nError: {resultado[1]}")
            return
        candidatos = resultado
        seleccion = candidatos[0]
        nombre_seleccion, tasa_seleccion = seleccion
        opcion_epm = None
        for cand in candidatos:
            if cand[0] == "FONDO GARANTÍAS EPM023":
                opcion_epm = cand
                break
        if opcion_epm and nombre_seleccion != "FONDO GARANTÍAS EPM023":
            print(f"\nEl fondo seleccionado es: {nombre_seleccion} ({tasa_seleccion:.4f}%)")
            print(f"Sin embargo, está disponible: FONDO GARANTÍAS EPM023 ({opcion_epm[1]:.4f}%)")
            respuesta = input("\n¿Deseas cambiar al FONDO GARANTÍAS EPM023? (S/N): ").strip().upper()
            if respuesta == 'S':
                seleccion = opcion_epm
                nombre_seleccion, tasa_seleccion = seleccion
                print("Ha seleccionado FONDO GARANTÍAS EPM023.")
            else:
                print(f"Se mantiene {nombre_seleccion}.")
        credito, seguro_total = calcular_credito(monto, plazo, tasa_seleccion)
        if credito is None:
            print(f"\nError: {seguro_total}")
            return
        print("\nRESULTADO\n")
        print(f"Monto solicitado: ${monto:,.0f}")
        print(f"Plazo: {plazo} meses")
        print(f"Fondo aplicable: {nombre_seleccion}")
        print(f"Comisión de fondo: {tasa_seleccion:.4f}%")
        print(f"Seguro total: ${seguro_total:,.0f}")
        print(f"Valor de fondo: ${tasa_seleccion * credito / 100:,.0f}")
        print(f"\nEL valor total del Crédito es: ${credito:,.0f}\n")
    except ValueError:
        print("\nError: Debe ingresar valores numéricos válidos\n")
    except Exception as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()
