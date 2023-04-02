import csv
import json

# Открываем TSV-файл для чтения
with open('enviromental_samples.tsv', 'r') as tsvfile:
    reader = csv.DictReader(tsvfile, delimiter='\t')
    # Преобразуем данные в список словарей, приводя значения полей к нужным типам данных
    rows = [
        {
            "project_name": str(row["project_name"]) if row["project_name"] != "None" else None,
            "publication_year": int(row["publication_year"]) if row["publication_year"] != "None" else None,
            "publication_doi": str(row["publication_doi"]) if row["publication_doi"] != "None" else None,
            "site_name": str(row["site_name"]) if row["site_name"] != "None" else None,
            "latitude": float(row["latitude"].replace(",", ".")) if isinstance(row["latitude"], str) and row["latitude"].replace(".", "", 1).isdigit() else None,
            "longitude": float(row["longitude"].replace(",", ".")) if isinstance(row["longitude"], str) and row["longitude"].replace(".", "", 1).isdigit() else None,
            "geo_loc_name": str(row["geo_loc_name"]) if row["geo_loc_name"] != "None" else None,
            "study_primary_focus": str(row["study_primary_focus"]) if row["study_primary_focus"] != "None" else None,
            "depth": float(row["depth"].replace(",", ".")) if isinstance(row["depth"], str) and row["depth"].replace(".", "", 1).isdigit() else None,
            "temp": float(row["temp"].replace(",", ".")) if isinstance(row["temp"], str) and row["temp"].replace(".", "", 1).isdigit() else None,
            "pH": float(row["pH"].replace(",", ".")) if isinstance(row["pH"], str) and row["pH"].replace(".", "", 1).isdigit() else None,
            "salinity": float(row["salinity"].replace(",", ".")) if isinstance(row["salinity"], str) and row["salinity"].replace(".", "", 1).isdigit() else None,
            "NO3-": float(row["NO3-"].replace(",", ".")) if isinstance(row["NO3-"], str) and row["NO3-"].replace(".", "", 1).isdigit() else None,
            "PO43-": float(row["PO43-"].replace(",", ".")) if isinstance(row["PO43-"], str) and row["PO43-"].replace(".", "", 1).isdigit() else None,
            "SO42-": float(row["SO42-"].replace(",", ".")) if isinstance(row["SO42-"], str) and row["SO42-"].replace(".", "", 1).isdigit() else None,
            "Ca2+": float(row["Ca2+"].replace(",", ".")) if isinstance(row["Ca2+"], str) and row["Ca2+"].replace(".", "", 1).isdigit() else None,
            "Mg2+": float(row["Mg2+"].replace(",", ".")) if isinstance(row["Mg2+"], str) and row["Mg2+"].replace(".", "", 1).isdigit() else None,
            "sample_name": str(row["sample_name"]) if row["sample_name"] != "None" else None,
            "feature": str(row["feature"]) if row["feature"] != "None" else None,
            "material": str(row["material"]) if row["material"] != "None" else None,
            "sampling_date": int(row["sampling_date"]) if row["sampling_date"] != "None" else None,
            "archive": str(row["archive"]) if row["archive"] != "None" else None,
            "archive_project": str(row["archive_project"]) if row["archive_project"] != "None" else None,
            "archive_accession": str(row["archive_accession"]) if row["archive_accession"] != "None" else None
        }
        for row in reader
    ]

# Открываем JSON-файл для записи
with open('enviromental_samples.json', 'w') as jsonfile:
    # Записываем данные в формате JSON
    json.dump(rows, jsonfile, indent=4, ensure_ascii=False)
