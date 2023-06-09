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

# Check if any of the old rows have been modified or deleted
if not df_fork.isin(df_pr).all().all():
    print("Old rows in the file have been modified or deleted")
    exit(1)

# Everything is OK
print("No old rows have been modified or deleted")
