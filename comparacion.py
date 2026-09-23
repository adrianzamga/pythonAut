import pandas as pd

az1 = pd.read_excel('C:/xampp/htdocs/Python - copia/pupils.xlsx', usecols="A") # S
az2 = pd.read_excel('C:/xampp/htdocs/Python - copia/ZA.xlsx', usecols="A") # C

az1.columns = ['Id']
az2.columns = ['Matricula']

matriculas1 = az1['Id'].dropna()
matriculas2 = az2['Matricula'].dropna()

set1 = set(matriculas1)  # S
set2 = set(matriculas2)  # C

matriculasEnAmbos = list(set1.intersection(set2))   # En ambos
soloEnS = list(set1.difference(set2))           # Solo en s
soloEnC = list(set2.difference(set1))        # Solo en c

max_length = max(len(matriculasEnAmbos), len(soloEnS), len(soloEnC))
matriculasEnAmbos.extend([None] * (max_length - len(matriculasEnAmbos)))
soloEnS.extend([None] * (max_length - len(soloEnS)))
soloEnC.extend([None] * (max_length - len(soloEnC)))

resultados = pd.DataFrame({
    'Matriculas en ambos archivos': matriculasEnAmbos,
    'Solo en S': soloEnS,
    'Solo en Creative': soloEnC
})

resultados.to_excel('resultadosAZ.xlsx', index=False)
print("Revisar archivo 'resultadosAZ.xlsx'.")
