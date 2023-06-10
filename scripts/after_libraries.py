import pandas as pd
import sys

if len(sys.argv) < 2:
    print("Please provide the path to the TSV file as a command-line argument.")
    sys.exit(1)

tsv_path = sys.argv[1]

df = pd.read_csv(tsv_path, sep='\t')
print(df)