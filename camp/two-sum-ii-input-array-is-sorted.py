class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        lst = []
        while j > i:
            if numbers[i] + numbers[j] == target:
                lst.append(i+1)
                lst.append(j+1)
                break
            elif numbers[i] + numbers[j] < target:
                i +=1
                continue
            else:
                j -=1
        return lst
        