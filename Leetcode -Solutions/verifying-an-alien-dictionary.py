class Solution:
        def isAlienSorted(self, words: List[str], order: str) -> bool:
                 table = str.maketrans(dict(zip(order, sorted(order))))
                 return all(a.translate(table) <= b.translate(table) for a, b in zip(words, words[1:]))
       
  
        