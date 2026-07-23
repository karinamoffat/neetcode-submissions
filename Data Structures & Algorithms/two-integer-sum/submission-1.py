class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # loop through nums
        # add all nums to hash table
        # subtract nums[i] from target, store in difference
        # use a hash map to determine if difference exists in nums
        # if so, check if they are the same value
        # if so, return lower index first then the higher index

        indices = [0, 0]
        store = {}

        for i in range(len(nums)):
            store[nums[i]] = i

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in store and store[difference] != i:
                indices[0] = min(store[difference], i)
                indices[1] = max(store[difference], i)
                return indices
                
        

