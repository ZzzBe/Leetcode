class Solution(object):
	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		hashtable_num={}
		nums_len=len(nums)
		for i in range(nums_len):
			sol_value=target-nums[i]
			if sol_value in hashtable_num:
				return [hashtable_num[sol_value],i]
			hashtable_num[nums[i]]=i
		return []

if __name__ == '__main__':
	nums = [2,7,11,15]
	target = 9
	print (Solution().twoSum(nums,target))
