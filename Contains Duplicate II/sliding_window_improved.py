# Use sliding window/2 poiners
# Transverse the array once
# During transversal, add (element, position) to the map
# if same element is found later, check diff between 
# previous position and current position is later than k
# if yes, then return True
# Otherwise, return False
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        found = False
        numbers_seen = {}

        for i in range(len(nums)):
            if not nums[i] in numbers_seen or i - numbers_seen[nums[i]] > k:
                numbers_seen[nums[i]] = i
            else:
                found = True
                break
        return found