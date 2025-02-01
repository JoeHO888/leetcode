class Solution:
    def frequencySort(self, s: str) -> str:
        
        # Create a counter map
        # Sort element by number of count, n
        # Append that element by n times

        character_count = {}

        for c in s:
            character_count[c] = character_count.get(c, 0) + 1
        
        res = ""
        for character, character_count in sorted(character_count.items(), key=lambda x: x[1], reverse=True):
            for _ in range(character_count):
                res += character
        return res