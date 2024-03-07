class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = -1
        right = len(matrix)
        while left + 1 < right:
            mid = (left + right) // 2
            if matrix[mid][0] == target:
                return True
            elif target > matrix[mid][0]:
                left = mid
            else:
                right = mid
        candidate = matrix[left]
        left = -1
        right = len(candidate)
        while left + 1 < right:
            mid = (left + right) // 2
            if candidate[mid] == target:
                return True
            elif candidate[mid] > target:
                right = mid
            else:
                left = mid
        return False
