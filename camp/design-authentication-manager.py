class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.auth = timeToLive
        self.token = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.token[tokenId] = currentTime + self.auth

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.token and currentTime < self.token[tokenId]:
            self.token[tokenId] = currentTime  + self.auth

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for values in self.token.values():
            if currentTime < values:
                count +=1
        return count
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)