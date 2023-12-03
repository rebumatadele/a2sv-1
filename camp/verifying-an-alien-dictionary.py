class Solution(object):
    def isAlienSorted(self, words, order):
        unsorted = words
        lookup = {c: i for i, c in enumerate(order)}
        for i in range(len(unsorted)-1):
            word1 = unsorted[i]
            word2 = unsorted[i+1]
            for k in range(min(len(word1), len(word2))):
                if word1[k] != word2[k]:
                    if lookup[word1[k]] > lookup[word2[k]]:
                        return False
                    break
            else:
                if len(word1) > len(word2):
                    return False
        return True