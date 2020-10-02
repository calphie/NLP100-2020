
from section3.solve20 import loadGBText
import re
text = loadGBText()
lines = loadGBText()
pattern = r"^\[\[Category:(.+)\]\]$"
m = re.compile(pattern)
for i,line in enumerate(lines.split()):
    match = m.match(line)
    if match:
        print(match.group(1))

