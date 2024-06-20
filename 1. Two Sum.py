class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num2index = {}
        for i, num in enumerate(nums):
            complement = target  - num
            if complement in num2index:
                return [num2index[complement], i]
            num2index[num] = i

# In the problem two sum we are looking for two values in the list
# We initialize a dictionary
# Then we use the for loop to iterate over the list
# We subtract from the target and then look for the existence of the second number
# in the dictionary
# if we don't find it, we take the current num and add it to the dictionary
# the key is the number, the value is the INDEX
# we then continue to add numbers until we find the second number we need

