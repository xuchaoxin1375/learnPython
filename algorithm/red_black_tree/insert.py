from fixup import red_black_tree_fixup
RED="red"
def red_black_insert(T,z):
    """red_black_insert operation.
    we know that the new node to be inserted must will be inserted to the leaf node of bst(bst-like tree) 

    Args:
        T (tree): red_black_tree
        z (node): node to be inserted
    """
    leaf=T.nil #node leaf is initialized to T.nil
    x=T.root  # the x node is to auxiliary to find the leaf node
    while x!=T.nil:
        """ the leaf is the parent of the node x,if x get NIL,then the leaf is the leaf node """
        leaf=x
        """ iterate x go down the tree """
        if z.key<x.key:
            x=x.left
        else:
            x=x.right
    """ make the leaf node leaf as the inserted node z's parent """
    z.p=leaf
    """ if the origin tree is empty:leaf==T.nil """
    if leaf==T.nil:
        """ make the node z as the T.root """
        T.root=z
    # """ put the node z to the proper side of the leaf node leaf to maintain the bst property: """
    elif z.key<leaf.key:
        leaf.left=z
    else :
        leaf.right=z
    """ reset the new node's child(both=T.nil);and set the color of the node z  """
    z.left=T.nil 
    z.right=T.nil 
    z.color=RED
    """ to fixup the inserted but maybe not meet the propriety of red_black tree:(outsource the fixup operation) """
    red_black_tree_fixup(T,z)