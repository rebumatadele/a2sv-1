class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def ship(num):
            a = 0
            day = 0
            for i in range(len(weights)):
                if a + weights[i] <= num:
                    a += weights[i]
                else:
                    a = weights[i]
                    day += 1
                    if a > num:
                        return False
            day += 1
            if day <= days:
                return True
            return False

        pos = max(weights) * ceil(len(weights) / days)
        left = sum(weights) // days - 1
        right = pos + 1
        while left + 1 < right:
            mid = (left + right)//2
            if ship(mid):
                right = mid
            else:
                left = mid
        return right

        