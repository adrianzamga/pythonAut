import pandas as pd
import unidecode

df = pd.read_excel("Creative.xlsx")
# Limpiar los nombres de columnas
df.columns = [unidecode.unidecode(str(col)).strip().lower() for col in df.columns]

# Imprimir columnas limpias
print("Columnas detectadas:")
for col in df.columns:
    print(f" - {col}")
