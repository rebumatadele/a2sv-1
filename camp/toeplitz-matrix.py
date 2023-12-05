class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)

        for rows in range((len(matrix) -1)):
            for column in range(len(matrix[rows]) -1):
                #the list would go out of index, so be carefull                   
                if matrix[rows][column] != matrix[rows + 1][column+1]:
                    return False
        return True

            