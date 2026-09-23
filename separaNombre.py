import pandas as pd

# Bloque que separa nombres y apellidos
def separarNombresApellidoZ(nombreCompleto):
    partes = nombreCompleto.split()
    
    if len(partes) >= 3:
        apellido_paterno = partes[0]
        apellido_materno = partes[1]
        nombres = " ".join(partes[2:])
    elif len(partes) == 2:
        apellido_paterno = partes[0]
        apellido_materno = ""
        nombres = partes[1]
    elif len(partes) == 1:
        # Si no tiene apellido
        nombres = partes[0]
        apellido_paterno = ""
        apellido_materno = ""
    else:
        nombres = ""
        apellido_paterno = ""
        apellido_materno = ""

    return nombres, apellido_paterno, apellido_materno

df = pd.read_excel('archivo_limpio.xlsx')

print(df.columns)
df[['Nombres', 'ApellidoP', 'ApellidoM']] = df['NombreCompleto'].apply(lambda x: pd.Series(separarNombresApellidoZ(x)))

df.to_excel('nombresSepAradoZ.xlsx', index=False)

print("Se creo el archivo")