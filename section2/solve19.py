from operator import itemgetter
with open("popular-names.txt") as f :
    lines = f.readlines()
names = {}
for line in lines:
    name = line.split()[0]
    if name not in names: names[name] = 0
    names[name] += 1
lst = sorted(names.items(), reverse=True, key=itemgetter(1))
for elem in lst:
    print(elem[1], elem[0])
# cut -f 1 ${file} | sort | uniq -c | sort -n -r