# https://leetcode.com/problems/find-palindrome-with-fixed-length/

from typing import List

class Solution:
    def __prepareNextStep(self) -> None:
        if self.__leftHalf >= self.__maxLeftHalfValue:
            self.__isEarlyCompletion = True
            return

        if self.__isOneDigit:
            self.__leftHalf += 1
        elif self.__withCenter: # в центре - одни символ
            if self.__center < 9:
                self.__center += 1
            else:
                self.__center = 0
                self.__leftHalf += 1
        else: # в центре - два символа
            self.__leftHalf += 1

    def __reverseString(self, s: str) -> str:
        return s[::-1]

    def __joinHalfes(self) -> str:
        if self.__withCenter:
            s = str(self.__leftHalf) + str(self.__center) + self.__reverseString(str(self.__leftHalf))
        else:
            s = str(self.__leftHalf) + self.__reverseString(str(self.__leftHalf))

        return int(s)

    def __buildPalindrome(self) -> int:
        if self.__isEarlyCompletion:
            return -1

        if self.__isOneDigit:
            return self.__leftHalf

        return self.__joinHalfes()

    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        self.__leftHalf = 1

        if intLength == 1:
            self.__isOneDigit = True
            self.__maxLeftHalfValue = 9
        else:
            self.__isOneDigit = False
            self.__maxLeftHalfValue = 10 ** (intLength // 2)
            self.__withCenter = (intLength % 2 != 0)
            self.__center = 0

            while (self.__leftHalf < self.__maxLeftHalfValue / 10):
                self.__leftHalf *= 10

        needleIndeces = {}
        maxPalindromIndex = 1
        for i in queries:
            needleIndeces[i] = 0
            if i > maxPalindromIndex:
                maxPalindromIndex = i

        self.__isEarlyCompletion = False
        for i in range(1, maxPalindromIndex + 1):
            if self.__isEarlyCompletion:
                break;

            if i in needleIndeces:
                needleIndeces[i] = self.__buildPalindrome()

            self.__prepareNextStep()

        result = []
        for i in queries:
            if needleIndeces[i] == 0:
                result.append(-1)
            else:
                result.append(needleIndeces[i])

        return result

# print(
#     Solution().kthPalindrome([1,2,3,4,5,90], 3)
# )
# print([101,111,121,131,141,999])

# print(
#     Solution().kthPalindrome([2,4,6], 4)
# )
# print([1111,1331,1551])

# print(
#     Solution().kthPalindrome([56,43,511421402,712824534,60879293,333224597,24,77,54,123133700,41,28,32], 4)
# )
# print([6556,5225,-1,-1,-1,-1,3333,8668,6336,-1,5005,3773,4114])

# print(
#     Solution().kthPalindrome([2,201429812,8,520498110,492711727,339882032,462074369,9,7,6], 1)
# )
# print([2, -1, 8, -1, -1, -1, -1, 9, 7, 6])

# print(
#     Solution().kthPalindrome([683392906,677531155,81,635486904,396454130,178964399], 13)
# )
# print([-1, -1, 1000080800001, -1, -1, -1])

# print(
#     Solution().kthPalindrome([492605370,206710368,19,985427531,55,13,979243001,831564215,83], 15)
# )
# print([-1, -1, 100000181000001, -1, 100000545000001, 100000121000001, -1, -1, 100000828000001])
# 25.746 seconds
