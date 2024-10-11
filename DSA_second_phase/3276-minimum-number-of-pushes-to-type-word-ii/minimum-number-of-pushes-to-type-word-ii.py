class Solution:
    def minimumPushes(self, word: str) -> int:
        nums = sorted(Counter(word).values(), reverse=True)
        ans1 = sum(nums[:8]) + 2 * sum(nums[8:16]) 
        ans2 =  sum(nums[16:24]) * 3 + sum(nums[24:]) * 4
        ret = ans1 + ans2

        return ret
