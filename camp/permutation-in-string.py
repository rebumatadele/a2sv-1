class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic1 = defaultdict(int)
        dic2 = defaultdict(int)
        w = len(s1)
        left = 0

        if len(s1) > len(s2):
            return False
        for i in s1:
            dic1[i] += 1
        
        for i in range(w):
            dic2[s2[i]] += 1
            
        for right in range(w, len(s2)):
           
            if dic1 == dic2:
                return True
            dic2[s2[left]] -= 1
            dic2[s2[right]] += 1
            
            if dic2[s2[left]] == 0:
                del dic2[s2[left]]
            left += 1
            
        if dic1 == dic2:
                return True

        

        





