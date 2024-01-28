class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans = 0
        dic = defaultdict()
        lst = []
        i,j = 0,0

        while j<len(fruits):
            if fruits[j] not in dic and len(dic)<2:
                lst.append(fruits[j])
                dic[fruits[j]]=j
                j+=1
            elif  fruits[j] in dic:
                dic[fruits[j]]=j
                j+=1
            else:  
                if dic[lst[0]]>dic[lst[1]]  :
                    i = dic[lst[1]]+1
                    del dic[lst[1]]
                    lst.pop()
                else:
                    i = dic[lst[0]]+1
                    del dic[lst[0]] 
                    lst.pop(0)              
            
            ans=max(ans,j-i)
        return ans