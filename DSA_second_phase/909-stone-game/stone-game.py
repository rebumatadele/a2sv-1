class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        ans = 0
        for i in range(1, n // 2 + 1):
            ans += max(piles[i] - piles[n - i], piles[n - i] - piles[i])
        return ans > 0