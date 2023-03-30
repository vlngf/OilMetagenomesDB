import csv
import json

# Открываем TSV-файл для чтения
with open('crude_oil_samples.tsv', 'r') as tsvfile:
    reader = csv.DictReader(tsvfile, delimiter='\t')
    # Преобразуем данные в список словарей, приводя значения полей к нужным типам данных
    rows = [
        {
            "project_name": str(row["project_name"]) if row["project_name"] != "None",
            "publication_year": int(row["publication_year"]) if row["publication_year"] != "None",
            "publication_doi": str(row["publication_doi"]) if row["publication_doi"] != "None",
            "site_name": str(row["site_name"]) if row["site_name"] != "None",
            "latitude": float(row["latitude"].replace(",", ".")) if isinstance(row["latitude"], str) and row["latitude"].replace(".", "", 1).isdigit(),
            "longitude": float(row["longitude"].replace(",", ".")) if isinstance(row["longitude"], str) and row["longitude"].replace(".", "", 1).isdigit(),
            "geo_loc_name": str(row["geo_loc_name"]) if row["geo_loc_name"] != "None",
            "study_primary_focus": str(row["study_primary_focus"]) if row["study_primary_focus"] != "None",
            "sequence_name": str(row["sequence_name"]) if row["sequence_name"] != "None",
            "depth": float(row["depth"].replace(",", ".")) if isinstance(row["depth"], str) and row["depth"].replace(".", "", 1).isdigit(),
            "sample_name": str(row["sample_name"]) if row["sample_name"] != "None",
            "sample_age": int(row["sample_age"]) if row["sample_age"] != "None",
            "sample_age_doi": str(row["sample_age_doi"]) if row["sample_age_doi"] != "None",
            "feature": str(row["feature"]) if row["feature"] != "None",
            "material": str(row["material"]) if row["material"] != "None",
            "sampling_date": int(row["sampling_date"]) if row["sampling_date"] != "None",
            "archive": str(row["archive"]) if row["archive"] != "None",
            "archive_project": str(row["archive_project"]) if row["archive_project"] != "None",
            "archive_accession": str(row["archive_accession"]) if row["archive_accession"] != "None"
        }
        for row in reader
    ]

# Открываем JSON-файл для записи
with open('crude_oil_samples.json', 'w') as jsonfile:
    # Записываем данные в формате JSON
    json.dump(rows, jsonfile, indent=4, ensure_ascii=False)
    
# Open and read the JSON file
with open('crude_oil_samples.json', 'r') as jsonfile:
    # Load the JSON data as a dictionary object
    data = json.loads(jsonfile.read())

# Create a set of all values in the "archive_accession" column
all_accessions = set()
for item in data:
    archive_accession = item['archive_accession']
    if archive_accession:
        accession_list = [value.strip() for value in archive_accession.split(',') if value.strip()]
        all_accessions.update(accession_list)

# Check if the number of unique values in the set is equal to the total number of values in the "archive_accession" column
if len(all_accessions) != sum(1 for item in data if item['archive_accession']):
    print('Error: Duplicate values found in "archive_accession"')
    exit(1)
else:
    print('All archive_accession are unique')
