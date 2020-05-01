import random
def wordShuffle(word:str) -> str:
    if len(word) <= 4 :return word
    midWords = list(word[1:-1])
    random.shuffle(midWords)
    return word[0] + "".join(midWords) + word[-1]

sentence = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(" ".join(map(wordShuffle, sentence.split())))