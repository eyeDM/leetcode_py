# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        memory = {}
        result = start = 0

        for i, char in enumerate(s):
            if char in memory and memory[char] >= start:
            #if memory.get(char, -1) >= start:
                start = memory[char] + 1

            memory[char] = i
            result = max(result, i + 1 - start)

        return result

#print( Solution.lengthOfLongestSubstring(Solution, 'abcabcbb') )
#print( Solution.lengthOfLongestSubstring(Solution, 'bbbbb') )
#print( Solution.lengthOfLongestSubstring(Solution, 'pwwkew') )
