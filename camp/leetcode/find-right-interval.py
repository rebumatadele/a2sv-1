class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        res = [-1] * len(intervals)
        dic = dict()
        for i, val in enumerate(intervals):
            dic[val[0]] = i

        intervals.sort(key = lambda x: x[0])
        for i in range(len(intervals)):
            current = intervals[i][1]
            left = i - 1
            #check this out
            right = len(intervals)
            while left + 1 < right:
                mid = (left + right) // 2
                if intervals[mid][0] >= current:
                    right = mid
                    # break
                else:
                    left = mid
            #left holds the index of the new elements
            if right == len(intervals):
                res[dic[intervals[i][0]]] = -1
                continue
            find = intervals[right][0]
            if find < current:
                res[dic[intervals[i][0]]] = -1
                continue
            res[dic[intervals[i][0]]] = (dic[find])
        print(res)
        return(res)

        
                
