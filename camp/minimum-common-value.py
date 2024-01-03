class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if set(nums1) & set(nums2):
            return(min(set(nums1) & set(nums2)))
        return -1