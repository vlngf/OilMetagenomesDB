import pandas as pd
import os
import subprocess

# Load the file from the pull request
df_pr = pd.read_csv(os.environ["FILE_PATH"], sep="\t")

# Fetch the version of the file when the fork was created
subprocess.run(["git", "fetch", "origin", "main"])
subprocess.run(["git", "checkout", "FETCH_HEAD", "--", os.environ["FILE_PATH"]])

# Load the old file
df_fork = pd.read_csv(os.environ["FILE_PATH"], sep="\t")

# Find the rows that are in the new file but not in the old file
new_rows = df_pr[~df_pr.isin(df_fork)].dropna()

# Check if any new rows are found
if not new_rows.empty:
    print("\033[31mNew rows added to common_libraries.tsv:\033[0m")
    print(new_rows)
