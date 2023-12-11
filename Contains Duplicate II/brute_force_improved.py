# Brutal Force
# Assume the array has at least 2 elements
# Assume k is larger than 1
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        for i in range(len(nums)-1):
            # Instead of looping all elements, just loop over up to k elements after i
            for j in range(i+1, min(i+k+1, len(nums))):
                if nums[i] == nums[j]:
                    return True
        
        return False