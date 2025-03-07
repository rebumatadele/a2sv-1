class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = defaultdict(int)
        
        for idx, el in enumerate(nums):
            difference = target - el
            if difference in num_dict:
                return [idx, num_dict[difference]]
            num_dict[el] = idx
        

