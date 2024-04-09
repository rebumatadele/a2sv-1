class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        lst = []
        for i in houses:
            left = -1
            right = len(heaters)
            while left + 1 < right:
                mid = (left + right) // 2
                if heaters[mid] == i:
                    lst.append(i - heaters[mid])
                    break
                elif heaters[mid] < i:
                    left = mid
                else:
                    right = mid
            else:
                
                if right == len(heaters):
                    right = right - 1
                lst.append((min(abs(i - heaters[right]), abs(i - heaters[left]))))
        return max(lst)
            