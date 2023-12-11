class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        my_dict = {}
        answer = []
        answer.append([])
        answer.append([])
        winner_dict = {}
        for match in matches:
            my_dict[match[1]] = my_dict.get(match[1], 0) + 1
            winner_dict[match[0]] = winner_dict.get(match[0], 0) + 1
        for key, value in my_dict.items():
            # print(key, " ", value)
            if value == 1:
                answer[1].append(key)

              
        for key, value in winner_dict.items():
            # print(key, " ", value)
            if key not in my_dict:
                answer[0].append(key)
        answer[0].sort()
        answer[1].sort()
        return answer

