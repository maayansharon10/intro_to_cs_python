# import the turtle module.
import turtle

# the aim of this program is to draw 3 flowers.

def draw_petal():
    """ to draw a single petal I define a function draw_petal() """
    turtle.circle(100, 90)
    turtle.left(90)
    turtle.circle(100, 90)
    return


def draw_flower():
    """ in order to draw a single flower I define draw_flower() in which I use
    draw_petal() a few times in different directions:"""
    turtle.setheading(0)
    draw_petal()
    turtle.setheading(90)
    draw_petal()
    turtle.setheading(180)
    draw_petal()
    turtle.setheading(270)
    draw_petal()
    turtle.setheading(270)
    turtle.forward(250)
    return


def draw_flower_advance():
    """ #drawing a flower and moving the turtle head in order to allow more
    flowers' drowing one next to the other i define draw_flower_advance() """
    draw_flower()
    turtle.right(90)
    turtle.up()
    turtle.forward(250)
    turtle.right(90)
    turtle.forward(250)
    turtle.left(90)
    turtle.down()
    return

def draw_flower_bed():
    """ in order to draw 3 different flowers I define draw_flower_bed() """
    turtle.up()
    turtle.forward(200)
    turtle.left(180)
    turtle.down()
    draw_flower_advance()
    draw_flower_advance()
    draw_flower_advance()
    return



if __name__ == "__main__":
    draw_flower_bed()

# required when done with using turtle module .
turtle.done
