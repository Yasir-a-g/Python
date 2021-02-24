from turtle import Screen
from snake import Snake
from food import Food
from Score_board import Scoreboard
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("my Snake Game")
screen.tracer(0)
# square_1 = Turtle(shape="square")
# square_1.color("white")
#
# square_2 = Turtle(shape="square")
# square_2.color("white")
# square_2.goto(-20, 0)
# square_3 = Turtle(shape="square")
# square_3.color("white")
# square_3.goto(-40, 0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up ,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right , "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    snake.move()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
    for segment in snake.segments[1: ]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            game_is_on = False
            Scoreboard.game_over()
"""  

"""

screen.exitonclick()


