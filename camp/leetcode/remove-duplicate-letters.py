class Solution: 
    def removeDuplicateLetters(self, s: str) -> str: 
        d = Counter(s) 
        st = [] 
        se = set() 
        for i in range(len(s)) : 
            if s[i] in se and d[s[i]] > 1 : 
                d[s[i]] -= 1 
            while st and s[i] <= st[-1] and d[st[-1]] > 1 and s[i] not in se:      
                d[st[-1]] -= 1 
                se.remove(st[-1]) 
                st.pop() 
            if s[i] not in se : 
                st.append(s[i]) 
                se.add(s[i])                 
        st = "".join(st) 
        return st