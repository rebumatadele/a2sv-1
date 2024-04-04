class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)
        val = list(count.values())
        size = len(val)
        if 1 in val:
            return False
        for i in range(size-1):
            for j in range(1+i, size):
                if gcd(val[i], val[j]) == 1 :
                    return False
        return True