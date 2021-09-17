# Refactor your file counter script to use `pathlib` also for
# reading and writing to your CSV file. Make sure to handle the
# path in a way so that you can run the script from anywhere. Absolute path
from pathlib import Path

data_path = Path("/home/leena/python-201/03_file-input-output/file-counts.csv")
with open(data_path.joinpath)
