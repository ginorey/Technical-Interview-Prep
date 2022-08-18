# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        # we need to find target value
        # we can use this below to find the number we need
        # current = target - nums[i]
        
        # we will use a dictionary to keep track of the numbers(keys) & their indexes(values)
        # we will iterate over the range of 0, len(nums) - 1
        # and that will give us the index!
        # if the current is not in the dictionary then we will append it(nums[i]) and its index(i)
        # if it is in the dictionary, that means it solves our problem
        # then we will return both the index of the current([i]), and the index of the value in the dict, indexDict[c]
        
        # initialize dict
        indexDict = dict()
        
        # iterate over the indexes
        for i in range(0, len(nums)):
            # keep track of current evaluation
            solution = target - nums[i]
            
            # check if current is in indexDict
            if solution in indexDict:
                # return current index, solution index
                return [i, indexDict[solution]]
            
            # if solution not in indexDict
            if solution not in indexDict:
                # append current index(i) and its value(nums[i])
                indexDict[nums[i]] = i
            
            
                