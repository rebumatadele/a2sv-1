class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        temp = capacity
        steps = 0
        for i in range(len(plants)):
            if plants[i] > temp:
                steps += i + (i + 1)
                temp = capacity
            elif plants[i] <= temp:
                steps += 1
            temp -= plants[i]

        return steps
