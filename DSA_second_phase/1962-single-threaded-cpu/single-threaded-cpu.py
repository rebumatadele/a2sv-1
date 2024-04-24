class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        arr = []
        curr = 0
        res  = [] 
        tasks= sorted((tasks,i) for i,tasks in enumerate(tasks))
        for (m,n), i in tasks:
            while arr and curr < m:
                p,j,k = heappop(arr)
                curr = max(k,curr)+p
                res.append(j)
            heappush(arr,(n,i,m))
        return res+[i for _, i, _ in sorted(arr)]
            



