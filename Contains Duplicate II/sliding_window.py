# Use sliding window/2 poiners
# whenever the difference between right pointer and left pointer
# is more than k
# shift left pointer to the right
# otherwise, shift right pointer to the right
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        begin = 0
        end = 1
        found = False
        numbers_seen = set()
        numbers_seen.add(nums[0])
        
        while end < len(nums):
            if end - begin <= k:
                if not nums[end] in numbers_seen:
                    numbers_seen.add(nums[end])
                    end += 1
                else:
                    found = True
                    break
            else:
                numbers_seen.remove(nums[begin])
                begin += 1
        return found

