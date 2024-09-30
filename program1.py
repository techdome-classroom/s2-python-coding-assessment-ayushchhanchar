class Solution(object):
    def isValid(self, s):
       
        stack = []
        
        matching_pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for char in s:
            if char in matching_pairs:
                stack.append(char)
            else:
                if not stack or matching_pairs[stack.pop()] != char:
                    return False
        return len(stack) == 0


# python -m unittest test1.py

