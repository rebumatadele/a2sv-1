class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = 0
        dic = defaultdict(int)
        for i in answers:
            dic[i] += 1
        for key, val in dic.items():
            if key < val -1:
                for i in range(ceil(val/(key+1))):
                    count += key + 1
            else:
                count += key + 1                
        return count
