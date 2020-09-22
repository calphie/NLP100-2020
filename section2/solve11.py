with open("popular-names.txt") as f:
    with open("popular-names-replace.txt", "w+") as p:
        p.write(f.read().replace("\t", " "))
#  diff <(cat popular-names.txt |  tr "\t" " "  ) <(cat popular-names-replace.txt)