import turtle as trt
import keyboard, time, pygame, random

pygame.init()  
drawer = trt.Turtle()
drawer.speed(0)

pepperoni_number = 10
cheese_number = 10
ingredient_in_hand = "cheese"

customertime = random.randint(5, 15)
customercheese = random.randint(0, 10)
customerpepperoni = random.randint(0, 10)
if customerpepperoni == 0 and customercheese == 0:
    customercheese += 1

success = True

x = 0
y = -200
screen = trt.Screen()
cheese_stamps_x = []
cheese_stamps_y = []
pepperoni_stamps_x = []
pepperoni_stamps_y = []

customer = trt.Turtle()
customer.penup()
screen.register_shape("customer1.gif")
screen.register_shape("customer1talking.gif")
customer.shape("customer1.gif")

drawer.hideturtle()
drawer.penup()

writer = trt.Turtle()
writer.penup()
writer.hideturtle()

screen.register_shape("Pizza-no-stuff.gif")

drawer.goto(x,y)
drawer.shape("Pizza-no-stuff.gif")
drawer.stamp()

player = trt.Turtle()

screen.register_shape("cheese.gif")
screen.register_shape("cheese_hand.gif")
screen.register_shape("melted_cheese.gif")
screen.register_shape("pepperoni.gif")
screen.register_shape("pepperoni_hand.gif")
screen.register_shape("Burnt_pizza.gif")
screen.register_shape("BG.gif")
screen.register_shape("win.gif")
screen.register_shape("lose.gif")

screen.bgpic("BG.gif")
screen.bgcolor("green")

music = 'music1.wav'
pygame.mixer.init()
pygame.mixer.Channel(0).play(pygame.mixer.Sound(music), 999)

player.shape("cheese_hand.gif")
player.penup()


customer.goto(0, -100)
writer.goto(150, 235)
writer.write("ORDER:\n" + str(customercheese) + " cheese\n" + str(customerpepperoni) + " pepperoni\n" + str(customertime) + " seconds of baking", font=("Comic Sans MS", 17))

running = True
def stop():
    global running
    running = False
    exit()

def bake(timerinput):
    drawer.clearstamps()
    player.clearstamps()
    player.hideturtle()
    music2 = 'baking.wav'
    pygame.mixer.init()
    pygame.mixer.Channel(0).play(pygame.mixer.Sound(music2), 999)
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
        for i in range(len(cheese_stamps_x)):
            player.goto(cheese_stamps_x[i], cheese_stamps_y[i])
            player.stamp()
        player.shape("pepperoni.gif")
        for i in range(len(pepperoni_stamps_x)):
            player.goto(pepperoni_stamps_x[i], pepperoni_stamps_y[i])
            player.stamp()
    pygame.mixer.init()
    pygame.mixer.Channel(0).play(pygame.mixer.Sound(music), 999)

player.goto(x, y)
trt.textinput("Welcome!", "to place an ingredient, press SPACE\nto switch to pepperoni, use P, and for cheese, press C\nWASD to move\nB to bake")

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
            if ingredient_in_hand == "pepperoni" and pepperoni_number > 0:
                pepperoni_number -= 1
                pepperoni_stamps_x.append(x)
                pepperoni_stamps_y.append(y)
            elif ingredient_in_hand == "cheese" and cheese_number > 0:
                cheese_number -= 1
                cheese_stamps_x.append(x)
                cheese_stamps_y.append(y)
            time.sleep(.2)
    if keyboard.is_pressed("b"):
        timer = int(trt.textinput("Baking Time", "How many seconds?"))
        bake(timer)
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