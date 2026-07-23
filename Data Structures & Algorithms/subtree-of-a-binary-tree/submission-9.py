# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(q, p) -> bool:
            if q is None and p is None:
                return True
            if q is None or p is None:
                return False
            if q.val != p.val:
                return False

            return (isSameTree(q.left, p.left) and isSameTree(q.right, p.right))
        
        # dfs should recurse the tree, going through each node
        # until the root value matches the subroot value
        def dfs(root, subRoot) -> bool:
            if root is None:
                return False

            return (isSameTree(root, subRoot) or dfs(root.left, subRoot) or dfs(root.right, subRoot))


        return dfs(root, subRoot)