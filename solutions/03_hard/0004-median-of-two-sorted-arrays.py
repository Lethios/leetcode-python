# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr_len = len(nums1) + len(nums2)
        middle_index = arr_len // 2

        merged_arr = []
        i, j = 0, 0
        count = 0

        while count <= middle_index:
            if i >= len(nums1):
                merged_arr.append(nums2[j])
                j += 1
            elif j >= len(nums2):
                merged_arr.append(nums1[i])
                i += 1
            elif nums1[i] < nums2[j]:
                merged_arr.append(nums1[i])
                i += 1
            else:
                merged_arr.append(nums2[j])
                j += 1
            count += 1

        if arr_len % 2 == 0:
            return (merged_arr[middle_index - 1] + merged_arr[middle_index]) / 2
        else:
            return (merged_arr[middle_index])
