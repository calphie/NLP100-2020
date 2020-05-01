from typing import List,Set
def wordNgram(words:List[str], n:int) -> Set[str]:
    N = len(words)
    return set(" ".join(words[ind:ind+n]) for ind in range(N-n+1))
def letterNgram(words:List[str], n:int) -> Set[str]:
    import itertools
    return set(itertools.chain.from_iterable([[w[i:i+n] for i in range(len(w) - n + 1 )] for w in words]))

if __name__ == "__main__":
    sentence = "I am an NLPer"
    print(wordNgram(sentence.split(), 3))
    print(letterNgram(sentence.split(),2))
