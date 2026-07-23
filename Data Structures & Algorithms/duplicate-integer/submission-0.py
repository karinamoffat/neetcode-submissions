class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # initialize hash table
        # loop through nums, adding each item to the hash
        # define an empty frequency dictionary
        # use .get to track if item exists already or not
        freq = {}

        for num in nums: # O(n)
            if num in freq: # O(n)
                freq[num] += 1
                return True
            else:
                freq[num] = 1
        
        return False
        
        