# Use the `csv` module to read in and count the different file types.
# import CSV
# With open(‘some.csv’, ‘rb’) as f:
# reader = csv.reader(f)
# for row in reader:
# print row
import csv

with open("filecounts.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
