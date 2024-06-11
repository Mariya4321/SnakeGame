from turtle import *

starting_position = [(0, 0), (-20, 0), (-40, 0)]
move_forward = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segment = []
        self.Create_snake()
        self.head = self.segment[0]
        self.speed = 0.1

    def Create_snake(self):
        for positions in starting_position:
            self.add_segment(positions)

    def add_segment(self, position):
        timmy = Turtle("square")
        timmy.penup()
        timmy.color("white")
        timmy.goto(position)
        self.segment.append(timmy)

    def extend(self):
        self.add_segment(self.segment[-1].position())
        self.speed *= 0.9

    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)

        self.head.forward(move_forward)

    def reset(self):
        for seg in self.segment:
            seg.goto(1000, 1000)
        self.segment.clear()
        self.Create_snake()
        self.head = self.segment[0]
        self.speed = 0.1

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


