class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        1. initialize hash
        2. check if key is in hash
        3. if key is not in hash, default to 0, if it is return its value. append 1.
        4. put values in a list: list[res.values()]
        5. reverse sort 4
        6. slice 4, return [0:k-1]
        '''

        freq = {}
        final = []
        res = set()
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        top_key = list(freq.values())
        top_key = sorted(top_key, reverse = True)
        top_key = top_key[:k]



        for num in nums:
            for i in range(k):
                if freq[num] == top_key[i]:
                   res.add(num)
        
        return list(res)

