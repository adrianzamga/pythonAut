import pandas as pd

archivo = ".xlsx"

df = pd.read_excel(archivo)

nuevas_filas = []

for _, fila in df.iterrows():
    # Agregar fila original
    nuevas_filas.append(fila.to_dict())

    # Agregar fila "Child of Staff"
    nuevas_filas.append({
        "Pupil Id": fila["Pupil Id"],
        "Custom Field Name": "Child of Staff",
        "Value": "No"
    })

# Crear nuevo DataFrame
df_nuevo = pd.DataFrame(nuevas_filas)

df_nuevo.to_excel("Staff_actualizado.xlsx", index=False)

print("Archivo creado correctamente.")