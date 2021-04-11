'''
Description: 
Version: 2.0
Author: xuchaoxin
Date: 2021-04-10 09:45:22
LastEditors: xuchaoxin
LastEditTime: 2021-04-10 11:34:17
'''
""" LEFT-ROTATE.T; x/
1 y D x:right //set y
2 x:right D y:left //turn y’s left subtree into x’s right subtree
3 if y:left ¤ T:nil
4 y:left:p D x
5 y:p D x:p //link x’s parent to y
6 if x:p == T:nil
7 T:root D y
8 elseif x == x:p:left
9 x:p:left D y
10 else x:p:right D y
11 y:left D x //put x on y’s left
12 x:p D y """
def right_rotate(T,x):
    pass
def left_rotate(T,x):
    """[summary]

    Args:
        T (tree): [description]
        x (node): [description]
    """    
    """ this is a bidirectional process:parent recognize its child,and its child recognize its parent! """
    """ there the y is a pointer of a node (it could be initialized to null) """
    y=x.right #make the y pointer hook the node which is x.right node
    x.right=y.left
    
    if y.left != T.nil:
        """ y.left as a child to recognize its new parent node x """
        y.left.p=x
    """ make y as a child to recognize its new parent:x.p
    (link x's parent to y)"""
    y.p=x.p
    """ then we should set the node y as the correct side(left/right) child of its new parent(x.p);or,make y as the T.root """
    """ if x is the T.root(be equivalent to x.p==T.nil) """
    if x.p==T.nil:
        """ make the y as T.root node """
        T.root=y
    # """ elif the x is the left child of its parent: """
    elif x==x.p.left:
        """then set the y as the left child of its new parent(x.p)"""
        x.p.left=y
    else:
        """ then set the y as the right child of its new parent(x.p)"""
        x.p.right=y
    y.left=x
    x.p=y

    