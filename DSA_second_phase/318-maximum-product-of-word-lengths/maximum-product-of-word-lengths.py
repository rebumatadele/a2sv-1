class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        bitmask = [0 for _ in range(n)]

        for i in range(n):
            for val in words[i]:
                bitmask[i] = bitmask[i] | (1 << ord("z") - ord(val))
        
        ret = 0
        for i in range(n):
            for j in range(i+1, n):
                if not (bitmask[i] & bitmask[j]):
                    ret = max(ret, len(words[i]) * len(words[j]))
        return ret

