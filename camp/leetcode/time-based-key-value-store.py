class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((value, timestamp)) 

    def get(self, key: str, timestamp: int) -> str:
        # print(self.dic)
        new_dic = self.dic[key]
        left = -1
        right = len(new_dic)
        while left + 1 < right:
            mid = (right + left) // 2
            if new_dic[mid][1] <= timestamp:
                left = mid
            else:
                right = mid
        if left== -1:
            return ""
        return new_dic[left][0]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)