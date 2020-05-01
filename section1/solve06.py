from section1.solve05 import letterNgram
X = "paraparaparadise"
Y = "paragraph"
setX = letterNgram([X], 2)
setY = letterNgram([Y], 2)
print("union = ", setX.union(setY))
print("intersection = ", setX.intersection(setY))
print("X \\ Y = ", setX.difference(setY))
print("Y \\ X = ", setY.difference(setX))
print("\"se\" contains X = ", "se" in X)
print("\"se\" contains Y = ", "se" in Y)