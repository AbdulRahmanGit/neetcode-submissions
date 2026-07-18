class Solution:
    def isValid(self, s: str) -> bool:
        closetopen =  { ")" : "(", "]" : "[", "}" : "{" }
        stack = []
        for c in s:
            if c in closetopen:
                if stack and stack[-1] == closetopen[c]:
                    stack.pop()
                
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False