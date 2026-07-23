# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        IDEA
        Lowest refers to height, not value. Maybe we can incorporate depth into this?
        Problem 1) even if we determine which node has the largest depth, we still don't know if it is a common
        ancestor? First problem is determining the valid ancestors.
        An ancestor is determined by the parent-child nodes only. It must be reachable without backtracking.
        
        let's go with the simplest solution I can think of right now:
        1. find the ancestors of the current node by continuing to go left or right depending on if the current node
        value is greater than or less than the current node. 
        ie looking for node '9', at every node we ask is node.val == '9'? yes, stop. is node.val > '9'? yes, node = node.right.
        is node.val < '9'? yes, node = node.left. add each node to the list until node.val == '9'.
        2. do the exact same for the other node.
        3. now you have two lists: p_ancestors and q_ancestors.
        4. sort both lists. iterate through each until you reach the end of the longest list.

        logic: once you have the two ancestors list, the common ancestor with the highest index is the lowest common ancestor.
        let's store ancestors as a map, where the node.val is the key and the depth is the value

        then, we can put the values of the common keys in structure and return the highest value (because that is the lowest
        common ancestor)

        the real logic:
        use depth first search. 
        search for both targets simultaneously
        at the node in which the algorithm diverges (to find t1 you go left, to find t2 you go right)
        this is the LCA
        
        dfs calls left before right (for pre-order)
        so the node that the algorithm calls left for one target and right for the other is the LCA
        '''

        q_left, q_right, p_left, p_right = 0,0,0,0
        if root.val == q.val or root.val == p.val:
            return root
        
        if root.val > q.val:
            q_left = 1
        else:
            q_right = 1
        
        if root.val > p.val:
            p_left = 1
        else:
            p_right = 1

        print(f"for {root.val}, q_left is {q_left}, q_right is {q_right}, p_left is {p_left}, and p_right is {p_right}. \n")

        if (q_left and p_right) or (q_right and p_left):
            return root
        
        elif q_right and p_right:
            return self.lowestCommonAncestor(root.right, p, q)
        
        else:
            return self.lowestCommonAncestor(root.left, p, q)
        
            

        # 5, 8, 7
        # 5, 3, 1, 2
        

        
