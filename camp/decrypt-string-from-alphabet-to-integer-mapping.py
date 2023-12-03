class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        new_str =""
        i=0
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                new_str += chr(int(s[i:i + 2]) + ord('a') - 1)
                i += 3
            else:
                new_str += chr(int(s[i]) + ord('a') - 1)
                i += 1

        return new_str
