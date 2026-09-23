import pandas as pd

df = pd.read_excel('nombresSepAradoZ.xlsx') 

# Se cambia el formato
df['Fecha'] = pd.to_datetime(df['Fecha']).dt.strftime('%d_%m_%Y')

df.to_excel('cAmbiaFechaz.xlsx', index=False)

print("Verificar el archivo 'cAmbiarFechaz.xlsx'.")