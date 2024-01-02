class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr1 = set(nums1)
        arr2 = set(nums2)
        inter = arr1 & arr2
        
        lst = []
        for num in inter:
            count = min(nums1.count(num), nums2.count(num))
            lst.extend([num] * count)
        
        return lst