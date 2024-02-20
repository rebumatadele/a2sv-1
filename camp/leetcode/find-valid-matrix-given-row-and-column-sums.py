class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        matrix = []

        for i in range(len(rowSum)):
            listo = []
            for j in range(len(colSum)):
                numo = min(rowSum[i], colSum[j])
                rowSum[i] -= numo
                colSum[j] -= numo
                listo.append(numo)
            matrix.append(listo)
       
        return matrix
