import pandas as pd

# Leer archivos en Excel
az1 = pd.read_excel(
    'C:/xampp/htdocs/Python - copia/pupils.xlsx',
    usecols="A"
)

az2 = pd.read_excel(
    'C:/xampp/htdocs/Python - copia/ZA.xlsx',
    usecols="A"
)

# Renombrar columnas
az1.columns = ['Id']
az2.columns = ['Matricula']

# Eliminar valores nulos
az1 = az1.dropna(subset=['Id']).reset_index(drop=True)
az2 = az2.dropna(subset=['Matricula']).reset_index(drop=True)

# Crear número de fila (empezando en 1)
az1['Fila1'] = az1.index + 1
az2['Fila2'] = az2.index + 1

# Comparar las matrículas
resultado = pd.merge(
    az1,
    az2,
    left_on='Id',
    right_on='Matricula',
    how='outer'
)

# Indicar si están en la misma fila
resultado['Misma_fila'] = (
    resultado['Fila1'] == resultado['Fila2']
)

# Ordenar por matrícula
resultado = resultado.sort_values(
    by='Id',
    na_position='last'
)

# Exportar
resultado.to_excel(
    'resultadosAZ.xlsx',
    index=False
)

print("Revisar archivo 'resultadosAZ.xlsx'.")
