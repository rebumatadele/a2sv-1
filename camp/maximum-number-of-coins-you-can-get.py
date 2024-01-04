class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        num = len(piles)/3
        pile = piles[:int(len(piles)-num)]
        i = 1
        total = 0
        while i < len(pile):
            total +=pile[i]
            i +=2
        return total


                