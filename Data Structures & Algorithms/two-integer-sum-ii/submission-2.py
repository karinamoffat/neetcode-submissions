class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                res = [l +1 , r +1]
                return res
            if sum > target:
                r -= 1
            if sum < target:
                l += 1