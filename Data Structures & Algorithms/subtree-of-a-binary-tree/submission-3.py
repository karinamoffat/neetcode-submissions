# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
        IDEA:
        similar in Same Binary Tree but this time instead of checking
        nodes, we need to begin the check once we land on the identified
        subroot. Once that subroot is identified we can take this as a
        new tree and use the Same Binary Tree logic against this portion.

        1. Locate the subtree node
        2. call isSameTree
        '''

        # assume the subtree does not exist in the tree until proven 
        # otherwise
        def isSameTree(q, p) -> bool:
            if q is None and p is None:
                return True
            if q is None or p is None:
                return False
            if q.val != p.val:
                return False

            left_result = isSameTree(q.left, p.left)
            right_result = isSameTree(q.right, p.right)
            return left_result and right_result
        
        # dfs should recurse the tree, going through each node
        # until the root value matches the subroot value
        def dfs(root, subRoot) -> bool:
            if root is None:
                return False
            
            result = False
            if root.val == subRoot.val:
                result = isSameTree(root, subRoot)

            result_left = dfs(root.left, subRoot)
            result_right = dfs(root.right, subRoot)

            return result or result_left or result_right


        return dfs(root, subRoot)