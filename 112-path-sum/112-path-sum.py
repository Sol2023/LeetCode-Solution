# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        sums =[]
        self.calculateBranchSums(root, 0, sums)
        for num in sums:
            if num == targetSum:
                return True
        return False
    
    def calculateBranchSums(self, node, runningSums, sums):
        if node is None:
            return
        
        newRunningSums= runningSums + node.val
        if node.left is None and node.right is None:
            sums.append(newRunningSums)
            return
        
        self.calculateBranchSums(node.left, newRunningSums, sums)
        self.calculateBranchSums(node.right, newRunningSums, sums)
        
    
        