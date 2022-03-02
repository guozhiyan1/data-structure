class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def FindValue(self, root):
    if not root:
        return None
    d = []
    result = []
    result1 = []
    result2 = []
    d.append(root)
    while (len(d) != 0):
        for i in range(len(d)):
            r = d.pop()
            result1.append(r.val)
            result2.append(r.val)
            if r.left:
                d.append(r.left)
                result1.append(self.FindValue(r.left))
            if r.right:
                d.append(r.right)
                result2.append(self.FindValue(r.right))
    result.append(result1)
    result.append(result2)
    return result


if __name__ == '__main__':
    root=TreeNode(10,5,12,4,7)
    a=FindValue(root)
    print(root)
