class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        new_word1=""
        new_word2=""
        for i, value in enumerate(word1):
            new_word1 +=value
        for i, value in enumerate(word2):
            new_word2 +=value
        if new_word1 == new_word2:
            return True
        else:
            return False

