# https://leetcode.com/problems/maximize-sum-of-at-most-k-distinct-elements/

class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        min_heap, unique = [], set()

        for num in nums:
            if num in unique:
                continue
            else:
                unique.add(num)

            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return sorted(min_heap, reverse=True)
