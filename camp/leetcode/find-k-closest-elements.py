class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = -1
        right = len(arr)
        res = []
        while left + 1 < right:
            mid = (left + right) // 2
            if arr[mid] == x:
                res.append(x)
                right = mid + 1
                left = mid - 1
                break
            elif arr[mid] > x:
                right = mid
            else:
                left = mid

        while left == -1 and k > len(res):
            res.append(arr[right])
            right += 1
        while right == len(arr) and k > len(res):
            res.append(arr[left])
            left -= 1

        while len(res) < k:
            if abs(x - arr[left]) > abs(x - arr[right]):
                res.append(arr[right])
                right += 1
            else:
                res.append(arr[left])
                left -= 1

            while left <= -1 and len(res) < k:
                res.append(arr[right])
                right += 1
            while right >= len(arr) and len(res) < k:
                res.append(arr[left])
                left -= 1

        res.sort()
        return res

