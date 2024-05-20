class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = [0] * (amount+1)
        memo[0] = 1
        for val in coins:
            for j in range(len(memo)):
                if val > j: 
                    continue

                memo[j] += memo[j - val]

        return memo[-1]
        
        
