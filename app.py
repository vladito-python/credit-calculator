from flask import Flask, render_template, request, jsonify
import pandas as pd
import math
from pruebas import cargar_comisiones_fondos, obtener_comision_global, obtener_comision_antioquia, obtener_comision_epm023, obtener_credito_total

app = Flask(__name__)

# Load data once at startup
DATOS = cargar_comisiones_fondos()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.json
        monto = float(data['monto'])
        plazo = int(data['plazo'])
        seguro_mensual = float(data['seguro'])
        
        # Validations
        if monto < 1500000:
            return jsonify({'error': 'El monto mínimo es de $1,500,000.'}), 400
        if not (1 <= plazo <= 36):
            return jsonify({'error': 'El plazo debe estar entre 1 y 36 meses.'}), 400

        # Calculate costs
        seguro_total = seguro_mensual * plazo
        
        # Get commissions
        comision_global = obtener_comision_global(monto, DATOS)
        comision_antioquia_info = obtener_comision_antioquia(monto, plazo, DATOS)
        comision_emp023 = obtener_comision_epm023(plazo, DATOS)
        
        opciones = []
        if comision_global is not None:
            opciones.append({'id': 'global', 'nombre': 'FONDO GLOBAL', 'tasa': comision_global})
            
        if comision_antioquia_info is not None:
            tasa_ant, nombre_ant = comision_antioquia_info
            opciones.append({'id': 'antioquia', 'nombre': f'FONDO DE ANTIOQUIA ({nombre_ant})', 'tasa': tasa_ant})
            
        if comision_emp023 is not None:
            opciones.append({'id': 'emp023', 'nombre': 'FONDO EMP023', 'tasa': comision_emp023})
            
        if not opciones:
            return jsonify({'error': 'No se encontró ningún fondo válido para los datos ingresados.'}), 400

        # Sort by rate
        opciones.sort(key=lambda x: x['tasa'])
        seleccion = opciones[0]
        
        # Suggestion Logic
        sugerencia = None
        if ('FONDO GLOBAL' in seleccion['nombre'] or 'FONDO DE ANTIOQUIA' in seleccion['nombre']) and comision_emp023 is not None:
            if seleccion['nombre'] != 'FONDO EMP023':
                sugerencia = {
                    'actual': seleccion,
                    'alternativa': {'id': 'emp023', 'nombre': 'FONDO EMP023', 'tasa': comision_emp023}
                }

        # Calculate totals for the best option
        credito_total = obtener_credito_total(seguro_total, monto, seleccion['tasa'])
        
        if credito_total > 39000000:
            return jsonify({'error': f'El valor del crédito total (${credito_total:,.0f}) supera el máximo de $39,000,000.'}), 400

        return jsonify({
            'monto': monto,
            'plazo': plazo,
            'seguro_total': seguro_total,
            'seleccion': seleccion,
            'sugerencia': sugerencia,
            'credito_total': credito_total,
            'comision_valor': round(seleccion['tasa'] * credito_total, 0)
        })

    except ValueError:
        return jsonify({'error': 'Valores inválidos'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/recalculate', methods=['POST'])
def recalculate_specific():
    # Endpoint to force calculation with a specific fund (for the suggestion switch)
    try:
        data = request.json
        monto = float(data['monto'])
        # plazo = int(data['plazo']) # Not needed for credit calc but kept for consistency
        seguro_total = float(data['seguro_total'])
        tasa = float(data['tasa'])
        
        credito_total = obtener_credito_total(seguro_total, monto, tasa)
        
        if credito_total > 39000000:
            return jsonify({'error': f'El valor del crédito total (${credito_total:,.0f}) supera el máximo de $39,000,000.'}), 400

        return jsonify({
            'credito_total': credito_total,
            'comision_valor': round(tasa * credito_total, 0)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # For local development
    app.run(debug=True)
    # For production (Render will use gunicorn, not this block)
