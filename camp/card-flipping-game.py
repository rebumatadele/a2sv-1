class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        
        lst = backs + fronts
        my_set = set(lst)
        pairs = zip(fronts, backs)
        for key, value in pairs:
            if key == value:
                my_set.discard(key)
        min_value = 0
        if len(my_set) >0:
            min_value = min(list(my_set))
        return (min_value)


        
