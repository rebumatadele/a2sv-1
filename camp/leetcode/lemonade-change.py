class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dic = defaultdict(int)
        for i in bills:
            if i == 5:
                dic[5] += 1
            elif i == 10:
                dic[5] -= 1
                dic[10] += 1
                if dic[5] < 0:
                    return False
            elif i == 20:
                if dic[10] >= 1:
                    dic[10] -= 1
                    dic[5] -= 1
                else:
                    dic[5] -=3
                dic[20] += 1
                if dic[5] < 0:
                    return False
        return True