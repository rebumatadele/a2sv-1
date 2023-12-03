class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        key = min(len(word1) , len(word2))
        new_word = ""
        for i in range(key):
            new_word +=word1[i]
            new_word +=word2[i]
        if len(word1)> len(word2):
            new_word +=word1[key:]
        elif len(word1)< len(word2):
            new_word +=word2[key:]
        return new_word