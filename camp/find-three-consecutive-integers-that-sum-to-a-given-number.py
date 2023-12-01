class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        arr = []
        mid = num//3
        if (mid*3 != num ):
            return arr
        middle = int (num / 3)
        arr.append(middle-1)
        arr.append(middle)
        arr.append(middle+1)
        return(arr)