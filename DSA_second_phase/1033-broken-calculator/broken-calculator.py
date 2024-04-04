class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int: 
        count = 0
        prev = startValue
        if startValue == target: return 0
        if startValue < target:
            while target > startValue:
                if target % 2 == 1:
                    target += 1
                    count += 1
                prev = target
                target //= 2
                count += 1
            temp = 0
            for i in range(count):
                temp += startValue * 2
            return min(count + (startValue - target), temp - prev)
        else: return startValue - target

        

