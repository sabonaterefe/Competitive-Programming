from collections import defaultdict

class AuthenticationManager(object):
    def __init__(self, timeToLive):
        self.tokens = {}
        self.expiration_times = defaultdict(int)
        self.timeToLive = timeToLive

    def generate(self, tokenId, currentTime):
        expirationTime = currentTime + self.timeToLive
        self.tokens[tokenId] = expirationTime
        self.expiration_times[expirationTime] += 1

    def renew(self, tokenId, currentTime):
        if tokenId in self.tokens:
            expirationTime = self.tokens[tokenId]
            if expirationTime > currentTime:
                self.expiration_times[expirationTime] -= 1
                expirationTime = currentTime + self.timeToLive
                self.tokens[tokenId] = expirationTime
                self.expiration_times[expirationTime] += 1

    def countUnexpiredTokens(self, currentTime):
        expired_tokens = []
        count = 0
        for expirationTime, tokenCount in self.expiration_times.items():
            if expirationTime > currentTime:
                count += tokenCount
            else:
                expired_tokens.append(expirationTime)
        for expirationTime in expired_tokens:
            del self.expiration_times[expirationTime]
        return count