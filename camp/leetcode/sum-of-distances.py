class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        pre = {}

        for i, num in enumerate(nums):
            if num not in pre:
                pre[num] = [1, [i]]
            else:
                pre[num][0] += 1
                pre[num][1].append(pre[num][1][-1] + i)

        res = []

        for i, num in enumerate(nums):
            n = len(pre[num][1])
            if n == 1:
                res.append(0)

            else:
                pre2 = pre[num][1]
                k = n - pre[num][0]
                left, right = pre2[k] - i, pre2[-1] - pre2[k]
                mid = (2*k - n + 1)*i
                res.append(right - left + mid)
                pre[num][0] -= 1
        return res