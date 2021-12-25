class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        map={")":"(", "]":"[", "}":"{"}
        for ch in s:
            if ch not in map:
                stack.append(ch)
            elif not stack or map[ch] != stack.pop():
                return False
        return not stack