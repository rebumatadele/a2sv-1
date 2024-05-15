class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        def dp(amount):
            if amount == 0:
                return 0
            elif amount < 0:
                return inf
            if amount not in memo:
                # count = 0
                memo[amount] = inf
                for val in coins:
                    memo[amount] = min(1 + dp(amount - val), memo[amount])
            return memo[amount]


        if amount == 0:
            return 0
        coins = list(set(coins))
        memo = defaultdict(int)
        ret = dp(amount)
        print(memo)
        if ret == inf: return -1
        return ret