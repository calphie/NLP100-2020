from sys import argv

N = int(argv[1])
with open("popular-names.txt") as f :
    lines = f.readlines()
total = len(lines)
assert  N <= total
unit = total // N
for start in range(0, total, unit):
    end = min(start + unit, total)
    print("".join(lines[start:end]))
    print("-" * 10)
# split -n $(exec `wc ${FILE}` / ${N}) -d ${FILE} file_prefix

