class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "]": "[", "}": "{"}

        for char in s: # iterates through s
            if char in mapping: # checks if char is a closing character
                if not stack: # empty stack
                    return False
                else:
                    popped = stack.pop() # pops off most recent char in stack
                    if mapping[char] != popped:
                        return False
            else:
                stack.append(char) # if char is an opening character
        
        if stack:
            return False
        return True