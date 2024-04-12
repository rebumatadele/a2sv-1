# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def build(root):
            dic = defaultdict(list)
            que = deque([root])
            while que:
                current = que.pop()
                if current.left:
                    dic[current.val].extend([current.left.val])
                    dic[current.left.val].extend([current.val])
                    que.append(current.left)

                if current.right:
                    dic[current.val].extend([current.right.val])
                    dic[current.right.val].extend([current.val])
                    que.append(current.right)
            return dic
        graph = build(root)

        print(graph)

        que = deque([target.val])
        dist = 0
        visited = set([target.val])
        ans = []

        while que:
            l = len(que)
            for _ in range(l):
                if dist == k:
                    return list(que)
                    
                current = que.popleft()
                
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        que.append(neighbor)
            
            dist += 1
        return []



            



