class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        que = deque()
        for i in deck:
            if que:
                flip = que[-1]
                que.pop()
                que.appendleft(flip)
                que.appendleft(i)
            else:
                que.append(i)
        return que

