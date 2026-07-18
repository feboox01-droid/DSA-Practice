class Solution(object):

    def twoSum(self, nums, target):

        for i in range(len(nums)):

            for j in range(i+1,len(nums)):

                if nums[i]+nums[j]==target:

                    return [i,j] 


#this is my first DSA problem i spend a lot of hr to solve this problem i know its just starting face so yaah its interesting but irritating but i continously dicipline my DSA jounery 
