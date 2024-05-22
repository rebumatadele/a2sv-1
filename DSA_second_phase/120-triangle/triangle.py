class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ans = triangle.copy()
        print(ans)
        
        for r in range(len(triangle)):
            for c in range(len(triangle[r])):
                if r == c == 0:
                    ans[0][0] = triangle[0][0]

                elif c == 0:
                    ans[r][c] = triangle[r-1][c] + triangle[r][c]

                elif c == (len(triangle[r]) - 1):
                    ans[r][c] = triangle[r-1][c-1] + triangle[r][c]

                else:
                    ans[r][c] = min(triangle[r-1][c], triangle[r-1][c-1]) + triangle[r][c]
        return min(ans[-1])

