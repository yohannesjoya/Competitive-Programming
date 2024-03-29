# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        queue = deque()
        queue.append(root)
        
        answer = []
        
        while queue:
            
            n = len(queue)
            
            pos = queue.popleft()
            answer.append(pos.val)
            if pos.left:
                    queue.append(pos.left)
            if pos.right:
                    queue.append(pos.right)
        
            
            for i in range(n-1):
                
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return answer[-1]