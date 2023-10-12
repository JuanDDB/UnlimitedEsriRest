import requests
import json
import csv
#Ingresa el link del query
service_url = "Ingresa/aqui/tu/url..https://xx.xxx.xxx/arcgis/rest/services/xxxx/xxxx/MapServer/0/query"
limite = 1000 #Limite identificado

off=0
rango= limite

#Ingresa parametros adicionales, por defecto retornará tdos los campos
params = {
    "where": "1=1",
    "outFields": "*",
    "f": "json",
}

all_records = []

while True:
    params["resultOffset"] = limite
    params ["resultRecordCount"] = rango
    response = requests.get(service_url, params=params)
    data = response.json()

    off += 1000

    if "features" in data:
        records = data["features"]
        if not records:
            # Si no hay más registros, sal del ciclo
            break
        all_records.extend(records)

json_file = "/content/drive/MyDrive/Colab Notebooks/Datos/data.json"

with open(json_file, "w") as json_output:
    json.dump(all_records, json_output)

csv_file = "/content/drive/MyDrive/Colab Notebooks/Datos/data.csv"

field_names = all_records[0]["attributes"].keys()

with open(csv_file, "w", newline="") as csv_output:
    writer = csv.DictWriter(csv_output, fieldnames=field_names)
    writer.writeheader()
    for record in all_records:
        writer.writerow(record["attributes"])

print(f"Los datos se han guardado en {json_file} y {csv_file}.")
