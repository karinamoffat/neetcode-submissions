# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        IDEA: modified dfs or bfs to take in two nodes at a time,
        returning false if any two nodes are not the same for the given
        iteration. if the whole search completes then no false was hit,
        so return true.

        problem 1: returning False just breaks this iteration, not the whole
        recursive stack. we need a way to bubble this False all the way
        through the recursive call stack, therefore we have to store
        the value.
        '''
        
        false_tracker = []

        def dfs(p, q):
            if p is None and q is None:
                return True
            
            if (p is None) != (q is None):
                false_tracker.append(False)
                return False
            
            if p.val != q.val:
                false_tracker.append(False)
                return False
            
            dfs(p.left, q.left)
            dfs(p.right, q.right)
        
        dfs(q, p)
        if len(false_tracker) > 0:
            return False
        else:
            return True