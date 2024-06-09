class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = set(nums1)
        res = set()
        for val in nums2:
            if val in s:
                res.add(val)
        return list(res)