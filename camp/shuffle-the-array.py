class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        shuffled_nums= []
        counter = n
        for i in range(n):
            shuffled_nums.append(nums[i])
            shuffled_nums.append(nums[counter])
            counter +=1

        return shuffled_nums
        
