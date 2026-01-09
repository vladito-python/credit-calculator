
import pandas as pd
try:
    df = pd.read_excel('COMISIONES FONDOS.xlsx', nrows=5)
    print("Columnas:", df.columns.tolist())
    print("Primeras filas:\n", df.head())
except Exception as e:
    print(f"Error reading excel: {e}")
