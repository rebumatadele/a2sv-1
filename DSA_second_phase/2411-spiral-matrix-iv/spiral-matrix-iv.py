# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1] * n for _ in range(m)]
        flag = 'r'
        row, col = 0, 0

        while head:
            matrix[row][col] = head.val

            if flag == 'r' and (col + 1 >= n or matrix[row][col + 1] != -1):
                flag = 'd'
            elif flag == 'd' and (row + 1 >= m or matrix[row + 1][col] != -1):
                flag = 'l'
            elif flag == 'l' and (col - 1 < 0 or matrix[row][col - 1] != -1):
                flag = 'u'
            elif flag == 'u' and (row - 1 < 0 or matrix[row - 1][col] != -1):
                flag = 'r'
            if flag == 'r':
                col += 1
            elif flag == 'd':
                row += 1
            elif flag == 'l':
                col -= 1
            elif flag == 'u':
                row -= 1
            if row >= m or col >= n or row < 0 or col < 0 or matrix[row][col] != -1:
                break

            head = head.next

        return matrix