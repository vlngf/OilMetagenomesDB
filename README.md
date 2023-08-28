<p align="center">
  <img src="assets\image\git_img_top.png" width="250" height="100" />
</p>
<h2 align="center">Community curated database of oil metagenomes</h2>

<div align="center">
  
  [![github-watchers](https://img.shields.io/github/watchers/agni-bioinformatics-lab/OilMetagenomesDB?label=Watch&style=social&logo=github)](https://github.com/agni-bioinformatics-lab/OilMetagenomesDB)
  [![github-stars](https://img.shields.io/github/stars/agni-bioinformatics-lab/OilMetagenomesDB?style=social&logo=github)](https://github.com/agni-bioinformatics-lab/OilMetagenomesDB)
  [![github-license](https://img.shields.io/github/license/agni-bioinformatics-lab/OilMetagenomesDB?style=social&logo=github)](https://github.com/agni-bioinformatics-lab/OilMetagenomesDB)

</div>

<a name="top"></a>
Community :octocat: curated database of the metagenome of oil and oil fields🛢️🦠

+ [Description](#description)
+ [Usage](#usage)
+ [Samples Column Specifications](#samples-column-specifications)
+ [Libraries Column Specifications](#libraries-column-specifications)
+ [Contributing](#contributing)
  + [Some tips](#some-tips)
  
## Description
This list contains information on crude oil metagenome and environmental metagenome in oil fields. Here you can find the name of publications, years of publications, DOI, type of samples, geographic location of sample collection, and associated conditions.

## Usage
To download the latest stable version of the OilMetagenomeDB example list and add data, follow these steps:
1. Go to the OilMetagenomeDB repository;
2. Copy the SSH key in the "<> Code" tab;
3. Use the command line to download the directory;
4. Go to the sample list of interest and complete the .tsv file in your spreadsheet program (for example, LibreOffice Calc, Microsoft Excel) or in the programming language of your choice (for example, R);

Basic commands for the command line:
* `git` - check if Git installed
* `git clone` <link> - cloning repo on your computer
* `git status` - check the changes
* `git commit -m "add script.py with greeting"` - save change in repository (-m is some message of what you’ve done)
* `git status` - check that commit is created 
* `git push` - update the GitHub repository
 
If you find dataset validation errors or think of a new dataset validation, then write me @rakhmanovtr 

<span id="samples-column-specifications"></span>
## Samples Column Specifications [![Up](assets\image\git_img_up.png)](#top)


The SAMPLE tables stores information about the sample, its type, date of collection, geographic coordinates, depth of sample extraction, etc.

- 🏞: oilfield environmental metagenomes
- 🦠: crude oil metagenomes

Numeric and text fields must be filled in with `None` to indicate 'value not reported'.

All column with 'defined categories' should be validated against
`assets/enums/<column>.json`. This is to ensure data consistency, e.g. all

If you wish to a new category, please consult with the [agni-bioinformatics-lab](https://github.com/agni-bioinformatics-lab), and then add it to `assets/enums/<column>.json`.

Sample columns are as follows ([documentation](https://github.com/agni-bioinformatics-lab/OilMetagenomesDB/tree/main/assets/documentation/samples)):

<span id="libraries-column-specifications"></span>
## Libraries Column Specifications [![Up](assets\image\git_img_up.png)](#top)
  The LIBRARIES tables store information about each specific reed from the library - id_ in databases, sequencing type (paired-end, single-end), sequencing strategy (WGS, RNA-Seq, amplicon), links to downloads and publications, etc.

- 🏞: oilfield environmental metagenomes
- 🦠: crude oil metagenomes

Numeric and text fields must be filled in with `None` to indicate 'value not reported'.

All column with 'defined categories' should be validated against
`assets/enums/<column>.json`. This is to ensure data consistency. E.g., all
libraries sequenced on Illumina NextSeq 500s are listed as `NextSeq 500` (as
defined in `assets/enums/instrument_models.json`). This is to ensure data
consistency.

Library columns are as follows ([documentation](https://github.com/agni-bioinformatics-lab/OilMetagenomesDB/tree/main/assets/documentation/libraries)):

<span id="contributing"></span>
## Contributing [![Up](assets\image\git_img_up.png)](#top)
Samples added to the OilMetagenomeDB should come from published studies. Samples should also be available in publicly accessible databases (e.g., EBI ENA or NCBI SRA).

When filling in the data, each sample from the publication will get a new row. For guidance on what information to add to each column see the README.md for a handy guide.

<span id="some-tips"></span>
### Some tips [![Up](assets\image\git_img_up.png)](#top)
* Do not add spaces at the end of data entries, for example the "geo_loc_name" column is checked against a predetermined list of countries, so if you type “Netherlands ” rather than just “Netherlands” they’ll be an issue as it won’t match.
* To check the columns that must match a predefined list, see enums
* If latitude and longitude are not specified, if the publication has only a very approximate location (such as a region), then click in the center of that region and record the latitude and longitude to 2 decimal places only.
  * If only a country with no additional information is specified as a sample location, enter the coordinates of the middle of that particular country, but without the decimal places.
* Be sure to record the correct archive_accession. Check out the README.md. These normally should be ‘SRA sample’ IDs (i.e. ERS or SRS for the ENA and NCBI SRA respectively), however please ask the coreteam if you are in doubt or have a different archive. Careful: You may have multiple ERS/SRS codes per sample as some people upload each library as a different ‘sample’. If this is the case be sure to include all the sample accessions comma separated list: ERRXXXX,ERRXXXXX,ERRXXXX. Always go with the sample accession rather than the run accession.