class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # N - 1, <=. OK
        # N - 1, <, Fail, wrong answer
        # N, <=, Fail, runtime error
        # N, <, Fail, runtime error

        # Binary Search
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1