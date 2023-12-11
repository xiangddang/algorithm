def balancedTree(root):
    if not root:
        return True
    
    def height(root):
        if not root:
            return 0
        return max(height(root.left), height(root.right)) + 1
    
    if abs(height(root.left) - height(root.right)) > 1:
        return False
    
    return balancedTree(root.left) and balancedTree(root.right)
    

    