class Solution:
   def buddyStrings(self, A, B):
      if len(A)!=len(B):
         return False
      elif sorted(A)!=sorted(B):
         return False
      elif A==B and len(set(A))==len(A):
         return False
      else:
         count=0
         for i in range(len(A)):
            if A[i]!=B[i]:
               count+=1
               if count==3:
                  return False
         return True
ob = Solution()
print(ob.buddyStrings("ba","ab"))