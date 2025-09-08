# https://leetcode.com/problems/valid-palindrome

from string import ascii_letters, digits

class Solution:
    def isPalindrome(self, s: str) -> bool:
        letter_set = set(ascii_letters + digits)
        clean = ''.join(char.lower() for char in s if char in letter_set)

        l, r = 0, len(clean) - 1
        while l < r:
            if clean[l] != clean[r]:
                return False

            l += 1
            r -= 1
       
        return True
