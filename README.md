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
Этот список содержит информацию о метагеноме сырой нефти и метагенома окружающей среды в месторождениях нефти. Здесь можно найти название публикаций, годы публикаций, DOI, тип образцов, географическое местоположение взятия образца, сопутствующие условия. 

## Usage
Чтобы загрузить последнюю стабильную версию списка примеров OilMetagenomeBD и добавить данные, необходимо выполнить следующие шаги:
1. Перейти в репозиторий OilMetagenomeBD;
2. Скопировать SSH ключ во вкладке "<> Code";
3. Основные команды для командной строки:
* git - check if Git installed
* git clone <link> - cloning repo on your computer
* git status - check the changes
* git commit -m "add script.py with greeting" - save change in repository (-m is some message of what you’ve done)
* git status - check that commit is created 
* git push - update the GitHub repository
## Samples Column Specifications
123
## Libraries Column Specifications
The libraries tables store information about each specific reed from the library - id_ in databases, sequencing type (paired-end, single-end), sequencing strategy (WGS, RNA-Seq, amplicon), links to downloads and publications, etc.

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

Library columns are as follows:
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
