import os
import django
import pandas as pd

# Configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from gestion.models import Cliente

def ejecutar_importacion():
    archivo = os.path.join('venv', 'clientes.xlsx')
    if not os.path.exists(archivo):
        print(f"❌ Error: No encuentro el archivo {archivo}")
        return

    print("⏳ Importando clientes a Agua y Jabón...")
    df = pd.read_excel(archivo)
    total_filas = len(df)
    print(f"⏳ Sincronizando {total_filas} clientes a Agua y Jabón...")
    
    codigos_en_excel = []
    creados = 0
    actualizados = 0

    for _, row in df.iterrows():
        # Limpieza del código: evitamos el ".0" si Excel lo lee como número
        val_codigo = row.iloc[0]
        if pd.isna(val_codigo) or pd.isna(row.iloc[1]):
            continue  # Salta si el código o el nombre están vacíos
        
        # Aseguramos que el código sea un string limpio, eliminando el .0 de Excel
        codigo_bc = str(val_codigo).replace('.0', '').strip()
        codigos_en_excel.append(codigo_bc)
        nombre = str(row.iloc[1]).strip() if pd.notna(row.iloc[1]) else "Sin nombre"
        
        obj, created = Cliente.objects.update_or_create(
            codigo_bc=codigo_bc, 
            defaults={
                'nombre': nombre,
                'alias': str(row.iloc[2]).strip() if pd.notna(row.iloc[2]) else "",
                'direccion_2': str(row.iloc[3]).strip() if pd.notna(row.iloc[3]) else "",
                'cif_nif': str(row.iloc[4]).strip() if pd.notna(row.iloc[4]) else "",
                'direccion': str(row.iloc[5]).strip() if pd.notna(row.iloc[5]) else "",
                'telefono': str(row.iloc[6]).strip() if pd.notna(row.iloc[6]) else "",
                'contacto': str(row.iloc[7]).strip() if pd.notna(row.iloc[7]) else "",
                'activo': True,
            }
        )
        
        if created:
            print(f" ✨ Nuevo: {codigo_bc} - {nombre}")
            creados += 1
        else:
            print(f" 🔄 Actualizado: {codigo_bc} - {nombre}")
            actualizados += 1

    # Limpieza: Desactivar clientes que están en la DB pero NO en el Excel actual
    desactivados = Cliente.objects.filter(activo=True).exclude(codigo_bc__in=codigos_en_excel).update(activo=False)

    print(f"\n✅ ¡Sincronización finalizada!")
    print(f"📊 Resumen: {creados} nuevos, {actualizados} actualizados, {desactivados} desactivados.")

if __name__ == '__main__':
    ejecutar_importacion()