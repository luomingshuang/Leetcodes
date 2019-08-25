#coding:utf-8

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
