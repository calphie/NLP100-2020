with open("popular-names.txt") as f :
    lines = f.readlines()
lst = sorted(map(lambda line:int(line.split()[2]), lines), reverse=True)
for elem in lst:
    print(elem)
# cut -f 3 ${file} | sort -n -r