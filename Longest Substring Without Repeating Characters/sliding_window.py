# Use sliding window in the search
# Whenever there is an repeated element
# no need to break the inner loop
# instead, move the begin of the sliding window to the right
# and then do the search
# inner loop refers to brute force approach
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        begin = 0
        end = 0
        result = 0
        characters_seen = set()

        while end < len(s):
            if not s[end] in characters_seen:
                characters_seen.add(s[end])
                result = max(result, end - begin + 1)
                end += 1
            else:
                characters_seen.remove(s[begin])
                begin += 1
        return result

        