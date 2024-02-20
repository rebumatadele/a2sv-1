class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lst = [] 
        left = 0
        maximum = 0
        dic = dict()
        for i in range(len(s)):
            dic[s[i]] = i
        for i in range(len(s)):
            maximum = max(maximum, dic[s[i]])
            if maximum == i:
                lst.append((i+1) - left)
                left = i + 1
        return lst

