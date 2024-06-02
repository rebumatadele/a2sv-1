class Solution:
    def sortSentence(self, s: str) -> str:
        lst = list(s.split())
        lst.sort(key = lambda x: x[-1])
        for i, value in enumerate(lst):
            lst[i] = value[:len(value) -1]
        string = " ".join(map(str, lst)).strip()
        return(string)