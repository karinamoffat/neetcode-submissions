# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

            
        visible_nodes = []

        queue = [root]

        while queue:
            level_length = len(queue)

            to_add = queue[level_length - 1] # get the right most node in this level
            visible_nodes.append(to_add.val)

            for _ in range(level_length):
                curr = queue.pop(0)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                
        return visible_nodes

            

