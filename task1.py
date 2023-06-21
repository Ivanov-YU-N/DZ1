class RBTree(object):
    def __init__(self):
        self.nil = RBTreeNode(0)
        self.root = self.null
class RBTreeNode(object):
    def __init__(self, x):
        self.velue = x
        self.left = None
        self.right = None
        self.parent = None
        self.color = 'black'
        self.size=None

    def LeftRotate(T, x):
        y = x.right
        x.right = y.left  
        if y.left != T.null:
            y.left.parent = x  
        y.parent = x.parent  
        if x.parent == T.null: 
            T.root = y      
        elif x == x.parent.left:  
            x.parent.left = y  
        else:
            x.parent.right = y  
        y.left = x   
        x.parent = y  
    def RightRotate(T, y):
        x = y.left
        y.left = x.right  
        if x.right != T.null: 
            x.right.parent = y 
        x.parent = y.parent  
        if y.parent == T.null:
            T.root = x    
        elif y == y.parent.right:
            y.parent.right = x   
        else:
            y.parent.left = x   
        x.right = y  
        y.parent = x 

