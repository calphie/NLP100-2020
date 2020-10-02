from section3.solve20 import  loadGBText
import re
lines = loadGBText().split("\n")
pattern = re.compile(r"^=+([^=]+)=+$")
for line in lines:
    obj = pattern.match(line)
    if obj:
        level = line.count("=")//2 - 1
        print(obj.group(1), level)
