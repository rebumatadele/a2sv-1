class Solution:
    def canCross(self, stones: list[int]) -> bool:
        s = set(stones)
        @cache
        def jump(i, k):
            if i == stones[-1]:
                return True
            for x in range(k - 1, k + 2):
                if x and x + i in s and jump(i + x, x):
                    return True
            return False

        return jump(stones[0], 0)
