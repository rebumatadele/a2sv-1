class Solution:
    def minimumSum(self, num: int) -> int:
        res = sorted(str(num))
        res = ''.join(res)
        a = res[0] + res[2]
        b = res[1] + res[3]
        return int(a) + int(b)