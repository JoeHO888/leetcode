class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Create a map counting the number of occurences of each element
        # Sort num by occurence count
        # Extract first kth items

        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        # len(nums) + 1
        # Because when there is N elements in nums
        # The max occurrence is N
        # So the max index is N
        # So the array should be N+1 length
        # 0 index of the array is never used
        count_buckets = [[] for _ in range(len(nums) + 1)]

        for num in count:
            count_buckets[count[num]].append(num)
        
        res = []
        for bucket_index in range(len(count_buckets) - 1, 0, -1):
            for num in count_buckets[bucket_index]:
                if len(res) < k:
                    res.append(num)
        
        return res