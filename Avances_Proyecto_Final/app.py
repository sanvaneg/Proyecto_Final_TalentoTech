
from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('formulario.html')  # Asegúrate de que el archivo HTML esté en la carpeta templates

@app.route('/calcular', methods=['POST'])
def calcular():
    consumo_mensual = float(request.form['consumo'])
    opcion = request.form['opcion']
    
    # Cargar datos desde un archivo CSV en línea
    url_csv = "URL_DEL_CSV"  # Reemplaza con la URL de tu archivo CSV
    df = pd.read_csv(url_csv)

    # Supongamos que el CSV tiene columnas 'produccion_total' y 'produccion_renovable'
    produccion_total = df['produccion_total'].sum()
    produccion_renovable = df['produccion_renovable'].sum()

    porcentaje_consumo = (consumo_mensual / produccion_total) * 100
    porcentaje_renovable = (produccion_renovable / produccion_total) * 100

    return f"Porcentaje de consumo: {porcentaje_consumo:.2f}%<br>Porcentaje de energía renovable: {porcentaje_renovable:.2f}%"

if __name__ == '__main__':
    app.run(debug=True)
