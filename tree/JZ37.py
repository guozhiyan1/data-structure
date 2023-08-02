class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 前序遍历
    def Serialize(self, root):
        # write code here
        list = []

        def test1(root):
            if not root:
                list.append("#")
            else:
                list.append(root.val)
                test1(root.left)
                test1(root.right)

        test1(root)
        s = ','.join('%s' % id for id in list)
        return s

    def Deserialize(self, s):
        # write code here
        vals = iter(s.split(","))

        def test2():

            val = next(vals)
            if val == "#":
                return None
            else:
                root = TreeNode(int(val))
                root.left = test2()
                root.right = test2()
            return root

        return test2()