# Read in all the words from the `words.txt` file.
# Then find and print:

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.
longestword = 0
thelongestword = ""
shortestword = 0
theshortestword = ""
thetotalnumberofwords = 0
with open("03_file-input-output/words.txt") as f:
    for row in f:
        thetotalnumberofwords = thetotalnumberofwords + 1
        if len(row) > longestword:
            longestword = len(row)
            thelongestword = row
        # elif len(row) < longestword:
        else:
            shortestword = len(row)
            theshortestword = row

print("The longest word is ", thelongestword, "char count is ", longestword)
print("The shortest word is ", theshortestword, "char count is ", shortestword)
print("The total number of words in the file is", thetotalnumberofwords)
