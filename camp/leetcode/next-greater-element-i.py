class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = defaultdict(lambda: -1)
        stack = []
        for i in nums2:
            while stack and i > stack[-1]:
                dic[stack[-1]] = i
                stack.pop()
            stack.append(i)        
        while stack:
            stack[-1] = -1
            stack.pop()
        ans = []
        for i in nums1:
            ans.append(dic[i])
        return ans
