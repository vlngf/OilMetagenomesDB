<p align="center">
  <img src="image\git_img_top.png" width="250" height="100" />
</p>
<h2 align="center">Community curated database of oil metagenomes</h2>

<div align="center">
  
  ![check_dataset paasing](https://img.shields.io/badge/check__dataset-passing-brightgreen)
  ![Latest Release](https://img.shields.io/badge/Latest__Release-v0.1-orange)
  
</div>
 
:octocat: Community curated database of the metagenome of oil and oil fields🛢️🦠

+ [Description](https://github.com/agni-bioinformatics-lab/OilMetagenomesDB/blob/main/README.md#description)
+ [Usage](https://github.com/agni-bioinformatics-lab/OilMetagenomesDB/blob/main/README.md#usage)
+ [Samples Column Specifications](https://github.com/agni-bioinformatics-lab/OilMetagenomesDB/blob/main/README.md#samples-column-specifications)
+ [Libraries Column Specifications](https://github.com/agni-bioinformatics-lab/OilMetagenomesDB/blob/main/README.md#libraries-column-specifications)
+ [Contributing](https://github.com/agni-bioinformatics-lab/OilMetagenomesDB/blob/main/README.md#contributing)
  + [Contributing your own Publications](https://github.com/agni-bioinformatics-lab/OilMetagenomesDB/blob/main/README.md#contributing-your-own-publications)
  + [Contributing previously published publications](https://github.com/agni-bioinformatics-lab/OilMetagenomesDB/blob/main/README.md#contributing-previously-published-publications)
  + [Guidelines and Conventions](https://github.com/agni-bioinformatics-lab/OilMetagenomesDB/blob/main/README.md#guidelines-and-conventions)
  
## Description
This list contains information on crude oil metagenome and environmental metagenome in oil fields. Here you can find the name of publications, years of publications, DOI, type of samples, geographic location of sample collection, and associated conditions.

## Usage
Чтобы загрузить последнюю стабильную версию списка примеров OilMetagenomeBD и добавить данные, необходимо выполнить следующие шаги:
1. Перейти в репозиторий OilMetagenomeBD;
2. Скопировать SSH ключ во вкладке "<> Code";
3. Скачать с помощью командной строки директорию;
4. Перейдите в интересующий список образцов и дополните файл .tsv в программе для работы с электронными таблицами (например, LibreOffice Calc, Microsoft Excel) или на выбранном вами языке программирования (например, R);

Основные команды для командной строки:
* `git` - check if Git installed
* `git clone` <link> - cloning repo on your computer
* `git status` - check the changes
* `git commit -m "add script.py with greeting"` - save change in repository (-m is some message of what you’ve done)
* `git status` - check that commit is created 
* `git push` - update the GitHub repository
 
## Samples Column Specifications
The SAMPLE tables stores information about the sample, its type, date of collection, geographic coordinates, depth of sample extraction, etc.

- 🏞: oilfield environmental metagenomes
- 🦠: crude oil metagenomes

Numeric fields (e.g. latitude), can be filled with `NA` to indicate 'no
reported value'. Free text fields (e.g. `geo_loc_name`) can be indicated with
`Unknown`, and restricted category columns sometimes will have an `unknown`
option.

All column with 'defined categories' should be validated against
`assets/enums/<column>.json`. This is to ensure data consistency, e.g. all
Dental calculus samples are listed as `dental calculus` (as defined in
`assets/enums/<column>.json`). This is to ensure data consistency.

If you wish to a new category, please consult with the [agni-bioinformatics-lab](https://github.com/agni-bioinformatics-lab), and then add it to `assets/enums/<column>.json`.

Sample columns are as follows ([documentation](https://github.com/agni-bioinformatics-lab/OilMetagenomesDB/tree/main/documentation/samples)):
* project name
* publication year
* data publication doi
* sample name
* latitude
* longitude
* geo loc name
* study  primary focus
* sequence  name
* depth
* sample name
* feature
* material
* sampling date
* archive
* archive project
* archive accession

## Libraries Column Specifications
  The LIBRARIES tables store information about each specific reed from the library - id_ in databases, sequencing type (paired-end, single-end), sequencing strategy (WGS, RNA-Seq, amplicon), links to downloads and publications, etc.

- 🏞: oilfield environmental metagenomes
- 🦠: crude oil metagenomes

Numeric fields (e.g. `read_count`), can be filled with `NA` to indicate 'no
reported value'. Free text fields (e.g. `library_name`) can be indicated with
`Unknown`, and restricted category columns sometimes will have an `unknown`
option.

All column with 'defined categories' should be validated against
`assets/enums/<column>.json`. This is to ensure data consistency. E.g., all
libraries sequenced on Illumina NextSeq 500s are listed as `NextSeq 500` (as
defined in `assets/enums/instrument_models.json`). This is to ensure data
consistency.

If you wish to a new category, please make a separate pull-request with your
modification in the corresponding `assets/enums/<column>.json` file.

Library columns are as follows ([documentation](https://github.com/agni-bioinformatics-lab/OilMetagenomesDB/tree/main/documentation/libraries)):
* project name
* publication year
* data publication doi
* sample name
* archive
* archive project
* archive sample accession
* library name
* strand type
* library polymerase
* library treatment
* library concentration
* instrument model
* library layout
* library strategy
* amplicon variable region
* read count
* archive data accession
* download links
* download md5s
* download sizes

## Contributing
123
### Contributing your own Publications
123
### Contributing previously published publications
123
### Guidelines and Conventions
123
