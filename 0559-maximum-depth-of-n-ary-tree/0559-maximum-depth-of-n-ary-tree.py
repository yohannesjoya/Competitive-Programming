"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
            def height(node):
                if not node:
                    return 0
                if not node.children:
                    return 1
                mxx = float('-inf')
                for child in node.children:
                    mxx = max(mxx,height(child))
                return mxx+1

            return height(root)