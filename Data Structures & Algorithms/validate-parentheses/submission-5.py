class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pair_map = {
            '}' : '{',
            ')' : '(',
            ']' : '['
        }

        for c in s:
            if c in pair_map:
                if not stack or stack.pop() != pair_map[c]:
                    return False
            else:
                stack.append(c)
        
        if len(stack) == 0: 
            return True
        else:
            return False

 

                

