class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        dictionary = {}
        temp = []
        for i, value1 in enumerate(list1):

            for j, value2 in enumerate(list2):
                if value1 == value2:
                    index = i + j
                    dictionary[value1] = index
        min_ = min(dictionary.values())
        for key, value in dictionary.items():
            if value == min_:
                temp.append(key)
        # temp = [min(dictionary, key = lambda k: dictionary[k])]
        return temp