# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_width = 0
        queue = deque()
        queue.append((root, 0))
        
        while queue:
            current_level_length = len(queue)
            node, level_head_index = queue[0]
            
            for i in range(current_level_length):
                node, col_index = queue.popleft()
                if node.left:
                    queue.append((node.left, 2*col_index))
                if node.right:
                    queue.append((node.right, 2*col_index+1))
            max_width = max(max_width, col_index-level_head_index+1)
        
        return max_width
        