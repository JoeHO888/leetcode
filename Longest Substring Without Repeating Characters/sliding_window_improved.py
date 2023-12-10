# Use sliding window in the search
# Whenever there is an repeated element
# move the begin of the sliding window to the right
# Instead of moving right pointer 1 step forward
# move it to the position after the last position of 
# repeated element

# Example
# a,b,c,a,z
# when right pointer encounters 2nd a, as we already saw a
# we move left pointer to z

# To achieve that, we need a map to capture position of
# every element seen

# One thing to note, when we are traversing the array,
# there are some elements being seen but on the left side of left
# point as we are moving left pointer, these elements are not
# in the sliding window, so can ignore

# Example
# a,b,c,a,z,e,f,b,l
# let's say our left & right pointers are at 2nd a & 2nd b
# As we transverse the array, 1st b will be in the map,
# but we move the left pointer to 2nd a already, so we will
# ignore the 1st b in the map & still count 2nd b
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        begin = 0
        end = 0
        result = 0
        characters_seen = {}

        while end < len(s):
            if not s[end] in characters_seen:
                characters_seen[s[end]] = end
                result = max(result, end - begin + 1)
                end += 1
            elif characters_seen[s[end]] < begin:
                characters_seen[s[end]] = end
                result = max(result, end - begin + 1)
                end += 1
            else:
                begin = characters_seen[s[end]] + 1
        return result

        