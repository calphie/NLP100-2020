from sys import argv
n = int(argv[1])
with open("popular-names.txt") as f :
    print("".join(f.readlines()[-n:]))
