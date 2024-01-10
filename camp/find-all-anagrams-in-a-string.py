class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dic1 = Counter(p)
        print(dic1)
        dic2 = Counter(s[:len(p)])
        left = 1
        lst = []
        if dic1 == dic2:
            lst.append(0)
        for i in range(len(p), len(s)):
            dic2[s[left-1]] -= 1
            dic2[s[i]] += 1
            if dic2[s[left-1]] == 0:
                del dic2[s[left-1]]
            if dic1 == dic2:
                lst.append(left)
            left +=1
        return lst

            
