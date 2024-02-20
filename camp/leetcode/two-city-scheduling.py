class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        total = 0
        half = len(costs) / 2
        costs.sort(reverse= True, key=lambda x: abs(x[0] - x[1]))
        print(costs)
        flag = 0
        flag2 = 0
        for i, val in enumerate(costs):
            if flag >= half:
                total += val[1] 
            elif flag2 >= half:
                total += val[0] 
            else:
                total += min(val)
                if min(val) == val[0]:
                    flag += 1
                if min(val) == val[1]:
                    flag2 += 1

        print(flag, flag2)

        return total
