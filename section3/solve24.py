from section3.solve20 import loadGBText
import re
pattern = re.compile(r"^\[\[ファイル:(.+)\]\]$")
text = loadGBText()
for line in text.split("\n"):
    match = pattern.match(line)
    if match:
        print(match.group(1).split("|")[0])