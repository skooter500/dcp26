with open("data/shakespere.txt") as f:
    header = f.readline()      # read (and skip) the first line
    print(header)
    for line in f:             # loop over the remaining lines
        print(line, end="")    # each line already ends with "\n"


