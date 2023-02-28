# Import libraries
import turtle
import time
import random

# Build game screen
wn = turtle.Screen()
wn.title("TETRIS by Further programming Group 20")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# Delay Game progress
delay = 0.25

class Shape():
    def __init__(self):
        self.x = 5
        self.y = 0
        self.color = random.randint(1, 7)
        
        # Block Shapes
        square = [[1,1],
                  [1,1]]
        # Horizontal ine shape
        horizontal_line = [[1,1,1,1]]
        # Vertical line shape
        vertical_line = [[1],
                         [1],
                         [1],
                         [1]]
        # Left line shape
        left_l = [[1,0,0,0],
                  [1,1,1,1]]
        # Right line shape
        right_l = [[0,0,0,1],
                   [1,1,1,1]]
        # Z-shape
        left_s = [[1,1,0],
                  [0,1,1]]
        # Inverted z-shape
        right_s = [[0,1,1],
                   [1,1,0]]
        #t-shape
        t = [[0,1,0],
             [1,1,1]]
        # list of shapes
        shapes = [square, horizontal_line, vertical_line, left_l, right_l, left_s, right_s, t]

        # Choose a random shape each time
        self.shape = random.choice(shapes)

                      
        self.height = len(self.shape)
        self.width = len(self.shape[0])
        
    # move shape across grid
    def move_left(self, grid):
        if self.x > 0:
            if grid[self.y][self.x - 1] == 0:
                self.erase_shape(grid)
                self.x -= 1
    # Drop shape in the middle
    def move_right(self, grid):
        if self.x < 12 - self.width:
            if grid[self.y][self.x + self.width] == 0:
                self.erase_shape(grid)
                self.x += 1
    # Fill shape within grid
    def draw_shape(self, grid):
        for y in range(self.height):
            for x in range(self.width):
                if(self.shape[y][x]==1):
                    grid[self.y + y][self.x + x] = self.color
    # Erase hosizontalline when full
    def erase_shape(self, grid):
        for y in range(self.height):
            for x in range(self.width):
                if(self.shape[y][x]==1):
                    grid[self.y + y][self.x + x] = 0
    # Make shape move around
    def can_move(self, grid):
        result = True
        for x in range(self.width):
            # Check if bottom is a 1
            if(self.shape[self.height-1][x] == 1):
                if(grid[self.y + self.height][self.x + x] != 0):
                    result = False
        return result
    # Make shape rotate
    def rotate(self, grid):

        # First erase_shape
        self.erase_shape(grid)
        rotated_shape = []
        for x in range(len(self.shape[0])):
            new_row = []
            for y in range(len(self.shape)-1, -1, -1):
                new_row.append(self.shape[y][x])
            rotated_shape.append(new_row)
        
        right_side = self.x + len(rotated_shape[0])
        if right_side < len(grid[0]):     
            self.shape = rotated_shape

            # Update the height and width
            self.height = len(self.shape)
            self.width = len(self.shape[0])
         
# Create Game Grid
grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Create the drawing pen
pen = turtle.Turtle()
pen.penup()
pen.speed(0)
pen.shape("square")
pen.setundobuffer(None)

def draw_grid(pen, grid):
    pen.clear()
    top = 230
    left = -110
    # Create list of shape colours
    colors = ["gray", "lightblue", "blue", "orange", "yellow", "green", "purple", "red"]
    
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            screen_x = left + (x * 20)
            screen_y = top - (y * 20)
            color_number = grid[y][x]
            color = colors[color_number]
            pen.color(color)
            pen.goto(screen_x, screen_y)
            pen.stamp()


def check_grid(grid):
    # Check if each row is full
    y = 23
    while y > 0:
        is_full = True
        for x in range(0, 12):
            if grid[y][x] == 0:
                is_full = False
                y -= 1
                break
        if is_full:
            global score
            score += 10
            draw_score(pen, score)
            for copy_y in range(y, 0, -1):
                for copy_x in range(0, 12):
                    grid[copy_y][copy_x] = grid[copy_y-1][copy_x]

def draw_score(pen, score):
    pen.color("blue")
    pen.hideturtle()
    pen.goto(-75, 350)
    pen.write("Score: {}".format(score), move=False, align="left", font=("Arial", 24, "normal"))
    
# Create the basic shape for the start of the game
shape = Shape()

# Put the shape in the grid
grid[shape.y][shape.x] = shape.color

wn.listen()
# To Move left
wn.onkeypress(lambda: shape.move_left(grid), "c")
# To Move right
wn.onkeypress(lambda: shape.move_right(grid), "b")
# To Rotate
wn.onkeypress(lambda: shape.rotate(grid), "space")

# Set the score to 0
score = 0

draw_score(pen, score)

# Main game loop
while True:
    wn.update()

    # Move the shape
    # Open Row
    # Check for the bottom
    if shape.y == 23 - shape.height + 1:
        shape = Shape()
        check_grid(grid)
    # Check for collision with next row
    elif shape.can_move(grid):
        # Erase the current shape
        shape.erase_shape(grid)
        
        # Move the shape by 1
        shape.y +=1
        
        # Draw the shape again
        shape.draw_shape(grid)

    else:
        shape = Shape()
        check_grid(grid)
        
    # Draw the screen
    draw_grid(pen, grid)
    draw_score(pen, score)
    
    time.sleep(delay)
    
wn.mainloop()
