class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left = 0
        right = len(cardPoints) - k
        total = sum(cardPoints[right:])
        res = total
        while right<len(cardPoints):
            total += (cardPoints[left] - cardPoints[right])
            res = max(res,total)
            left += 1
            right += 1
        
        return res