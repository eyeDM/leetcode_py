# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if x < 10:
            return True

        x = str(x)

        for i in range(0, len(x)//2):
            if x[i] != x[-1-i]:
                return False

        return True

#print( Solution.isPalindrome(Solution, 700007) )