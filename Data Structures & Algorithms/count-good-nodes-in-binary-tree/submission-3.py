# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(maximum, root, result) -> int:
            
            if root.val >= maximum:
                result += 1
            
            maximum = max(root.val, maximum)

            if root.left:
                result = dfs(maximum, root.left, result)
            if root.right:
                result = dfs(maximum, root.right, result)

            return result

        return dfs(root.val, root, 0)