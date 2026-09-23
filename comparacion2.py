import pandas as pd

comparaciones = {
    'colsep': 'colsep.xlsx',
    'coloct': 'coloct.xlsx',
    'colnov': 'colnov.xlsx',
    'coldic': 'coldic.xlsx',
    'colene': 'colene.xlsx',
    'colfeb': 'colfeb.xlsx',
    'colmar': 'colmar.xlsx',
    'colabr': 'colabr.xlsx',
    'colmay': 'colmay.xlsx',
    'coljun': 'coljun.xlsx'
}

df_creative = pd.read_excel(".xlsx", header=0, dtype=str)

print("Filas en creative.xlsx:", df_creative.columns.tolist())

df_creative.columns = df_creative.columns.str.strip().str.lower()  # Normaliza

df_debug = pd.read_excel("Creative.xlsx", header=None)

print("No procesados (primeras 5 filas):")
print(df_debug.head())

with pd.ExcelWriter("comparacion_matriculas.xlsx") as escritor:

    for mes, archivo in comparaciones.items():

        if mes not in df_creative.columns:
            print(f"Columna '{mes}' no encontrada. Se omite.")
            continue

        try:
            df_colpri = pd.read_excel(archivo, dtype=str)

            columna_matricula = next(
                (columna for columna in df_colpri.columns
                 if 'matricula' in columna.lower()),
                None
            )

            if not columna_matricula:
                print(f"Columna 'Matrícula' no encontrada en {archivo}. Se omite.")
                continue

            ids_creative = df_creative[mes].dropna().astype(str)
            ids_colpri = df_colpri[columna_matricula].dropna().astype(str)

            df_comparacion = pd.merge(
                left=pd.DataFrame({'Id_Creative': ids_creative}),
                right=pd.DataFrame({'Id_Colpri': ids_colpri}),
                left_on='Id_Creative',
                right_on='Id_Colpri',
                how='outer',
                indicator='Coincide'
            )

            df_comparacion['Coincide'] = (
                df_comparacion['Coincide'] == 'both'
            )

            df_comparacion.to_excel(
                escritor,
                sheet_name=mes,
                index=False
            )

            print(f"Comparación completada: {mes}")

        except FileNotFoundError:
            print(f"Archivo {archivo} no encontrado. Se omite.")