class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        idxToRemove = set()
        stack = []
        for i, c in enumerate(s):
            if c not in '()':
                continue
            elif c == '(':
                stack.append(i)
            elif not stack:
                idxToRemove.add(i)
            else:
                stack.pop()
        
        idxToRemove = idxToRemove.union(set(stack))
        stringBuilder = []
        
        for i, c in enumerate(s):
            if i not in idxToRemove:
                stringBuilder.append(c)
        
        return ''.join(stringBuilder)