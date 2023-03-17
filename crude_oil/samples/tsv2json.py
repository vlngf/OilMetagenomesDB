import csv
import json

# Открываем TSV-файл для чтения
with open('crude_oil_samples.tsv', 'r') as tsvfile:
    reader = csv.DictReader(tsvfile, delimiter='\t')
    # Преобразуем данные в список словарей, приводя значения полей к нужным типам данных
    rows = [
        {
            "project_name": row["project_name"],
            "publication_year": int(row["publication_year"]),
            "publication_doi": row["publication_doi"],
            "site_name": row["site_name"],
            "latitude": float(row["latitude"]),
            "longitude": float(row["longitude"]),
            "geo_loc_name": row["geo_loc_name"],
            "study_primary_focus": row["study_primary_focus"],
            "sequence_name": row["sequence_name"],
            "depth": float(row["depth"]),
            "sample_name": row["sample_name"],
            "sample_age": int(row["sample_age"]),
            "sample_age_doi": row["sample_age_doi"],
            "feature": row["feature"],
            "material": row["material"],
            "sampling_date": int(row["sampling_date"]),
            "archive": row["archive"],
            "archive_project": row["archive_project"],
            "archive_accession": row["archive_accession"]
        }
        for row in reader
    ]

# Открываем JSON-файл для записи
with open('crude_oil_samples.json', 'w') as jsonfile:
    # Записываем данные в формате JSON
    json.dump(rows, jsonfile, indent=4, ensure_ascii=False)
