
import pandas as pd

archivo = ".xlsx"
df = pd.read_excel(archivo)

df["Fecha"] = pd.to_datetime(
    df["Fecha"],
    format="%d.%m.%Y",
    errors="coerce"
)

conceptos = [
    "HSP",
    "CON",
    "CO20",
    "C5",
    "C3H",
    "C0",
    "CU",
    "C",
    "COLT",
    "CWU",
    "IN",
    "SM",
    "CDS",
    "COREU",
    "CWQ3"             
]

mask = df["Concepto"].isin(conceptos)

df["FechaMin"] = df.groupby(["Matricula", "Concepto"])["Fecha"].transform("min")

df["EsPrimerPagoConcepto"] = ""

es_primer_pago = mask & (df["Fecha"] == df["FechaMin"])

df.loc[es_primer_pago, "EsPrimerPagoConcepto"] = (
    "SI, " + df.loc[es_primer_pago, "Fecha"].dt.strftime("%d.%m.%Y")
)

df.drop(columns=["FechaMin"], inplace=True)

df.to_excel(archivo, index=False)

print("Archivo actualizado correctamente")