class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        right = len(citations) -1
        while left <= right:
            mid = (left + right)//2
            if citations[mid] < ((len(citations)) - mid):
                left = mid + 1
            else:
                right = mid -1
        if left == -1:
            left = 0
        return len(citations) - left