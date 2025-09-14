# https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []

        for i in range(n + 1):
            counter = 0
            j = i

            while j > 0:
                counter = counter + 1 if j & 1 == 1 else counter
                j >>= 1
            ans.append(counter)

        return ans
