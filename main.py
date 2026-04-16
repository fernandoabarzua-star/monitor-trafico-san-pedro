import WazeRouteCalculator
from datetime import datetime
import os

def ejecutar_consulta():
    # Coordenadas exactas (Santiago, Chile)
    origen = "-36.828147, -73.051742" 
    destino = "-36.841757, -73.102688"
    region = 'EU' # PARA SUDAMÉRICA SIEMPRE USA 'EU'

    try:
        # 1. Conexión con Waze
        waze = WazeRouteCalculator.WazeRouteCalculator(origen, destino, region)
        
        # 2. Usamos calc_route_info() (en singular) que es más sencillo
        # Esto devuelve directamente el tiempo (min) y la distancia (km)
        tiempo, distancia = waze.calc_route_info()
        
        ahora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # 3. Preparar la línea para el CSV
        linea = f"{ahora},{tiempo:.2f},{distancia:.2f}\n"

        # 4. Guardar (modo 'a' para append)
        file_path = 'datos_trafico.csv'
        es_nuevo = not os.path.exists(file_path)
        
        with open(file_path, mode='a', encoding='utf-8') as f:
            if es_nuevo:
                f.write("Fecha_Hora,Tiempo_Minutos,Distancia_KM\n")
            f.write(linea)
            
        print(f"✅ Registro exitoso: {ahora} | {tiempo:.2f} min")

    except Exception as e:
        # Esto nos dirá exactamente qué falla si algo sale mal
        print(f"❌ Error detallado: {type(e).__name__} - {e}")

if __name__ == "__main__":
    ejecutar_consulta()
