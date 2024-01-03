class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for i in s:
            if i.isalnum():
                new_str +=i.lower()
        print(new_str)
        i = 0
        j = len(new_str) - 1
        while i<j:
            if new_str[i] != new_str[j]:
                return False
            i+=1
            j-=1
        return True
        