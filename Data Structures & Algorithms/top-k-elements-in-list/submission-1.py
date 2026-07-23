class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        # store the frequency of each value
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        # store the top k frequencies
        sorted_hash = sorted(freq.values(), reverse = True)
        values = list(sorted_hash[:k])

        # find the keys in freq with that value
        
        final = set()
        for val in values:
            for num in nums:
                if freq[num] == val:
                    final.add(num)
        
        return list(final)

        
