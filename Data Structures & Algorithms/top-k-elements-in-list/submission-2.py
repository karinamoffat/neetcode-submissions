class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a map for number and its frequency
        # frequency becomes an index, store the key at count[frequency] by appending lists
        # iterate through highest to lowest index of count, adding each individiaul item to a 
        # list, while len(res) <= k
        # return res
        freq = {}
        count = [[] for i in range(len(nums) + 1)] # need the +1 bc max freq is length of list, so the index in the count list will be len(list), but bc of zero indexing it will be out of bounds.

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        for val, i in freq.items():
            count[i].append(val)

        print(count)

        res = []
        for i in range(len(count) - 1, 0, -1):
            for num in count[i]:
                res.append(num)

                if len(res) == k:
                    return res

        # loop through highest to lowest index in count
        # if len(res) < k, append value(s) at 
            

