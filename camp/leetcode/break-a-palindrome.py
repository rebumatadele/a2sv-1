class Solution:
    def breakPalindrome(self, palindrome: str) -> str: 
        lst = list(palindrome)
        l = (len(palindrome) // 2) - 1
        if len(lst) == 1:
            return ""

        for i in range(l + 1):
            if lst[i] > "a":
                lst[i] = "a"
                break
        else:
            for i in range(l + 2, len(lst)):
                if lst[i] > "a":
                    lst[i] = "a"
                    break     
            else:
                lst[-1] = "b"    

        return "".join(lst)

                