class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n=len(prices)
        dp=[[0,0] for i in range(n+1)]
        for ind in range(n-1,-1,-1):
            for buy in range(2):
                profit=0
                if buy==0: #buy a stock
                    take=-prices[ind]+dp[ind+1][1] 
                    not_take=0+dp[ind+1][0]
                    profit=max(take,not_take)
                else:
                    take=prices[ind]-fee+dp[ind+1][0] 
                    not_take=0+dp[ind+1][1]
                    profit=max(take,not_take)
                dp[ind][buy]=profit
        return dp[0][0]
