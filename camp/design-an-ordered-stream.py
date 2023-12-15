class OrderedStream:

    def __init__(self, n: int):
        self.my_list = [None]*n

    def insert(self, idKey: int, value: str) -> List[str]:
        self.my_list[idKey-1] = value
        for j in range(len(self.my_list)):
            if self.my_list[j] == None:
                return self.my_list[idKey-1:j]
            elif j == len(self.my_list) - 1:
                return self.my_list[idKey-1:j+1]
                



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)