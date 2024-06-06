class Solution:
    def minimumSteps(self, s: str) -> int:
        res = 0                          
        black = []  
        n = len(s)        
        for i in range(n):
            if s[i] == '1':
                black.append(i) 
        black.reverse()       
        for i in range(len(black)):
            res += (n - i - 1 - black[i])
        return res  
