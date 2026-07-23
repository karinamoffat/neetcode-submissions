# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        
        while stack:
            curr = stack.pop()
            if not curr ==None:
                temp_left, temp_right = None, None

                if curr.left:
                    temp_left = curr.left
                if curr.right:
                    temp_right = curr.right

                curr.left = temp_right
                curr.right = temp_left

                if not curr.right == None:
                    stack.append(curr.right)

                if not curr.left==None:
                    stack.append(curr.left)
            
                  
        return root


            
