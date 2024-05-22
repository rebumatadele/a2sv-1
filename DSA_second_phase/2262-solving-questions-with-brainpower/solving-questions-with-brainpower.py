class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = defaultdict(int)
        maxx = [0] * len(questions)
        g_max = 0
        for i in range(len(questions)-1, -1, -1):
            temp = i + questions[i][1] + 1

            if temp < len(questions):

                dp[i] = questions[i][0] + maxx[temp]

                g_max = max(g_max, dp[i])
                maxx[i] = g_max
                continue

            dp[i] = questions[i][0]
            g_max = max(g_max, dp[i])
            maxx[i] = g_max

        # print(dp)
        return max(dp.values())