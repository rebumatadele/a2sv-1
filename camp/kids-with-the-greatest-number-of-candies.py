class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        lst = []
        for i, value in enumerate(candies):
            max_c = max(candies)
            if value + extraCandies >=max_c:
                lst.append(True)
            else:
                lst.append(False)
        return lst