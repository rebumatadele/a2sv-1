class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        lst = []
        for i in range(0, len(nums) , 2):
            if nums[i] == 1:
                lst.append(nums[i+1])
            else:
                for _ in range(nums[i]):
                    lst.append(nums[i+1])
        return lst
