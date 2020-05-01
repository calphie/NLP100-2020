sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can"
takeOneLetterIndex = {1,5,6,7,8,9,15,16,19}
atoms = {val[:1 if i+1 in takeOneLetterIndex else 2]:i+1 for i,val in enumerate(sentence.split())}
print(atoms)