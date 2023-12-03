from typing import List

class Solution:
    def printVertically(self, s: str) -> List[str]:
        new_s = s.split()
        max_length = max(len(word) for word in new_s)
        end_s = [""] * max_length
        for p in range(max_length):
            for i in new_s:
                if p < len(i):
                    end_s[p] += i[p]
                else:
                    end_s[p] += " "
            end_s[p]= end_s[p].rstrip() 
        return end_s