# Loop over the array twice in a nested loop, try every combination of substring
# Once there is a repeated element, break the inner loop
# Start searching  from the i, i.e. the start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        characters_seen = set()
        for i in range(len(s)):
            for j in range(i,len(s)):
                if not s[j] in characters_seen:
                    characters_seen.add(s[j])
                    result = max(result, j-i+1)
                else:
                    characters_seen = set()
                    break
        return result

