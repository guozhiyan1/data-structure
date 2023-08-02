class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.mid = []

    def isSymmetrical(self, pRoot: TreeNode) -> bool:
        # write code here
        if not pRoot:
            return True
        if pRoot.left and pRoot.right and pRoot.left.val != pRoot.right.val:
            return False
        self.MidSort(pRoot)
        if len(self.mid) % 2 == 0:
            return False
        for i in range(len(self.mid) // 2):
            if self.mid[i] != self.mid[len(self.mid) - 1 - i]:
                return False
        return True

    def MidSort(self, pRoot):
        if pRoot.left and pRoot.right:
            if pRoot.left:
                self.MidSort(pRoot.left)
            self.mid.append(pRoot.val)
            if pRoot.right:
                self.MidSort(pRoot.right)
        elif not pRoot.left and not pRoot.right:
            self.mid.append(pRoot.val)
        elif pRoot.left:
            self.MidSort(pRoot.left)
            self.mid.append(pRoot.val)
        elif pRoot.right:
            self.mid.append(pRoot.val)
            self.MidSort(pRoot.right)

class Solution1:
    def isSymmetrical(self , pRoot: TreeNode) -> bool:
        # write code here
        if not pRoot:
            return True
        return self.isBalance(pRoot.left,pRoot.right)
    def isBalance(self,pRoot1,pRoot2):
        if pRoot1==None and pRoot2!=None:
            return False
        if pRoot2==None and pRoot1!=None:
            return False
        if pRoot2==None and pRoot1==None:
            return True
        if pRoot1.val!=pRoot2.val:
            return False
        return self.isBalance(pRoot1.left,pRoot2.right) and self.isBalance(pRoot1.right,pRoot2.left)

