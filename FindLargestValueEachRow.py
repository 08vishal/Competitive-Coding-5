#Time Complexity=O(n)
#Space Complexity=O(n)
#Leetcode submission:successful

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root :
            return []
        result=[]
        #result.append(root.val)
        q=[]
        large=-float("inf")
        q.append(root)
        while(len(q)>0):
            result.append(max(x.val for x in q))
            size=len(q)
            for i in range(size):
                curr=q.pop(0)
                
                if curr.left:
                    #large=max(large,curr.left.val)
                    q.append(curr.left)
                if curr.right:
                    #large=max(large,curr.right.val)
                    q.append(curr.right)
            #result.append(large)
            
        return result
                