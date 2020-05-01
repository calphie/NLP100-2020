import string
sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
sentence = sentence.replace(".","").replace(",","")
words = list(map(lambda s:len(s),sentence.split()))
print(words)
