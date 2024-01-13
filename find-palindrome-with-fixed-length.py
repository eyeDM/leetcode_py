# https://leetcode.com/problems/find-palindrome-with-fixed-length/

from typing import List

class Solution:
    def __simplestCase(self, queries: List[int]) -> List[int]:
        result = []

        for i in queries:
            if i > 9:
                result.append(-1)
            else:
                result.append(i)

        return result

    def __buildPalindrome(self, leftHalfSeed: int, withCenter: bool, i: int) -> int:
        leftHalf = str(leftHalfSeed + i - 1)

        if withCenter:
            return int(
                leftHalf + leftHalf[:-1][::-1]
            )
        else:
            return int(
                leftHalf + leftHalf[::-1]
            )

    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        if intLength == 1:
            return self.__simplestCase(queries)

        if intLength % 2:
            withCenter = True
            maxIndex = 9 * 10 ** (intLength // 2)
        else:
            withCenter = False
            maxIndex = 9 * 10 ** (intLength // 2 - 1)

        leftHalfSeed = 1
        while (leftHalfSeed < maxIndex / 10):
            leftHalfSeed *= 10

        result = []
        cache = {}
        for j, i in enumerate(queries):
            if i > maxIndex:
                result.append(-1)
            else:
                if i in cache:
                    result.append(result[ cache[i] ])
                else:
                    result.append(
                        self.__buildPalindrome(leftHalfSeed, withCenter, i)
                    )
                    cache[i] = j

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
# 0.08 seconds
