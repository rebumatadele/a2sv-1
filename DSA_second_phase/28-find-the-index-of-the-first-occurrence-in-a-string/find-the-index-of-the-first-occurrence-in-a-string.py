class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        h = len(haystack)
        n = len(needle)
        i = 0
        j = n - 1
        while j < h:
            temp = haystack[i:j+1]
            # print(temp)
            if temp == needle:
                return i
            j += 1
            i += 1
        return -1

        

