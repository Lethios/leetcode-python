# https://leetcode.com/problems/maximum-average-subarray-i

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1:
            return nums[0]

        l = sum = max_sum = 0
        
        for r, num in enumerate(nums):
            sum = sum + num

            if r == k - 1:
                max_sum = sum
            elif r > k - 1:
                sum = sum - nums[l]
                l += 1
            
            max_sum = sum if sum > max_sum else max_sum

        return round(max_sum / k, 5)
