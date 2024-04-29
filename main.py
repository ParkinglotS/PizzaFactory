#imports
import turtle as trt
import keyboard, time, pygame, random
"""
Title: PizzaFactory
Author: Parker Szymczak
Date: 4/28/24
Code version: 9.0
Availability: https://github.com/ParkinglotS/PizzaFactory.git
"""

#pygame used only for music
pygame.init()  

#creating the drawer turtle
drawer = trt.Turtle()
drawer.hideturtle()
drawer.penup()
drawer.speed(0)

#variables for knowing how many ingredients you can place and which ingredient is in your hand
pepperoni_number = 10
cheese_number = 10
ingredient_in_hand = "cheese"

#randomizing the customer's order
customertime = random.randint(5, 15)
customercheese = random.randint(0, 10)
customerpepperoni = random.randint(0, 10)
if customerpepperoni == 0 and customercheese == 0:
    customercheese += 1

#setting variables to defaults
success = True
x = 0
y = -200
screen = trt.Screen()
cheese_stamps_x = []
cheese_stamps_y = []
pepperoni_stamps_x = []
pepperoni_stamps_y = []

#creating the customer turtle and setting its shape/sprite
customer = trt.Turtle()
customer.speed(0)
customer.penup()
screen.register_shape("customer1.gif")
screen.register_shape("customer1talking.gif")
customer.goto(0, -100)
customer.shape("customer1.gif")

#creating the writer turtle
writer = trt.Turtle()
writer.speed(0)
writer.penup()
writer.hideturtle()

#registering the shape for the drawer (turtle is weird, you have to register shapes in a certain order)
screen.register_shape("Pizza-no-stuff.gif")

#drawing the pizza base
drawer.goto(x,y)
drawer.shape("Pizza-no-stuff.gif")
drawer.stamp()

#creating the player turtle
player = trt.Turtle()
player.speed(0)
player.penup()

#registering lots of shapes
screen.register_shape("cheese.gif")
screen.register_shape("cheese_hand.gif")
screen.register_shape("melted_cheese.gif")
screen.register_shape("pepperoni.gif")
screen.register_shape("pepperoni_hand.gif")
screen.register_shape("Burnt_pizza.gif")
screen.register_shape("BG.gif")
screen.register_shape("win.gif")
screen.register_shape("lose.gif")

#setting the background
screen.bgpic("BG.gif")
screen.bgcolor("green")

#setting the music using pygame
music = 'music1.wav'
pygame.mixer.init()
pygame.mixer.Channel(0).play(pygame.mixer.Sound(music), 999)

#initializing the player's shape
player.shape("cheese_hand.gif")

#writing the order
writer.goto(150, 235)
writer.write("ORDER:\n" + str(customercheese) + " cheese\n" + str(customerpepperoni) + " pepperoni\n" + str(customertime) + " seconds of baking", font=("Comic Sans MS", 17))

#baking function (takes in how long you want it to bake)
"""
Title: bake (function)
Author: Parker Szymczak
Date: 4/28/24
Code version: 9.0
Availability: https://github.com/ParkinglotS/PizzaFactory.git
"""
def bake(timerinput):
    #clears the pizza, presumably putting it in the oven
    drawer.clearstamps()
    player.clearstamps()
    player.hideturtle()
    #sets the music to baking music
    music2 = 'baking.wav'
    pygame.mixer.init()
    pygame.mixer.Channel(0).play(pygame.mixer.Sound(music2), 999)
    #if the time inputted is too long, it will only go for 5 seconds and then burn. if there is no ingredients, it will burn otherwise, it just replaces the cheese with baked/melted cheese
    if timerinput <= 60:
        time.sleep(timerinput)
    else:
        time.sleep(5)
    if (len(cheese_stamps_x) < 1 and len(pepperoni_stamps_x) < 1) or timerinput > 60:
        drawer.shape("Burnt_pizza.gif")
        drawer.stamp()
    else:
        drawer.shape("Pizza-no-stuff.gif")
        drawer.stamp()
        player.shape("melted_cheese.gif")
        #keeps track of where ingredients were pre-bake so that it can put them back
        for i in range(len(cheese_stamps_x)):
            player.goto(cheese_stamps_x[i], cheese_stamps_y[i])
            player.stamp()
        player.shape("pepperoni.gif")
        for i in range(len(pepperoni_stamps_x)):
            player.goto(pepperoni_stamps_x[i], pepperoni_stamps_y[i])
            player.stamp()
    pygame.mixer.init()
    pygame.mixer.Channel(0).play(pygame.mixer.Sound(music), 999)

#name input
while True:
    playerName = trt.textinput("Welcome!", "to place an ingredient, press SPACE\nto switch to pepperoni, use P, and for cheese, press C\nWASD to move\nB to bake\n\nPlease write your name:")
    if playerName == "":
        print("please write your name")
    else:
        break

#writing "the inputted name's pizza factory"
writer.goto(-360, 300)
writer.write(playerName + "'s\nPizza Factory", font = ("Comic Sans MS", 17, "italic"))

#initializing player position
player.goto(x, y)

#mainloop
"""
Title: PizzaFactory mainloop
Author: Parker Szymczak
Date: 4/28/24
Code version: 9.0
Availability: https://github.com/ParkinglotS/PizzaFactory.git
"""
while True:
    #movement
    if keyboard.is_pressed("w"):
        y += 1
    if keyboard.is_pressed("s"):
        y -= 1
    if keyboard.is_pressed("a"):
        x -= 1
    if keyboard.is_pressed("d"):
        x += 1
    player.goto(x, y)
    #switching ingredients
    if keyboard.is_pressed("c"):
        ingredient_in_hand = "cheese"
        player.shape("cheese_hand.gif")
    if keyboard.is_pressed("p"):
        ingredient_in_hand = "pepperoni"
        player.shape("pepperoni_hand.gif")
    #placing ingredients
    if keyboard.is_pressed("space"):
        if (ingredient_in_hand == "cheese" and cheese_number > 0) or (ingredient_in_hand == "pepperoni" and pepperoni_number > 0):
            player.shape(ingredient_in_hand + ".gif")
            player.stamp()
            player.shape(ingredient_in_hand + "_hand.gif")
            if ingredient_in_hand == "pepperoni" and pepperoni_number > 0:
                pepperoni_number -= 1
                pepperoni_stamps_x.append(x)
                pepperoni_stamps_y.append(y)
            elif ingredient_in_hand == "cheese" and cheese_number > 0:
                cheese_number -= 1
                cheese_stamps_x.append(x)
                cheese_stamps_y.append(y)
            time.sleep(.2)
    #baking pizza
    if keyboard.is_pressed("b"):
        timer = int(trt.textinput("Baking Time", "How many seconds?"))
        bake(timer)
        #checking if you got the order right
        if not timer == customertime or not len(cheese_stamps_y) == customercheese or not len(pepperoni_stamps_x) == customerpepperoni:
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('LOSING.wav'))
            time.sleep(2)
            customer.shape("customer1talking.gif")
            customer.setx(0)
            customer.sety(0)
            time.sleep(2)
            customer.hideturtle()
            customer.shape("lose.gif")
            customer.stamp()
        else:
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('WINNING.wav'))
            time.sleep(2)
            customer.shape("customer1talking.gif")
            customer.setx(0)
            customer.sety(0)
            time.sleep(2)
            customer.hideturtle()
            customer.setx(0)
            customer.sety(0)
            customer.shape("win.gif")
            customer.stamp()
        break
        



screen.mainloop()