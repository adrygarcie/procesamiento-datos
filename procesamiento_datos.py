import pandas as pd

url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/latest/owid-covid-latest.csv"
datos = pd.read_csv(url)
datos_procesados = datos[['location', 'total_cases', 'total_deaths', 'population']].dropna()

datos_procesados.to_csv("datos_procesados.csv", index=False)

print("✅ Datos procesados y guardados en datos_procesados.csv")