with open("popular-names.txt") as f :
    lines = f.readlines()
lst = sorted(list(set(map(lambda line:line.split()[0], lines))))
for elem in lst:
    print(elem)
# cut -f 1 ${file} | sort | uniq