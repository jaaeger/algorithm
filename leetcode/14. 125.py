# Палиндром

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # filtered = "".join(filter(str.isalnum,s)).lower()
        # return filtered == filtered[::-1]
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not self.isalnum(s[left]):
                left += 1
            while left < right and not self.isalnum(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True

    def isalnum(self, s: str) -> bool:
        return (
                ord("0") <= ord(s) <= ord("9")
                or
                ord("A") <= ord(s) <= ord("Z")
                or
                ord("a") <= ord(s) <= ord("z")
        )