class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=str(x)
        if y[::-1]==str(x):
            return True
        else:
            return False