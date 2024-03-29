#coding:utf-8
###法一：暴力解法
class Solution:
    def twoSum(self, nums, target):       
        N = len(nums)
        sums = []
        
        for idx in range(N):
            for n in range(idx+1, N):
                sums.append((nums[idx]+nums[n], idx, n))
        for sum in sums:
            if sum[0] == target:
                return sum[1],sum[2]
###法二：差值搜索
class Solution:
    def twoSum(self, nums, target):
        N = len(nums)
        sums = []
        for idx in range(N):
            res = target - nums[idx]
            print(nums[idx], res)
            print(nums[idx+1:])
            if res in nums[idx+1:]:
                #print(nums[idx+1:])
                return idx, nums[idx+1:].index(res)+idx+1
