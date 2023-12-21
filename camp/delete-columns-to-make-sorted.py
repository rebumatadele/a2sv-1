class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        from collections import defaultdict
        count=0
        dic = defaultdict(list)
        for r in range(len(strs)):
            for c in range(len(strs[0])):
                dic[c].append(strs[r][c])
        for i,el in dic.items():
            test = el.copy()
            test.sort()
            if test != el:
                count +=1
        print(dic)
        return(count)