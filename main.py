import turtle as trt
import keyboard, time, pygame

pygame.init()  
drawer = trt.Turtle()
drawer.speed(0)

pepperoni_number = 10
cheese_number = 10
ingredient_in_hand = "cheese"

x = 0
y = -200



drawer.hideturtle()
drawer.write("PIZZA MAKER", align = "center", font=("Arial", 80, "normal"))
drawer.penup()

screen = trt.Screen()
screen.register_shape("Pizza-no-stuff.gif")

drawer.goto(x,y)
drawer.shape("Pizza-no-stuff.gif")
drawer.stamp()


player = trt.Turtle()
screen.register_shape("cheese.gif")
screen.register_shape("cheese_hand.gif")
screen.register_shape("pepperoni.gif")
screen.register_shape("pepperoni_hand.gif")


player.shape("cheese_hand.gif")
player.penup()
running = True
def stop():
    global running
    running = False
    exit()

while running:
    if keyboard.is_pressed("w"):
        y += 1
    if keyboard.is_pressed("s"):
        y -= 1
    if keyboard.is_pressed("a"):
        x -= 1
    if keyboard.is_pressed("d"):
        x += 1
    player.goto(x, y)
    if keyboard.is_pressed("c"):
        ingredient_in_hand = "cheese"
        player.shape("cheese_hand.gif")
    if keyboard.is_pressed("p"):
        ingredient_in_hand = "pepperoni"
        player.shape("pepperoni_hand.gif")
    if keyboard.is_pressed("space"):
        if (ingredient_in_hand == "cheese" and cheese_number > 0) or (ingredient_in_hand == "pepperoni" and pepperoni_number > 0):
            player.shape(ingredient_in_hand + ".gif")
            player.stamp()
            player.shape(ingredient_in_hand + "_hand.gif")
            if ingredient_in_hand == "pepperoni":
                pepperoni_number -= 1
            elif ingredient_in_hand == "cheese":
                cheese_number -= 1
            time.sleep(.2)



screen.mainloop()