class Solution:
    def numberOfMatches(self, n: int) -> int:
        games = 0
        while n >1:
            if n%2 == 0:
                games += n/2
                n /=2
            elif n%2 == 1:
                games += (n-1)/2 
                n = (n+1)/2

        return int(games)