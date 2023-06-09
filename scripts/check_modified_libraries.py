import pandas as pd
import os

# Load the tsv files
file_path = os.environ.get('FILE_PATH')
df_PR = pd.read_csv(file_path, sep='\t')

# Replace 'main' with 'master' if your default branch is master
df_fork = pd.read_csv(f"https://raw.githubusercontent.com/{os.environ.get('GITHUB_REPOSITORY')}/main/common_libraries/common_libraries.tsv", sep='\t')

# Check if any rows have been deleted
if len(df_PR) < len(df_fork):
    print("Rows have been deleted from the TSV file. This is not allowed.")
    exit(1)

# Check if any existing values have been modified
for column in df_PR.columns:
    if any(df_PR[column] != df_fork[column]):
        modified_rows = df_PR.index[df_PR[column] != df_fork[column]].tolist()
        for row in modified_rows:
            print(f"Value in column {column} and row {row} has been modified. This is not allowed.")
        exit(1)
