##
import turtle
##
binTree = turtle.Turtle()
my_win = turtle.Screen()
def draw_tree(branch_length, t): 
    if branch_length > 2: 
        t.forward(branch_length)
        t.right(20)
        draw_tree(branch_length-20, t) 
        t.left(40) 
        draw_tree(branch_length-20, t) 
        t.right(20) 
        t.backward(branch_length)
binTree.left(90)
binTree.up() # 抬起尾巴
binTree.backward(200)
binTree.down() # 放下尾巴
binTree.color('green')
draw_tree(100, binTree)
my_win.exitonclick()
##
