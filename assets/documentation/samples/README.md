# OilMetagenomesDB - Samples Column Specifications

This page describes columns definitions for all sample-level lists. 

Sample columns are as follows:

| Feature | Description | Example | Possible values | Type, pattern, enum |
| :---: | :---: | :---: | :---: | :---: |
| project_name | Name of the project, <br> AuthorYear format | Zilov2023 | Unique to the article | "type": "string", <br> "pattern": "\^[A-Z][a-z]+\\\d{4}$" |
| publication_year | Year of publication, <br> YYYY format | 2023 | Unique to the article | "type": "string", <br> "pattern": "^(19[0-9]{2}\|20[0-2][0-9]\|2023)$" |
| publication_doi | Doi articles | 10.1007/s00253-018-8766-2 | Unique to the article | "type": "string", <br> "pattern": "^10\\\\.\\\d{4,9}\\\\/[^,]+$" |
| oil_reservoir | The name of the oil field should be written in the article or found by coordinates | romashkinskoe | Unique to the article | "type": "string", <br> "pattern": "^([^A-Z]*\|None)$" |
| oil_wells | The ID of the well in the article | A1 | Unique to the article | "type": "string", <br> "pattern": "^([^A-Z]*\|None)$" |
| latitude | The latitude at which the sample was taken | 1000.0 | Unique to the article | "type": "string", <br> "pattern": "^(\\\d+\\\\.\\\d+\|None)$" |
| longitude | The longitude at which the sample was taken | 1000.0 | Unique to the article | "type": "string", <br> "pattern": "^(\\\d+\\\\.\\\d+\|None)$" |
| geo_loc_name | The country where the well/field is located, from where samples were taken for analysis | usa | Registered in enum | [enum](https://github.com/agni-bioinformatics-lab/OilMetagenomesDB/blob/main/schemas_samples/geo_loc_name.json) |
| study_primary_focus | The focus of the research in the article | ecology | Registered in enum | [enum](https://github.com/agni-bioinformatics-lab/OilMetagenomesDB/blob/main/schemas_samples/study_primary_focus.json) |
| study_process | The biochemical process that is studied in the article | bioremediation | Registered in enum | [enum](https://github.com/agni-bioinformatics-lab/OilMetagenomesDB/blob/main/schemas_samples/study_process.json) |
| depth | Sampling depth in meters | 1000.0 | Unique to the article | "type": "string", <br> "pattern": "^(\\\d+\\\\.\\\d+\|None)$" |
| temp | Temperature in Celsius | 100.0 | Unique to the article | "type": "string", <br> "pattern": "^(\\\d+\\\\.\\\d+\|None)$" |
| pH | Sample acidity | 10.0 | Unique to the article | "type": "string", <br> "pattern": "^(\\\d+\\\\.\\\d+\|None)$" |
| salinity | Specify in ppt, if 10% is specified, write 100; <br> 1 ppt = 1000 mg/l | 0.5 | Unique to the article | "type": "string", <br> "pattern": "^(\\\d+\\\\.\\\d+\|None)$" |
| API | Specify in API units. <br> For example: 0.932 g/cm3 = 932 kg/m3 =20 API | 20 | Unique to the article | "type": "string", <br> "pattern": "^(\\\d+\|None)$" |
| NO3- | We specify in mg/l | 5.0 | Unique to the article | "type": "string", <br> "pattern": "^(\\\d+\\\\.\\\d+\|None)$" |
| PO43- | We specify in mg/l | 5.0 | Unique to the article | "type": "string", <br> "pattern": "^(\\\d+\\\\.\\\d+\|None)$" |
| SO42- | We specify in mg/l | 5.0 | Unique to the article | "type": "string", <br> "pattern": "^(\\\d+\\\\.\\\d+\|None)$" |
| Ca2+ | We specify in mg/l | 5.0 | Unique to the article | "type": "string", <br> "pattern": "^(\\\d+\\\\.\\\d+\|None)$" |
| Mg2+ | We specify in mg/l | 5.0 | Unique to the article | "type": "string", <br> "pattern": "^(\\\d+\\\\.\\\d+\|None)$" |
| Na+ | We specify in mg/l | 5.0 | Unique to the article | "type": "string", <br> "pattern": "^(\\\d+\\\\.\\\d+\|None)$" |
| K+ | We specify in mg/l | 5.0 | Unique to the article | "type": "string", <br> "pattern": "^(\\\d+\\\\.\\\d+\|None)$" |
| Cl- | We specify in mg/l | 5.0 | Unique to the article | "type": "string", <br> "pattern": "^(\\\d+\\\\.\\\d+\|None)$" |
| HCO3- | We specify in mg/l | 5.0 | Unique to the article | "type": "string", <br> "pattern": "^(\\\d+\\\\.\\\d+\|None)$" |
| acetate | We specify in mg/l | 5.0 | Unique to the article | "type": "string", <br> "pattern": "^(\\\d+\\\\.\\\d+\|None)$" |
| sample_name | What kind of ID was used by the study for this sample. <br> We take it from the article. If not in the article, we take it from NCBI | a1 | Unique to the article | "type": "string", <br> "pattern": "\^[^A-Z]*$" |
| feature | Description of the medium from which the sample was obtained | reservoir | Registered in enum | [enum](https://github.com/agni-bioinformatics-lab/OilMetagenomesDB/blob/main/schemas_samples/feature.json) |
| material | The type of sample from which bacterial dna was isolated | oil field production water | Registered in enum | [enum](https://github.com/agni-bioinformatics-lab/OilMetagenomesDB/blob/main/schemas_samples/material.json) |
| collection_date | Date of sample collection | 2020 | Unique to the article | "type": "string", <br> "pattern": "^(\\\d+\|None)$" |
| archive | The archive where the library data is stored | sra | Registered in enum | [enum](https://github.com/agni-bioinformatics-lab/OilMetagenomesDB/blob/main/schemas_samples/archive.json) |
| archive_project | Project code with all sample data (PRJ). The article may specify the code of a set of experiments (SRP), experiment code (SRX), sample code (SRS). <br> Through these designations in NCBI, you can find the project code | prjna604781 | Unique to the article | "type": "string", <br> "pattern": "^(prj\|srp\|srx\|srs)[a-z]*\\\d+$" |
| archive_accession | Data code for sample, <br> starts SRS for SRA or ERS for ENA | srs5536770 | Unique globally | "type": "string", <br> "pattern": "^(srs\|ers)\\\d+$" |