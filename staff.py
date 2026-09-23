import pandas as pd

archivo1 = "S.xlsx"
archivo2 = "V.xlsx"

df1 = pd.read_excel(archivo1)
df2 = pd.read_excel(archivo2)

df1.columns = df1.columns.astype(str).str.strip()
df2.columns = df2.columns.astype(str).str.strip()

matricula1 = "Número de empleado"
matricula2 = "Staff Id"

equivalencias = {
    "Parentesco con el contacto": "Relation Type",
    "Primer Nombre": "Forename",
    "Segundo Nombre": "Middle Names",
    "Apellidos de Contacto": "Surname",
    "Dirección de domicilio actual de contacto": "Address 1",
    "Teléfono de Contacto": "Mobile",
    "Email de Contacto": "Email"
}

# bloque para eliminar matrículas duplicadas del archivo 1
df1 = df1.drop_duplicates(
    subset=[matricula1],
    keep="first"
)

# matrícula como identificador
df1 = df1.set_index(matricula1)
df2 = df2.set_index(matricula2)

for columna1, columna2 in equivalencias.items():
    df2[columna2] = df1[columna1].reindex(df2.index)


df2 = df2.reset_index() # Restaurar matrícula

df2.to_excel("archivo2_actualizado.xlsx", index=False)

print("Archivo actualizado correctamente.")