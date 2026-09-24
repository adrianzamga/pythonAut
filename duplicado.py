import pandas as pd

df = pd.read_excel(".xlsx")

# Revisa los primeros datos
print(df.head())

# Crear columna "Estado" para marcar duplicados en la columna L
df["Estado"] = df["L"].duplicated(keep=False).map({True: "Duplicado", False: "Único"})

df.to_excel("resultado_con_duplicados.xlsx", index=False)

print("Archivo generado: resultado_con_duplicados.xlsx")
