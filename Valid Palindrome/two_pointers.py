class Solution:
    
    # Use 2 pointers to denote the 1st and last characters
    # If any of them is non-alphanumeric, move it forward or backward
    # If both of them are alphanumeric, check if they are the same.
    # If yes, move both pointers 1 step closer to each other. And keep comparing
    # If no, return False
    # If every characters at those 2 pointers we compared are the same
    # Return True

    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1
        while start < end:

            # move start pointer 1 step forward if the character is non-alphanumeric   
            if not s[start].isalnum():
                start += 1
            # move end pointer 1 step backward if the character is non-alphanumeric            
            elif not s[end].isalnum():
                end -= 1
            
            # characters at start and end pointers are alphanumeric
            else:
                # if they aren't the same
                if s[start].lower() != s[end].lower():
                    return False
                # if they are the same, keep comparing
                else:
                    start += 1
                    end -= 1
        return True