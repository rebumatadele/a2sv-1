class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row = defaultdict(int)
        col = defaultdict(int)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                row[r] = max(row[r], grid[r][c])
                col[c] = max(col[c], grid[r][c])
        # print(row)
        # print(col)
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                res += min(col[c], row[r])- grid[r][c]
        return res


