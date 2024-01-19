class Solution:
	def maximumUniqueSubarray(self, nums: List[int]) -> int:
		l = 0
		v = set()
		res = 0
		current = 0
		for h in range(len(nums)):
			while nums[h] in v:
				v.remove(nums[l])
				current -= nums[l]
				l+=1
			v.add(nums[h])
			current += nums[h]
			if current > res:
				res = current
		return res