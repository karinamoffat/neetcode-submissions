# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        Idea: use a stack, LIFO.
        Use reverse preorder traversal to iterate through the tree
        Use recursive preorder but do right --> root --> left
        '''

        if root is None:
            return
        
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)

        self.invertTree(root.right)

        return root

# solution for recursive but we are not allowed to use recursive here