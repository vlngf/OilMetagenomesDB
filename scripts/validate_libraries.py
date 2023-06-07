# validate_libraries.py
import pandas as pd
import json
from jsonschema import validate, Draft7Validator

def validate_libraries():
    # Load the data
    df = pd.read_csv('assets/commons/common_libraries.tsv', sep='\t')

    # Load the schema
    with open('assets/commons/common_libraries.json') as f:
        schema = json.load(f)

    # Convert the data to a list of dictionaries
    data = df.to_dict(orient='records')

    # Validate each record
    v = Draft7Validator(schema)
    errors = sorted(v.iter_errors(data), key=lambda e: e.path)
    for error in errors:
        print(error.message)

    assert not errors, "The common_libraries.tsv file does not match the schema"
    
    print("Validation of common_libraries.tsv against the schema was successful.")
    
if __name__ == "__main__":
    validate_libraries()
