# Write the file counts to a `.csv` file.
# file_out = open("output.txt", "w")
# file_out.write('This is what you are writing to the file')
# file_out.close()
with open("03_file-input-output/file-counter/filecounts.csv") as f:
    with open("03_file-input-output/file-counter/filecounts.txt", "w") as f1:
        for line in f:
            f1.write(line)
