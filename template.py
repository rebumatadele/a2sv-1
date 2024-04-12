import sys
def i(): return int(sys.stdin.readline().strip())
def l(): return list(map(int, sys.stdin.readline().strip().split()))
def ls(): return sorted(list(map(int, sys.stdin.readline().strip().split())))
def s(): return sys.stdin.readline().strip()
def d(): return [int(digit) for digit in input()]
def c(): return list(sys.stdin.readline().strip())

def grid(col):
    array = []
    for _ in range(col):
        a = list(map(int, input().split()))
        array.append(a)
    return array
        
from collections import Counter, defaultdict, deque
from bisect import bisect_right, bisect_left
from math import ceil, sqrt, gcd

#Merge Sort Conquerer
def merge(left_half, right_half):
    left_index = 0
    right_index = 0
    sorted_array = []
 
    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] <= right_half[right_index]:
            sorted_array.append(left_half[left_index])
            left_index += 1
        else:
            sorted_array.append(right_half[right_index])
            right_index += 1

    sorted_array.extend(left_half[left_index:])
    sorted_array.extend(right_half[right_index:])

    return sorted_array

#Merge Sort Divider Function
def mergeSort(left, right, arr):
    if left == right:
        return [arr[left]]
    
    mid = left + (right - left) // 2
    left_half = mergeSort(left, mid, arr)
    right_half = mergeSort(mid + 1, right, arr)

    return merge(left_half, right_half)

# Helper Function for binary search
def binary_helper(arr, pos, condition):
    total = 0
    test = 0
    for i in arr:
        test += ceil(i/pos)
    if test <= condition:
        return True

#Binary Search           
def binary(arr):
    left = 0
    right = max(arr)
    while left + 1 < right:
        mid = (left + right) // 2
        if binary_helper(arr, mid):
            right = mid
        else:
            left = mid
    return right

def sieve(n):
    is_prime:list[bool] = [True for _ in range(n + 1)]
    is_prime[0] = is_prime[1] = False
    d = 2
    while d*d <= n:
        if is_prime[d]:
            i = d * d
            while i <= n:
                is_prime[i] = False
                i += d
        d += 1   
    ans = []
    for i, val in enumerate(is_prime):
        if val:
            ans.append(i)      
    return ans
def prime_factor(n):
    factorization: list[int] = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factorization.append(d)
            n //= d
        d += 1
        if n > 1:
            factorization.append(n)
    return factorization
def is_prime(x: int) -> bool:
    d = 2
    while d*d <= x:
        if x % d == 0:
            return False
        d += 1
    return True

def factor(n):
    factors = []
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    return factors

#finding GCF from a list
def find_gcf(numbers):
    if len(numbers) == 0:
        return None
    gcf = numbers[0]
    for num in numbers[1:]:
        gcf = gcd(gcf, num)
    return gcf 

#finding lcm
def find_lcm(numbers):
    if len(numbers) == 0:
        return None
    lcm = numbers[0]
    for num in numbers[1:]:
        lcm = lcm * num // gcd(lcm, num)
    return lcm

#finding gcd manually
def gcd(a, b):
 if b == 0:
    return a
 return gcd(b, a % b)

def buildListDWG():
    n = int(input())
    graph = defaultdict(list)
    for i in range(n):
        line = input().split()
        node = int(line[0])
        for neighbor in range(1, len(line)):
            adj_node, weight = map(int, line[neighbor].split(","))
            graph[node].append((adj_node, weight))
    return graph

def buildMatrixDWG():
    n = int(input())
    graph = defaultdict(list)
    for i in range(n):
        row = list(map(int, input().split()))
        for j in range(len(row)):
            graph[i].append((j, row[j]))
            
def buildCount(isConnected):
    graph = defaultdict(list)
    for i, val in enumerate(isConnected):
        temp = []
        for j in val:
            if j:
                temp.append(j)
        graph[i] = temp
    return graph

def dfsRecursion(key, visited, graph):
    visited.add(key)
    for neighbor in graph[key]:
        if neighbor not in visited:
            dfsRecursion(neighbor)

def dfsGrid(grid):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
    
    def inbound(row, col):
        return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
    
    def dfs(grid, visited, row, col):
        visited[row][col] = True
        #Base Case Goes Here
        for row_change, col_change in directions:
            new_row = row + row_change
            new_col = col + col_change
            if inbound(new_row, new_col) and not visited[new_row][new_col]:
                dfs(grid, visited, new_row, new_col)

def dfsIterative(edges, source, destination):
    def build(edges):
        graph = defaultdict(list)
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
            
    graph = build(edges)
    stack = [source]
    visited = set([source])
    while stack:
        node = stack.pop()
        if node == destination:
            return True
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)
    
def bfs(graph):
    visited = set([node])
    queue = deque([node])
    # _list = []
    while queue:
        node = queue.popleft()
        # _list.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return

def levelOrder(root):

        if not root: return []
        que = deque([root])
        res = []

        while que:
            l = len(que)
            temp = []
            
            for _ in range(l):
                node = que.popleft()
                temp.append(node.val)

                if node.left:
                    que.append(node.left)

                if node.right:
                    que.append(node.right)

            res.append(temp)

        return res


#execution starts here
def solve():
    
    return
#accepting test cases   
t = i()
for i in range(t):
    solve()