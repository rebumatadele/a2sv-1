class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = -1
        right = len(letters)
        while left + 1 < right:
            mid = (left + right) // 2
            if target < letters[mid]:
                right = mid
            else:
                left = mid
        if left + 1 < len(letters):
            return letters[left+1]
        return letters[0]