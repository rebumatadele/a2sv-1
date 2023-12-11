class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        from collections import Counter
        percent = 0.25 * len(arr)
        my_dict = Counter(arr)
        return max(my_dict, key = my_dict.get)
