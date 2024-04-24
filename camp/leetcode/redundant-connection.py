class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(k):
            while k != parent[k]:
                parent[k] = parent[parent[k]]
                k = parent[k]
            return k
        
        def union(x, y):
            root1 = find(x)
            root2 = find(y)

            if root1 != root2:
                if size[root1] > size[root2]:
                    parent[root2] = root1
                elif size[root2] > size[root1]:
                    parent[root1] = root2
                else:
                    parent[root1] = root2
                    size[root2] += 1
                return False
            else:
                return True
            


        size = [0] * (len(edges)+1)
        parent = {i:i for i in range( len(edges)+1)}

        for val in edges:
            a = union(val[0], val[1])
            if a:
                return val

