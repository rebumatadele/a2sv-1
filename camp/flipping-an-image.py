class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        lst = [[] * len(image[0]) for _ in range(len(image))]
        for ind, values in enumerate(image):
            for i in range(len(values)-1, -1, -1):
                lst[ind].append(abs(values[i] - 1))
        return lst
        

