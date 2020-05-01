def myEncypt(sentence:str)->str:
    import string
    return "".join(map(lambda s : chr(219 - ord(s)) if s in string.ascii_lowercase else s, sentence))
print(myEncypt(myEncypt("I am a engineer Working at Indeed!")))