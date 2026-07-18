# DSA-Practice

1. I solve My DSA Problems ( spend a lot of hr 1+hr) but its interesting
                 class Solution(object):

    def twoSum(self, nums, target):

        for i in range(len(nums)):

            for j in range(i+1,len(nums)):

                if nums[i]+nums[j]==target:

                    return [i,j]
