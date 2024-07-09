from turtle import Turtle, Screen
import threading
import random

# Create turtles and screen
t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
screen = Screen()
t_wall = Turtle()
t_wall.color("white")
t_wall.pensize(35)
t_wall.speed("fastest")
t1.speed("fastest")
t2.speed("fastest")
t3.speed("fastest")
# Setup turtles and screen
t1.shape("square")
t2.shape("square")
t3.shape("square")
t1.color("white")
t2.color("white")
t3.color("white")
screen.bgcolor("black")
t1.penup()
t2.penup()
t3.penup()
t1.goto(0, 0)
t2.goto(-20, 0)
t3.goto(-40, 0)

# Initialize food and score
food = Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.speed(0)
food.goto(random.randint(-200, 200), random.randint(-200, 200))

score = 0

# Initialize snake segments
snake_segments = [t1, t2, t3]

def making_wall():
    global t_wall 
    t_wall.penup()
    t_wall.goto(-screen.window_width() / 2, screen.window_height() / 2)
    t_wall.pendown()
    for _ in range(2):
        t_wall.forward(screen.window_width())
        t_wall.right(90)
        t_wall.forward(screen.window_height())
        t_wall.right(90)
    t_wall.hideturtle()

# Call the function to draw the wall
making_wall()

# Function to display game over message
def game_over():
    screen.textinput("Game Over", f"Oh no! You hit the wall. Game Over. Your score was: {score}")

# Function to move snake left
def move_left():
    if t1.heading() != 0:  # Prevent turning directly back on itself
        t1.setheading(180)  # Point turtle 1 to the left
        move_snake()

# Function to move snake right
def move_right():
    if t1.heading() != 180:  # Prevent turning directly back on itself
        t1.setheading(0)  # Point turtle 1 to the right
        move_snake()

# Function to move snake up
def move_up():
    if t1.heading() != 270:  # Prevent turning directly back on itself
        t1.setheading(90)  # Point turtle 1 upwards
        move_snake()

# Function to move snake down
def move_down():
    if t1.heading() != 90:  # Prevent turning directly back on itself
        t1.setheading(270)  # Point turtle 1 downwards
        move_snake()

# Function to add a new segment to the snake
def add_segment():
    new_segment = Turtle()
    new_segment.penup()
    new_segment.shape("square")
    new_segment.color("white")
    snake_segments.append(new_segment)
    new_segment.speed("fastest")
# Function to move snake forward
def move_snake():
    global score

    # Move the snake as before
    for i in range(len(snake_segments) - 1, 0, -1):
        x = snake_segments[i - 1].xcor()
        y = snake_segments[i - 1].ycor()
        snake_segments[i].goto(x, y)
    t1.forward(20)

    # Check collision with food
    if t1.distance(food) < 20:
        score += 1
        move_food()
        add_segment()
        print(f"Score: {score}")  # Update score display (you can modify this to display on screen)

    # Check collision with wall for the head of the snake
    if t1.xcor() <= -screen.window_width() / 2 + 20 or t1.xcor() >= screen.window_width() / 2 - 20 or t1.ycor() <= -screen.window_height() / 2 + 20 or t1.ycor() >= screen.window_height() / 2 - 20:
        game_over()  # Call game over function
        screen.bye()  # Close the screen
        return

# Function to move food to a new random position
# Function to move food to a new random position
def move_food():
    while True:
        x = random.randint(int(-screen.window_width() / 2 + 20), int(screen.window_width() / 2 - 20))
        y = random.randint(int(-screen.window_height() / 2 + 20), int(screen.window_height() / 2 - 20))
        food.goto(x, y)

        # Check if food overlaps with any snake segment
        food_collision = False
        for segment in snake_segments:
            if food.distance(segment) < 20:
                food_collision = True
                break
        
        if not food_collision:
            break


# Setup screen listeners and key bindings
screen.listen()
screen.onkey(key="Left", fun=move_left)
screen.onkey(key="Right", fun=move_right)
screen.onkey(key="Up", fun=move_up)
screen.onkey(key="Down", fun=move_down)

# Function to continuously move the snake in a separate thread
def snake_movement():
    while True:
        move_snake()

# Create and start a thread for snake movement
snake_thread = threading.Thread(target=snake_movement)
snake_thread.start()

# Start the main loop
screen.mainloop()
