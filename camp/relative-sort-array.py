class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr3 = []
        res = []
        arr1.sort()
        for i in arr2:
            for _ in range(arr1.count(i)):
                res.append(i)
        for j in arr1:
            if j not in arr2:
                res.append(j)
        return res

        
