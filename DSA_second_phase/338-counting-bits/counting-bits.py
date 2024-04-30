class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0 for _ in range(n+1)]
        # for i in range(n+1):
        #     cnt = 0
        #     origional = i
        #     while i >= 1:
        #         j = i
        #         i = i//2
        #         if j != i * 2:
        #             cnt += 1
        #     ans[origional] = cnt
        # return ans
        # print(ans)

        for i in range(n+1):

            if i % 2 == 1:
                ans[i] = ans[i -1] + 1
            else:
                ans[i] = ans[i // 2 ]
                # print("dfg")
        return ans


                
                
