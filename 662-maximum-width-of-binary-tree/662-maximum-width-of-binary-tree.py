# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque()
        maxWidth = 0
        queue.append((root, 0))
        
        while queue:
            length = len(queue)
            node, levelHeadIdx = queue[0]
            
            for i in range(length):
                node, currLevelIdx = queue.popleft()
                if node.left:
                    queue.append((node.left, 2*currLevelIdx))
                if node.right:
                    queue.append((node.right, 2*currLevelIdx+1))
                    
            maxWidth = max(maxWidth,currLevelIdx-levelHeadIdx+1)

        return maxWidth
    	