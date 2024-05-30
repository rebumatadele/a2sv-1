class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        ans = 0
        pre = 0
        count = [0] * (2**10)
        count[pre] = 1
        for cha in word:
            pre ^= 1 << (ord(cha) - ord('a'))
            ans += count[pre]
            for i in range(10):
                ans += count[pre ^ (1 << i)]
            count[pre] += 1 
        print(ans)
        return ans

