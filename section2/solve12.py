from operator import itemgetter
with open("popular-names.txt") as f:
    with open("col1.txt", "w+") as f1:
        with open("col2.txt", "w+") as f2:
            fileContents = list(map(lambda x:x.split(),f.readlines()))
            f1.write("\n".join(map(itemgetter(0), fileContents)))
            f2.write("\n".join(map(itemgetter(1), fileContents)))
# cut popular-names.txt -f 1 > col1.txt
# cut popular-names.txt -f 1 > col2.txt

