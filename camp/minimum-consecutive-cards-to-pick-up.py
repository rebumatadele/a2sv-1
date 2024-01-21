class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        c={}
        l=0
        res=float("inf")
        for r in range(len(cards)):
            if cards[r] in c:
                while l<r and ((cards[l]!=cards[r]) or (c[cards[r]]>1)):
                    c[cards[l]]-=1   
                    if c[cards[l]]==0:
                        del c[cards[l]]
                    l+=1
                
                res=min(res,r-l+1)
            c[cards[r]]=1+c.get(cards[r],0)
        return res if not res==float("inf") else -1