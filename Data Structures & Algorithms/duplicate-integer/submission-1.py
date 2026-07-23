class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        1. initialize the hash set
        2. iterate thorugh nums
        i. if num in set return True
        3. if you make it through without returnign true, it means no duplicates found. return False.
        '''

        freq = set()

        for num in nums:
            if num in freq:
                return True
            freq.add(num)
        
        return False