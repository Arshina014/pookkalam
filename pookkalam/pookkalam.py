import turtle, math, os
turtle.tracer(0,0)

# ---------------- Setup ----------------
screen = turtle.Screen()
screen.setup(1000, 1000)
screen.bgcolor("white")
screen.title("Pookkalam")


print("Files in current folder:", os.listdir())

# Register GIFs
motifs = ["vallamkali.gif", "deepam.gif"]
for m in motifs:
    if m in os.listdir():
        screen.register_shape(m)
    else:
        print(f"⚠ File {m} not found in folder")

# ---------------- Utilities ----------------
def draw_circle(radius, color):
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.goto(0, -radius)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def dotted_ring(radius, count, colors, size=15):
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()
    for i in range(count):
        angle = 2 * math.pi * i / count
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        t.goto(x, y)
        t.dot(size, colors[i % len(colors)])

def jasmine_ring(radius, count):
    dotted_ring(radius, count, ["white"], size=10)

def red_ring(radius, count):
    dotted_ring(radius, count, ["red","darkred"], size=13)    

def lotus_flower(x, y, size=15, petals=24, color="#A70404"):
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.goto(x, y - size/2)
    t.pendown()
    for _ in range(petals):
        t.fillcolor(color)
        t.begin_fill()
        t.circle(size, 60)
        t.left(120)
        t.circle(size, 60)
        t.end_fill()
        t.left(360 / petals)

def flower(x, y, size=15, petals=24, color="#d11e1e"):
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.goto(x, y - size/2)
    t.pendown()
    for _ in range(petals):
        t.fillcolor(color)
        t.begin_fill()
        t.circle(size, 60)
        t.left(120)
        t.circle(size, 60)
        t.end_fill()
        t.left(360 / petals)        

def lotus_ring(radius, count):
    for i in range(count):
        angle = 2 * math.pi * i / count
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        lotus_flower(x, y, size=20)

def flower_ring(radius, count, color="red"):
    for i in range(count):
        angle = 2 * math.pi * i / count
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        flower(x, y, size=15, color=color)

def flower_ring_alternate(radius, count):
    colors = ["red", "dark red"]
    for i in range(count):
        angle = 2 * math.pi * i / count
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        flower(x, y, size=15, color=colors[i % 2])

def leaf_ring(radius, count):
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    for i in range(count):
        angle = 360 / count * i
        t.penup()
        t.goto(0, 0)
        t.setheading(angle)
        t.forward(radius)
        t.pendown()
        t.fillcolor("forest green")
        t.begin_fill()
        t.circle(30, 60)
        t.left(120)
        t.circle(30, 60)
        t.end_fill()

def place_in_circle(shape, radius, count, scale=0.7):
    if shape not in screen.getshapes():
        print(f"⚠ Shape {shape} not registered, skipping.")
        return
    t = turtle.Turtle()
    t.hideturtle()
    t.shape(shape)
    t.penup()
    for i in range(count):
        angle = 2 * math.pi * i / count
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        t.goto(x, y)
        t.shapesize(scale, scale)
        t.stamp()

def place_center(shape, scale=3.0):
    if shape not in screen.getshapes():
        print(f"⚠ Shape {shape} not registered, skipping.")
        return
    t = turtle.Turtle()
    t.hideturtle()
    t.shape(shape)
    t.shapesize(scale, scale)
    t.stamp()

# ---------- Square Flower Layer ----------
def square_flower(side=250, count=12, colors=("gold", "yellow")):
    """Large overlapping squares around center."""
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    for i in range(count):
        angle = (360 / count) * i + 60
        t.penup()
        t.goto(0,0)
        t.setheading(angle)
        t.pendown()
        t.fillcolor(colors[i % 2])
        t.begin_fill()
        for _ in range(4):
            t.forward(side)
            t.left(90)
        t.end_fill()

# ---------- Gopuram Spires (elongated cones) ----------
def gopuram_ring(radius, count, color1="#E6AA2B", color2="#D1170A"):

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    for i in range(count):
        angle = 360 / count * i
        t.penup()
        t.goto(0, 0)
        t.setheading(angle)
        t.forward(radius)
        t.pendown()
        color = color1 if i % 2 == 0 else color2
        t.fillcolor(color)
        t.begin_fill()
        t.left(120)
        t.forward(20)    # base half
        t.right(150)
        t.forward(80)    # tall height
        t.right(60)
        t.forward(80)    # tall height
        t.right(150)
        t.forward(20)    # base half
        t.end_fill()

# ---------------- Design ----------------
def draw_pookkalam():
    # Base circles
    draw_circle(425, "yellow")
    draw_circle(370, "orange")
    
    leaf_ring(430, 125)
    leaf_ring(355, 125)
    
    dotted_ring(384, 140, ["orange", "dark orange"], size=18)
    jasmine_ring(372, 220)
    red_ring(410, 190)

    square_flower(side=260, count=16, colors=("#f7e335", "#e96519"))

    
    gopuram_ring(190, 30)

    # Gold base circle above squares
    draw_circle(220, "gold")

    lotus_ring(200, 45)
    lotus_ring(420, 90)
    
    flower_ring_alternate(220, 60)

    

    # Extra flower ring
    flower_ring(397, 90, color="#ff3d0c")



    # Vallamkali center motif
    place_center("vallamkali.gif", scale=2.0)

    # Deepam ring
    place_in_circle("deepam.gif", 500, 18, scale=1)
    place_in_circle("deepam.gif", 340, 16, scale=1)


# ---------------- Run ----------------
draw_pookkalam()
turtle.update()
turtle.done()