# OilMetagenomesDB - Libraries Column Specifications

This page describes columns definitions for all library-level lists.

Library columns are as follows:

| Feature | Description | Example | Possible values | Type, pattern, enum |
| :---: | :---: | :---: | :---: | :---: |
| project_name | Name of the project, <br> AuthorYear format | Zilov2023 | article_common | "type": "string", <br> "pattern": "\^[A-Z][a-z]+\\\d{4}$" |
| publication_year | Year of publication, <br> YYYY format | 2023 | article_common | "type": "string", <br> "pattern": "^(19[0-9]{2}\|20[0-2][0-9]\|2023)$" |
| publication_doi | DOI of the articles | 10.1007/s00253-018-8766-2 | article_common | "type": "string", <br> "pattern": "^10\\\\.\\\d{4,9}\\\\/[^,]+$" |
| sample_name | What kind of ID was used by the study for this sample. <br> We take it from the article. If not in the article, we take it from NCBI | A1 | article_uniq | "type": "string", <br> "pattern": "^.+$" |
| archive | The archive where the library data is stored | SRA | article_common | Specified in an enum <br> [(link)](https://github.com/agni-bioinformatics-lab/OilMetagenomesDB/blob/main/schemas_libraries/archive.json) |
| archive_project | Project code with all sample data (PRJ). The article may specify the code of a set of experiments (SRP), experiment code (SRX), sample code (SRS). <br> Through these designations in NCBI, you can find the project code | PRJNA604781 | article_common | "type": "string", <br> "pattern": "^(PRJ\|SRP\|SRX\|SRS)[A-Z]*\\\d+$" |
| archive_accession | Data code for sample, <br> starts SRS for SRA or ERS for ENA | SRS5536770 | db_uniq | "type": "string", <br> "pattern": "^(SRS\|ERS)\\\d+$" |
| library_name | Laboratory name of the sequenced library | 16s5_samples_set | article_uniq | "type": "string", <br> "pattern": "^.+$" |
| strand_type | The type of library prepared for sequencing. <br> Must be specified in the kit instructions for sample preparation - LINK | double | db_common | Specified in an enum <br> [(link)](https://github.com/agni-bioinformatics-lab/OilMetagenomesDB/blob/main/schemas_libraries/strand_type.json) |
| library_polymerase | Specify the polymerases that were applied after indexing the library - write the source, if we take it not from the article. - can be in the amplification kit | fastpfu polymerase | db_common | "type": "string", <br> "pattern": "^([^A-Z]*\|None\|unknown)$" |
| library_treatment | The type of library processing to repair the damage. <br> Indicated in the article | user | db_common | Specified in an enum <br> [(link)](https://github.com/agni-bioinformatics-lab/OilMetagenomesDB/blob/main/schemas_libraries/library_treatment.json) |
| library_concentration | This is the number of copies of qPCR per mkl of the extract of this library. <br> If the library has been sequenced several times, then you can duplicate the value for each library. Is it a nanogram per microliter or a copy per microliter | 41700000.1 | db_common | "type": "string", <br> "pattern": "^(\\\d+\\\\.\\\d+\|None\|unknown)$" |
| PCR_cycle_count | Number of PCR cycles | 25 | db_common | "type": "string", <br> "pattern": "^(\\\d+\|None\|unknown)$" |
| instrument_model | Sequencer model. <br> Specified in the article | illumina hiseq4000 | db_common | Specified in an enum <br> [(link)](https://github.com/agni-bioinformatics-lab/OilMetagenomesDB/blob/main/schemas_libraries/instrument_model.json) |
| library_layout | The sequencing method (one-sided or two-sided) can be understood by the number of FASTQ files (1 or 2, respectively) | paired | article_common | Specified in an enum <br> [(link)](https://github.com/agni-bioinformatics-lab/OilMetagenomesDB/blob/main/schemas_libraries/library_layout.json) |
| library_strategy | Research strategy | amplicon | db_common | Specified in an enum <br> [(link)](https://github.com/agni-bioinformatics-lab/OilMetagenomesDB/blob/main/schemas_libraries/library_strategy.json) |
| amplicon_variable_region | Variable regions of the 16S rRNA gene, which are used to identify taxa of bacteria and archaea. <br> Specified in the article | v3-v4 | db_common | "type": "string", <br> pattern": "^(None\|unknown\|(v[1-9]\|v1-v2\|v2-v3\|v3-v4\|v4-v5\|v5-v6\|v6-v7\|v7-v8\|v8-v9\|v1-v3\|v6-v8)(, ?(v[1-9]\|v1-v2\|v2-v3\|v3-v4\|v4-v5\|v5-v6\|v6-v7\|v7-v8\|v8-v9\|v1-v3\|v6-v8))*)$" |
| read_count | How many reads are in the FASTQ files. <br> Finds the parser | 215326 | article_uniq | "type": "string", <br> "pattern": "^(\\\d+)$" |
| archive_data_accession | The result of the SRR experiment | SRR7754480 | db_uniq | "type": "string", <br> "pattern": "^(SRR)\\\d+" |
| download_links | A link to download each raw data file. <br> Finds the parser | https&#58;//sra-pub-run- <br> odp.s3.amazonaws.com/ <br> sra/SRR7754480/SRR7754480 | article_uniq | "type": "string", <br> "pattern": "^(http\|ftp)" |
| download_md5s | MD5 checksums of the corresponding uploaded files. <br> This allows you to verify the data integrity of uploaded files by comparing the checksum of your file with the checksum on the server from which they were downloaded. <br> Finds the parser | 5f574505fa16b7ae <br> 01a46682f8f24c87 | article_uniq | "type": "string", <br> "pattern": "^\[a-zA-Z0-9]{32}$" |
| download_sizes | The sizes of the corresponding uploaded files in bytes. <br> This can be used to estimate the hard disk space that will be used after booting. For paired readings, it can be separated by a semicolon. Finds the parser | 71368888 | db_common | "type": "string", <br> "pattern": "^(\\\d+)$" |