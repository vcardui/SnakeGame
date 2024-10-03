from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.segments[0].distance(food) < 15:
        print("The food was delicious")
        food.refresh()
        snake.grow()
        scoreboard.score += 1
        scoreboard.update_scoreboard()

    # Detect collision with wall
    if 280 < snake.segments[0].xcor() or snake.segments[0].xcor() < -280 or 280 < snake.segments[0].ycor() or snake.segments[0].ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with itself
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            scoreboard.reset()
            scoreboard.score = 0
            snake.reset()


screen.exitonclick()
