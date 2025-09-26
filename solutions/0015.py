class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        len_n, ans = len(nums), []
        dup_set = set()
        nums.sort()

        for fix in range(0, len_n - 2):
            i, j = fix + 1, len_n - 1

            while i < j:
                sum_n = nums[fix] + nums[i] + nums[j]
                if sum_n < 0:
                    i += 1
                elif sum_n > 0:
                    j -= 1
                else:
                    if (nums[fix], nums[i], nums[j]) not in dup_set:
                        ans.append([nums[fix], nums[i], nums[j]])
                        dup_set.add((nums[fix], nums[i], nums[j]))

                    i += 1

        return ans
