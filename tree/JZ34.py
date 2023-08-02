#二叉树中和为某一值的路径(二)
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import copy
class Solution:
    def __init__(self):
        self.node=[]
        self.result=[]
    def FindPath(self , root: TreeNode, target: int) -> List[List[int]]:
        # write code here
        if not root:
            return None
        d=[]
        d.append(root)
        while len(d)!=0:
            for i in range(len(d)):
                node=d.pop()
                self.node.append(node.val)
                if node.left:
                    self.FindPath(node.left, target-node.val)
                if node.right:
                    self.FindPath(node.right, target-node.val)
                if not node.left and not node.right:
                    if node.val==target:
                        self.result.append(copy.deepcopy(self.node))
                        self.node.pop()
                        return self.result
                self.node.pop()
            return self.result


class Solution1:
    def FindPath(self, root: TreeNode, target: int) -> list:
        # write code here
        self.final, self.f = [], []  # 存放所有路径以及当前路径
        self.find_root(root)
        return [a for a in self.final if sum(a) == target]  # 找出和刚好为target的列表

    def find_root(self, node):  # 找出所有到叶子节点的路径
        if not node:
            return
        self.f.append(node.val)
        self.find_root(node.left)
        self.find_root(node.right)
        if not node.left and not node.right:
            self.final.append(self.f.copy())
        self.f.pop()
