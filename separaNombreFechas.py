import pandas as pd

def separarNombresApellidoZ(nombreCompleto):

    if pd.isna(nombreCompleto):
        return "", "", ""

    partes = str(nombreCompleto).split()

    if len(partes) >= 3:

        apellido_paterno = partes[0]

        apellido_materno = partes[1]

        nombres = " ".join(partes[2:])
        
    elif len(partes) == 2:

        apellido_paterno = partes[0]
        apellido_materno = ""
        nombres = partes[1]

    elif len(partes) == 1:

        nombres = partes[0]
        apellido_paterno = ""
        apellido_materno = ""

    else:

        nombres = ""
        apellido_paterno = ""
        apellido_materno = ""

    return nombres, apellido_paterno, apellido_materno

df = pd.read_excel("archivo_limpio.xlsx")

print("Columnas encontradas:")
print(df.columns)

df[["Nombres", "ApellidoP", "ApellidoM"]] = (
    df["NombreCompleto"]
    .apply(lambda x: pd.Series(separarNombresApellidoZ(x)))
)

df["Fecha"] = pd.to_datetime(
    df["Fecha"],
    errors="coerce"
).dt.strftime("%d_%m_%Y")

df.to_excel("archivo_final.xlsx", index=False)

print("El archivo 'archivo_final.xlsx' ha sido creado correctamente.")