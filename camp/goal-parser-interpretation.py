class Solution:
    def interpret(self, command: str) -> str:
        goal = ""
        j = 0
        for i in command:
            if i == ")":
                j+=1
                continue
            elif i == "G":
                goal += "G"
                j+=1
            elif i == "(" and  command[j+1] ==")" :
                goal+="o"
                j+=1
            elif i == "(" and command[j+1] == "a":
                goal+="al"
                j+=1
            else:
                j+=1
        return goal
