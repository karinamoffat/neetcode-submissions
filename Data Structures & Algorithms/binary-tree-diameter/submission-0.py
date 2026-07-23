# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node):
            if node is None:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            curr_diameter = left_height + right_height
            self.res = max(self.res, curr_diameter)

            return max(left_height, right_height) + 1

        dfs(root)
        return self.res