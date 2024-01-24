from turtle import Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard

import time
screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    if snake.head.distance(food) < 15:
        food.refresh()
        score.refresh()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.gameover()
        is_on = False

    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            is_on = False
            score.gameover()
screen.exitonclick()
