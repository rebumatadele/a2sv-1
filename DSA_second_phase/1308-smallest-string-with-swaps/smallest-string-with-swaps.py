class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def find(x):
            if x == parent[x]:
                return x
            else:
                parent[x] = find(parent[x])
                return parent[x]
    
        def union( x, y):
            parent_x = find(x)
            parent_y = find(y)
            if parent_x != parent_y:
                if rank[parent_x]>=rank[parent_y]:
                    parent[parent_y] = parent_x
                    rank[parent_x] += rank[parent_y]
                else:
                    parent[parent_x] = parent_y
                    rank[parent_y] += rank[parent_x]
        parent = list(range(len(s)))
        rank = [1] * len(s)
        for i,j in pairs:
            union(i,j)   

        indexes_by_root = {}
        chars_by_root = {}
        for i in range(len(s)):
            root = find(i)
            if root not in indexes_by_root:
                indexes_by_root[root] = [i]
                chars_by_root[root] = [s[i]]
            else:
                indexes_by_root[root].append(i)
                chars_by_root[root].append(s[i])
        
        result = [None] * len(s)
        for root in indexes_by_root:
            sorted_characters = sorted(chars_by_root[root])
            for index, slot in enumerate(indexes_by_root[root]):
                result[slot] = sorted_characters[index]
                
        result = ''.join(result)
        return result     
