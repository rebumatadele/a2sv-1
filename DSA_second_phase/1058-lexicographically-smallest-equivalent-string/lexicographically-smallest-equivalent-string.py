class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        

        def find(k):
            while parent[k] != k:
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
                    parent[root2] = root1
                    size[root1] += 1
                    
        parent = defaultdict(str)
        size = defaultdict(str)
        for i in range(len(s1)):
            parent[s1[i]] = s1[i]
            parent[s2[i]] = s2[i]

            size[s2[i]] = 1
            size[s1[i]] = 1


        
        for i in range(len(s1)):
            union(s1[i], s2[i])

        res = defaultdict(list)
        print(parent)
        for key, value in parent.items():
            res[find(value)].append(key)
        print(res)
        ans = []
        for val in res.values():
            val.sort()
            ans.append(val)
        ret = ""
        
        for v in baseStr:
            for val in ans:
                if v in val:
                    ret += val[0]
                    break
            else:
                ret += v
        print(ret)
        return ret