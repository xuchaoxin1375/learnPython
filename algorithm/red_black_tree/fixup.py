'''
Description: 
Version: 2.0
Author: xuchaoxin
Date: 2021-04-10 11:04:55
LastEditors: xuchaoxin
LastEditTime: 2021-04-10 13:06:52
'''
from rotation import * 
RED="red"
BLACK="black"
def red_black_tree_fixup(T, z):
    """[fixup the rb tree]

    Args:
        T (tree): [red_black_tree]
        z (node): the node to be insert to the RB tree
    """    
    """ when the z.p.color=red,then over the fixup process """
    while z.p.color==RED:
        """ if the z.p is the left child of its parent:"""
        if z.p==z.p.p.left:
            """ make the y pointer link to the z.p.p.right as the uncle of the z"""
            y=z.p.p.right #z's uncle node
            # todo comprare:
            """ according the uncle node's(y) color to classify three cases: """
            if y.color==RED:
                """ change the color of z's parent and uncle's color:"""
                z.p.color=BLACK
                y.color=BLACK
                """ meanwhile change the color of z's grandparent:(in this case,the grandparent of z must be black,because the RB tree's properties"""
                z.p.p.color=RED
                """ iterate the be inserted node :make the z's grandparent as the new violate node(if not lucky),well,then 
                we repeat the similar process by the while loop"""
                z=z.p.p
            # """ z's uncle(y) is black: """
            else:
                # """ case 2:
                # make case2 to case3: """
                if z==z.p.right:
                    """ the z is the right child of its parent: that pointer z to point old z's parent
                    this is to make rotation operation:"""
                    z=z.p
                    left_rotate(T,z)
                # """ case3: """
                elif z==z.p.left:
                    pass
                    """ the case3,it could be handle directly by the
                    following statements out of the judge code segment:"""
                
                """ change the color of the z.p and z.p.p """
                z.p.color=BLACK
                z.p.p.color=RED
                right_rotate(T,z.p.p)
        else:
            """ z.p==z.p.p.right """
            """ the same then clause with 'right' and 'left' exchanged"""
            pass

                
    