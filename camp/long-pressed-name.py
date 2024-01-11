class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n = 0      
        t = 0       
        while n <= len(name) and t < len(typed):
            if n < len(name) and typed[t] == name[n]:
                t += 1
                n += 1
            elif typed[t] == name[n-1] and n != 0:
                t += 1
            else:
                return False
            
        return n == len(name) and t == len(typed)
        