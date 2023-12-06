class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        lst = []
        for i, value in enumerate(boxes):
            step = 0
            for k, val in enumerate(boxes):
                if k == i or val == "0":
                    continue
                elif val == "1":
                  step +=abs(k-i)

            lst.append(step)
        return lst