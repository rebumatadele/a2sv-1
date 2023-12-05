class Solution:
    def largestGoodInteger(self, num: str) -> str:
        sub = ""
        for i, value in enumerate(num):
            if len(num[i:])>=3:
                if value == num[i + 1] == num[i + 2]:
                    current = value + num[i+1] + num[i+2]
                    sub = str(max(sub, current ))
        return sub

