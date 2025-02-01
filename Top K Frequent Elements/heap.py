import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Create a map counting the number of occurences of each element
        # Loop the map, push (e, count * -1) to form a max heap
        # Pop the heap for k times

        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        max_heap = []
        for num in count:
            heapq.heappush(max_heap, (count[num] * -1, num))
        
        res = []
        for _ in range(k):
            _, num = heapq.heappop(max_heap)
            res.append(num)
        return res
