class Solution:
	def subarraySum(self, nums: List[int], k: int) -> int:
		res = 0 
		Psum = 0
		d = {0 : 1}
		for num in nums:
			Psum += num
			if Psum - k in d:
			
				res += d[Psum - k]

			if Psum not in d:
			
				d[Psum] = 1
			else:
				d[Psum] = d[Psum] + 1

		return res