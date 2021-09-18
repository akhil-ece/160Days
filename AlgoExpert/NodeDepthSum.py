# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def nodeDepths(root):
    depth = 0
    stack = [{"node" : root, "depth" : 0}]
    while len(stack) > 0:
        poppedNode = stack.pop()
        node, NodeDepth = poppedNode["node"], poppedNode["depth"]
        if node is None:
            continue
        depth += NodeDepth

        stack.append({"node" : node.left, "depth" : depth + 1})
        stack.append({"node": node.right, "depth": depth + 1})

    return depth

	

def nodeDepths(root, depth = 0):
    if(root) is None:
        return 0
	return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)





