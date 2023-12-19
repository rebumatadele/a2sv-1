from collections import defaultdict


class FrequencyTracker(object):
    def __init__(self) -> None:
        self.my_dict = defaultdict(int)
        self.freq = defaultdict(int)

    def add(self, number):
        self.my_dict[number] +=1
        self.freq[dic := self.my_dict[number]] += 1
        self.freq[dic-1] -= 1

    def deleteOne(self, number):
        if self.my_dict[number]:
            self.my_dict[number] -=1

            self.freq[dic := self.my_dict[number]] += 1
            self.freq[dic+1] -= 1
    
    def hasFrequency(self, frequency):
        return  self.freq[frequency] > 0
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)