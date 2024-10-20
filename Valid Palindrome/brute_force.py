import math

class Solution:

    # Clean data first
    # Use cleaned data, divide it by 2 (mid point at math.floor(len(cleanData) // 2))
    
    # If the array is even (i.e. 2N), then the last index needs to check is N - 1 -> so range(N)
    # Or this
    # Divide it by 2 -> we are sure that the last element we will check is then at N - 1 -> done

    # If the array is odd (i.e. 2N + 1), then the last index needs to check is N - 1 -> so range(N)
    # i.e. N = math.floor(len(cleanData) // 2)
    # Or this
    # Dividie it by 2 -> N + 0.5 -> use floor to get rid of 0.5 -> as we don't need to check the middle element
    # so just need to through first range(N)


    # Compare index i vs len(cleanData) - 1 - i
    # And see if they are different
    def cleanPhrase(self, phrase:str) -> str:
        cleanPhrase = ""
        for character in phrase:
            if character.isalnum():
                cleanPhrase += character.lower()
        return cleanPhrase
    def isPalindrome(self, s: str) -> bool:
        cleanPhrase = self.cleanPhrase(s)
        for i in range(math.floor(len(cleanPhrase)//2)):
            if cleanPhrase[i] != cleanPhrase[len(cleanPhrase) - 1 - i ]:
                return False
        return True