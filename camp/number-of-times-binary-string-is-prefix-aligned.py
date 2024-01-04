class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count = 0
        max_ = flips[0]
        for i in range(1, len(flips) + 1):
            max_ = max(max_, flips[i-1])
            if max_ == i:
                count +=1
        return count
