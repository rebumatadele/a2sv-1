class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        d=defaultdict(list)
        safe =set() 
        dic=defaultdict(int)
        ans =[]
        
        for i in range(len(graph)):
            current = 0
            for j in graph[i]:
                current += 1
                d[j].append(i) 
            dic[i] = current
            if current == 0: 
                safe.add(i)
        
        stack=list(safe)
        while(stack):
            x=stack.pop(0)
            for node in d[x]:
                if node not in safe:
                    dic[node] -= 1 
                    if dic[node] == 0:
                        stack.append(node)
                        safe.add(node)

        return sorted(list(safe))