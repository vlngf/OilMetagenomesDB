import pandas as pd
import json
def tsv_to_json():
  df = pd.read_table('https://github.com/agni-bioinformatics-lab/OilMetagenomesDB/blob/main/crude_oil/samples/crude_oil_samples.tsv')
  columns = df.columns.values.tolist()
  converters = [str, int, str, str, float, float, str, str, str, float, str, float, str, str, str, float, str, str, str]
  rows = [[fxn(x) for x, fxn in zip(row, converters)] for i, row in df[columns].iterrows()]
  datatables_format = {'data': rows}
  with open('OilMetagenomesDB/crude_oil/samples/crude_oil_samples.json', 'w') as write_file:
    json.dump(datatables_format, write_file, indent=2)

if __name__ == '__main__':
  tsv_to_json()
