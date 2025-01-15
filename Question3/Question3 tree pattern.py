import turtle

# use recursive function to generate a tree pattern
def draw_tree(t, branch_length, left_angle, right_angle, depth, reduction_factor):
    # Base condition: if depth is 0, stop drawing
    if depth == 0:
        return
    
    # main branch color is red and line thickness is 5
    if depth == 5:  
        t.pencolor("red")  
        t.pensize(5)  
    # green is the colour for second and third branch and line thickness is 4 and green is colour for the rest of the branch and line thickness is 2
    elif depth == 4:  
        t.pencolor("green")  
        t.pensize(4)  
    else:  
        t.pencolor("green")  
        t.pensize(2) 
    
    # draw the current branch and move the the turtle forward to draw it
    t.forward(branch_length)  

    # draw the left sub-branch and turn the turtle left by certain angle
    t.left(left_angle)  
    draw_tree(t, branch_length * reduction_factor, left_angle, right_angle, depth - 1, reduction_factor)

    # draw the right sub-branch and turn the turtle right by sum of the angle
    t.right(left_angle + right_angle)  
    draw_tree(t, branch_length * reduction_factor, left_angle, right_angle, depth - 1, reduction_factor)

    # return to the original angle after drawing right branch
    t.left(right_angle)  
    
    # draw the other branch and move the turtle back to the original position 
    t.backward(branch_length)  # Move the turtle backward by the length of the branch

# main function to set parameters for the tree, including branch angles, starting length, depth, and branch length reduction
def main():
    # parameters for the tree
    left_angle = 20  
    right_angle = 25  
    starting_length = 100  
    depth = 5  
    reduction_factor = 0.7  

    # code to set up turtle and screen, with the turtle facing upwards and moving to the fastest speed
    t = turtle.Turtle()  
    screen = turtle.Screen()  
    screen.bgcolor("white")  
    t.left(90)  
    t.speed(0)  

    # lift the turtle pen to avoid drawing while moving to initial position at the bottom centre of the screen and then the pen down to start drawing
    t.penup()  
    t.setpos(0, -200)  
    t.pendown()  
    # call the recursive function to draw tree
    draw_tree(t, starting_length, left_angle, right_angle, depth, reduction_factor)

    # hide turtle after finish the drawing
    t.hideturtle()

    # finish the drawing and keep the window open until closed by the user
    turtle.done()

# run the program
if __name__ == "__main__":
    main()

