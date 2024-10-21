class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        # Create counter map
        # Sort it by 2 levels, count & then alphabetical order
        count = {}
        for word in words:
            count[word] = count.get(word, 0) + 1
        
        return [ word for word, _ in sorted(count.items(), key=lambda x: (-x[1], x[0]))][:k]