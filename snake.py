from turtle import Turtle

STARTING_POSITIONS = [(0,0) , (-20,0) , (-40,0)]
MOVE_DISTANCE = 20
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for positions in STARTING_POSITIONS:
            s = Turtle()
            s.pensize(20)
            s.color("white")
            s.shape("square")
            s.penup()
            s.goto(positions)
            self.segments.append(s)


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        ang = self.segments[0].heading()
        if ang == 0 or ang == 180:
            self.segments[0].setheading(90)

    def down(self):
        ang = self.segments[0].heading()
        if ang == 0 or ang == 180:
            self.segments[0].setheading(270)

    def left(self):
        ang = self.segments[0].heading()
        if ang == 90 or ang == 270:
            self.segments[0].setheading(180)

    def right(self):
        ang = self.segments[0].heading()
        if ang == 90 or ang == 270:
            self.segments[0].setheading(0)

    def position(self):
        return(self.segments[0].pos())

    def size_inc(self):
        s = Turtle()
        s.pensize(20)
        s.color("white")
        s.shape("square")
        s.penup()
        s.goto(self.segments[-1].position())
        self.segments.append(s)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
