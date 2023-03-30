import csv
import json
    
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
