class Solution:
    def decodeString(self, s: str) -> str:
        def helper(index, encodedStr):
            look = 0
            string = ""
            while index < len(encodedStr):
                if encodedStr[index] == "[": 
                    new_index , SubStr = helper(index+1, encodedStr)
                    string += (look*SubStr)
                    look , index = 0 , new_index
                elif encodedStr[index].isdigit():
                    look = look*10 + int(encodedStr[index])
                elif encodedStr[index] == "]":
                    return index, string
                else:
                    string += encodedStr[index]
                
                index +=1
            return index, string    
                
        i , decodedStr = helper(0,s)
        return decodedStr
        