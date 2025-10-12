# Problem: https://leetcode.com/problems/valid-parentheses/
# Difficulty: Easy
# Time Complexity: O(n)
# Space Complexity: O(n)

def isValid(s):

    stack=[]
    mapping={')':'(', '}':'{', ']':'['}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else: #alakasiz karakter
            return False
    return not stack
s = "({[()]})"
print(isValid(s))