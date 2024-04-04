class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:

        # n = len(nums)
        # ans = 0
        # for i in range(n):
        #     temp = nums[i]
        #     for j in range(i, n):
        #         temp = math.gcd(temp, nums[j])
        #         if temp == k:
        #             ans += 1
        #         elif temp < k:
        #             break
        # return ans


        count = 0
        for i in range(len(nums)):
            temp = nums[i]
            for j in range(i, len(nums)):
                temp = gcd(temp, nums[j])
                if temp == k:
                    count += 1
                elif temp < k:
                    break
        return count