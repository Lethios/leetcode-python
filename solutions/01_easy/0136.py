# https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        valid_set = set()

        for num in nums:
            valid_set.add(num) if num not in valid_set else valid_set.remove(num)

        for char in valid_set:
            return char
