import os
import django
import pandas as pd
from decimal import Decimal

# Configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from gestion.models import Articulo

def cargar_articulos():
    # Construimos la ruta absoluta relativa al script para evitar errores en Windows
    fichero = os.path.join(os.path.dirname(__file__), 'Lista de productos.xlsx')
    
    if not os.path.exists(fichero):
        print(f"Error: No encuentro el archivo {fichero}")
        return

    # Leemos el Excel
    df = pd.read_excel(fichero)
    print(f"Sincronizando {len(df)} artículos...")

    for _, fila in df.iterrows():
        # 0: Nº, 1: Descripción, 2: Unidad medida, 3: Coste, 4: Alias
        codigo_str = str(fila.iloc[0]).strip()
        desc = str(fila.iloc[1]).strip()
        u_medida = str(fila.iloc[2]).strip()
        
        try:
            coste = float(fila.iloc[3])
            coste = Decimal(str(fila.iloc[3])).quantize(Decimal("0.00"))
        except (ValueError, TypeError):
            coste = 0.0
            coste = Decimal("0.00")
            
        alias = str(fila.iloc[4]).strip() if pd.notna(fila.iloc[4]) else ""

        # Guardar en la base de datos
        Articulo.objects.update_or_create(
            codigo=codigo_str,
            defaults={
                'descripcion': desc,
                'unidad_medida': u_medida,
                'coste_unitario': coste,
                'descripcion_alias': alias,
            }
        )

    print("--- ¡IMPORTACIÓN DE ARTÍCULOS COMPLETADA! ---")

if __name__ == '__main__':
    cargar_articulos()