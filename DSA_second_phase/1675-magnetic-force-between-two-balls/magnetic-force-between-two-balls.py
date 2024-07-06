class Solution:
    def maxDistance(self, a: List[int], m: int) -> int:
        def f(d, y=-inf):
            balls = 0
            for x in a:
                if x-y >= d:
                    y = x
                    balls += 1

            return balls < m

        a = sorted(a)

        return bisect_left(range(a[-1]), 1, key=f)-1