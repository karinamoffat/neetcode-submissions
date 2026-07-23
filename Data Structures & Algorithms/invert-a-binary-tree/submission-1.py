# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        Inverse of pre-order: root --> right --> left
        1. curr = stack.pop() # 1
        2. if curr.left and curr.right
            i. stack.append(curr.left) 
            ii. stack.append(curr.right)
            a. temp = curr.left # 2
            b. curr.left = curr.right # 3
            c. curr.right = temp # 2
        3. 
        '''

        if root is None:
            return None

        stack = [root]
        
        while stack:
            curr = stack.pop()
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
            
            temp = curr.left
            curr.left = curr.right
            curr.right = temp

        return root