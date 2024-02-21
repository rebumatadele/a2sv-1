class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        while maxDoubles and target > 1:
            if target %2 == 1:
                target -= 1
                count += 1
            else:
                target = int(target / 2)
                maxDoubles -= 1
                count += 1
        return (count + (target -1))

