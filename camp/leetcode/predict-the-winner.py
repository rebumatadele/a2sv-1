class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def predict(i, j):
            if i == j:
                return nums[i]
            leftDiff = nums[i] - predict(i + 1, j)
            rightDiff = nums[j] - predict(i, j - 1)
            return max(leftDiff, rightDiff)
        
        return predict(0, len(nums) - 1) >= 0