class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        dic = defaultdict(int)
        left = 0
        maximum = 0
        for r in range(len(answerKey)):
            dic[answerKey[r]] += 1
            if dic['T'] > k and dic['F'] > k:
                dic[answerKey[left]] -= 1
                left += 1
            maximum = max(maximum, r-left +1)
        return maximum