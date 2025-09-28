from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: Optional[TreeNode]) -> int:
    """
    Compute the maximum depth (height) of a binary tree.

    Args:
        root (TreeNode | None): The root node of the tree

    Returns:
        int: The maximum depth of the tree
    """
    if not root:
        return 0
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    return 1 + max(left_depth, right_depth)


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Find the lowest common ancestor (LCA) of two nodes in a Binary Search Tree.

    Args:
        root (TreeNode): Root of the BST
        p (TreeNode): First node
        q (TreeNode): Second node

    Returns:
        TreeNode: The LCA node
    """
    # Because it's a BST, we can use node values to decide where to go
    current = root
    while current:
        if p.val < current.val and q.val < current.val:
            current = current.left
        elif p.val > current.val and q.val > current.val:
            current = current.right
        else:
            # We are either split between left/right OR one matches current
            return current
