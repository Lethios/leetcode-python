# https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_set = set()

        for digit in nums:
            if digit in unique_set:
                return True
        
            unique_set.add(digit)
        
        return False
