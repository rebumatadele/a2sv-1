class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        ret = [-1] * len(queries)
        for i, (a, b) in enumerate(queries):
            if a == b:
                ret[i] = a
            elif heights[max(a, b)] > heights[min(a, b)]:
                ret[i] = max(a, b)
        queries = sorted([(max(a, b), max(heights[a], heights[b]), i) for i, (a, b) in enumerate(queries) if ret[i] == -1], key=lambda x: -x[0])
        s = []
        for i, h, idx in queries:
            while i + 1 < len(heights):
                g = heights.pop()
                while s and -s[-1][0] <= g:
                    s.pop()
                s.append((-g, len(heights)))
            p = bisect_left(s, (-h, -1)) - 1
            if p >= 0:
                ret[idx] = s[p][1]
        return ret        