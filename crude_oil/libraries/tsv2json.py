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
            "data_publication_doi": str(row["publication_doi"]) if row["publication_doi"] != "None" else None,
            "sample_name": str(row["sample_name"]) if row["sample_name"] != "None" else None,
            "archive": str(row["archive"]) if row["archive"] != "None" else None,
            "archive_project": str(row["archive_project"]) if row["archive_project"] != "None" else None,
            "archive_sample_accession": str(row["archive_sample_accession"]) if row["archive_sample_accession"] != "None" else None,
            "library_name": str(row["library_name"]) if row["library_name"] != "None" else None,
            "strand_type": str(row["strand_type"]) if row["strand_type"] != "None" else None,
            "library_polymerase": str(row["library_polymerase"]) if row["library_polymerase"] != "None" else None,
            "library_treatment": str(row["library_treatment"]) if row["library_treatment"] != "None" else None,
            "library_concentration": str(row["library_concentration"]) if row["library_concentration"] != "None" else None,
            "instrument_model": str(row["instrument_model"]) if row["instrument_model"] != "None" else None,
            "library_layout": str(row["library_layout"]) if row["library_layout"] != "None" else None,
            "library_strategy": str(row["library_strategy"]) if row["library_strategy"] != "None" else None,
            "amplicon_variable_region": str(row["amplicon_variable_region"]) if row["amplicon_variable_region"] != "None" else None,
            "read_count": int(row["read_count"]) if row["read_count"] != "None" else None,
            "archive_data_accession": str(row["archive_data_accession"]) if row["archive_data_accession"] != "None" else None,
            "download_links": str(row["download_links"]) if row["download_links"] != "None" else None,
            "download_md5s": str(row["download_md5s"]) if row["download_md5s"] != "None" else None,
            "download_sizes": int(row["download_sizes"]) if row["download_sizes"] != "None" else None,
        }
        for row in reader
    ]

# Открываем JSON-файл для записи
with open('enviromental_samples.json', 'w') as jsonfile:
    # Записываем данные в формате JSON
    json.dump(rows, jsonfile, indent=4, ensure_ascii=False)
