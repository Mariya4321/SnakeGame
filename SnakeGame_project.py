from turtle import Screen
import time
from snake import Snake
from Food import Food
from scoreboard import ScoreBoard

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
game_score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(snake.speed)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        game_score.score_inc()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_score.reset()
        snake.reset()

    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            game_score.reset()
            snake.reset()

screen.exitonclick()
