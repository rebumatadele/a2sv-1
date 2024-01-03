class Solution:
    def smallestNumber(self, num: int) -> int:
        nums = str(num)
        lst = []
        for char in nums:
            if char.isdigit():
                lst.append(int(char))
        if nums[0] == "-":
            lst.sort(reverse = True)
        else:
            lst.sort()
        print(lst)
        if lst[0] == 0:
            for i in range(1, len(lst)):
                if lst[i] !=0:
                    lst[0], lst[i] = lst[i], lst[0]
                    break
        res = "".join(map(str, lst))
        if nums[0] == "-":
            res = 0 - int(res)
        else:
            res = int(res)
        return(res)