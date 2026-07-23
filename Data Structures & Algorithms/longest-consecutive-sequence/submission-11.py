class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        idea 1: use an efficient sorting algorithm to sort the array. then,
            use a count variable and each time you iterate through the array where
            the difference between curr and curr +1 = 1, increment count.
            if difference is greater than 1, reset count to 1.

        idea 2:
        1. iniitalize a set
        2. sort array. add every num in nums to set, do not include duplicates
        3. 
        '''
        if len(nums) == 0:
            return 0

        temp = set()

        # nums = [2, 3, 4, 4, 5, 10, 20]

        for num in nums:
            if num not in temp:
                temp.add(num)
        
        temp = sorted(temp)

        if len(temp) == 1:
            return 1

        print(temp)
        # added every value to the set in ascending order
        count, max_count = 1, 1

        for i in range(1, len(temp)):
            val = temp[i]
            print(val)
            # handling the last element
            if i == len(temp) - 1: # O(1)
                if val - temp[i - 1] == 1:
                    count += 1
                return max(count, max_count)
            
            # starting from element 0
            prev_val = temp[i - 1]
            if val - prev_val == 1:
                count += 1

            if val - prev_val != 1:
                if count > max_count: max_count = count
                count = 1