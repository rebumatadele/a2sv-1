class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        

        for i in range(len(nums), 0, -1):
            tmp = 0
            for j in range(i):
                if not self.compare(nums[j], nums[tmp]):
                    tmp = j
            nums[tmp], nums[i-1] = nums[i-1], nums[tmp]
        return str(int("".join(map(str, nums))))
    def compare(self, n1, n2):
            return str(n1) + str(n2) > str(n2) + str(n1)