import pandas as pd

# se lee empezando desde la fila 2 y seleccionando solo la columna B
df1 = pd.read_excel('.xlsx', usecols="B", skiprows=1) 
df2 = pd.read_excel('.xlsx', usecols="B", skiprows=1)


df1.columns = ['Matricula']
df2.columns = ['Matricula']

# Si hay valores nulos se eliminan
matriculas1 = df1['Matricula'].dropna()
matriculas2 = df2['Matricula'].dropna()

set1 = set(matriculas1)
set2 = set(matriculas2)

matriculas_en_ambos = list(set1.intersection(set2))

solo_en_archivo1 = list(set1.difference(set2))

solo_en_archivo2 = list(set2.difference(set1))

max_length = max(len(matriculas_en_ambos), len(solo_en_archivo1), len(solo_en_archivo2))

matriculas_en_ambos.extend([None] * (max_length - len(matriculas_en_ambos)))
solo_en_archivo1.extend([None] * (max_length - len(solo_en_archivo1)))
solo_en_archivo2.extend([None] * (max_length - len(solo_en_archivo2)))

resultados = pd.DataFrame({
    'Matriculas en ambos archivos': matriculas_en_ambos,
    'Solo en archivo 1'
    : solo_en_archivo1,
    'Solo en archivo 2': solo_en_archivo2
})

resultados.to_excel('resultados_comparacion.xlsx', index=False)

print("¡Comparación completada! Revisa el archivo 'resultados_comparacion.xlsx'.")