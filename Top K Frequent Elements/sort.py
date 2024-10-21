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
        
        return [ num for num, _ in sorted(count.items(), key=lambda x: x[1], reverse=True)][:k]
