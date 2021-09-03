# Write a program that reads in `words.txt` and prints only the words
# that have more than 20 characters (not counting whitespace).
with open("03_file-input-output/words.txt") as f:
    for row in f:
        if len(row) > 20:
            print(row)
