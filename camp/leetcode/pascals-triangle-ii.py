class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # 1 in front and 1 in the back
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        n = rowIndex + 1
        res = [1] * n
        temp = self.getRow(rowIndex - 1)
        for i in range(1, len(temp)):
            res[i] = temp[i-1] + temp[i]
        # print(res)
        return res