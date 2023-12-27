class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        #Count Sort qrr 1 according to arr2 as a key
        max_ = max(arr1)
        min_ = min(arr1)
        lst = []
        res = []
        
        lst = [0]*(max_+ 1)
        for value in arr1:
            lst[value] +=1
        for value in arr2:
            res.extend([value]*lst[value]) 
            lst[value] = 0
        print(lst)
        for p in range(len(lst)):
            if lst[p] != 0:
                res.extend([p]*lst[p])
        return res
