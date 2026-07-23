"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        mapping = {}
        max_area = 0

        def dfs(node):
            if node is None:
                return node

            if node in mapping:
                return mapping[node]
            
            clone = Node(val = node.val)
            mapping[node] = clone

            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return mapping[node]
            
        '''for neighbor in node.neighbors:
            if neighbor.val not in visited:
                print(f"next node is: {neighbor.val}")
                dfs(neighbor, clone)'''

        return dfs(node)

        
