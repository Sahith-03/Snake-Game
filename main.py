from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake game")
screen.tracer(0)

scoreboard = Scoreboard()

snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

food = Food()

game_is_on = True
food_colide = True
score = 0
coord = 0

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect Collision with food
    if snake.head.distance(food) < 15:
        scoreboard.refresh()
        food.refresh()
        snake.size_inc()

    #Collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            time.sleep(2)
            break

    #Detect Collision with Wall
    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor())>280:
        scoreboard.reset()
        snake.reset()
        time.sleep(2)
screen.exitonclick()