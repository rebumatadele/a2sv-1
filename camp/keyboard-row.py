class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = list("qwertyuiop")
        row2 = list("asdfghjkl")
        row3 = list("zxcvbnm")       
        result = []
        for word in words:
            flag = 0
            temp = word
            word = word.lower()

            if word[0] in row1:
                result_row = row1
            elif word[0] in row2:
                result_row = row2
            elif word[0] in row3:
                result_row = row3
            for i in range(len(word)):
                if word[i] not in result_row:
                    flag = 1
                    break
            if flag == 0:
                result.append(temp)
        return result