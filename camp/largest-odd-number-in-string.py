class Solution:
    def largestOddNumber(self, num: str) -> str:
        num = num[::-1]
        max_ ="0"
        for i in range(len(num)):
            if int(num[i]) % 2 == 1:
                max_ = num[i:]
                max_= max_[::-1]
                if max_=="0":
                  return ""
                return max_       
        max_= max_[::-1]
        if max_=="0":
          return ""
        return max_