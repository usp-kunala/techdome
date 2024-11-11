class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        matching_parentheses = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in matching_parentheses:
                
                if stack and stack[-1] == matching_parentheses[char]:
                    stack.pop()
                else:
                    return False
            else:
                
                stack.append(char)

    
        return not stack
        pass







    



  

