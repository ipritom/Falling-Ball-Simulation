'''
Falling Ball Simulation
Version: 0.1
by Pritom Mojumder
____________________
axis() to visualize XY axis
X(),Y() to transform points according to transformed axis
ball(x,y,radius,time) creates ball
drop(y,height,trigger_time,time) perform dropping event

'''

import pygame as p
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'
width = 900; height = 900
c_x = int(width/2)
c_y = int(height/2)+100

t_state = False #this only triggered when obejct needs to be droped
t = 0
g = 18
#set origin at surface center
def X(x): 
    global width
    return int((c_x+x))
def Y(y):
    global height
    return int((c_y-y))
#create visible axis
def axis():
    p.draw.line(gameDisplay,ash,[X(0),Y(c_y)],[X(0),Y(-c_y)],1) #x-axis
    p.draw.line(gameDisplay,ash,[X(-c_x),Y(0)],[X(c_x),Y(0)],1) #y-axis
def ball(x,y,radi,clk):
    global t_state
    global t
    
    h = radi
    #when clock is off
    if t_state == False:
        #need to fall
        if y>h:
            t = clk
            t_state = True
            print("initialize y,t,clk",y,t,clk)
            p.draw.circle(gameDisplay,ash,[X(x),Y(y)],radi,2)
            return y
        #no need to fall    
        elif y<=h:
            print("no_drop")
            p.draw.circle(gameDisplay,ash,[X(x),Y(y)],radi,2)
            return y
    #when clock is running       
    elif t_state == True:
        #print("droping y,t,clk",y,t,clk)
        y = drop(y,h,t,clk)
        p.draw.circle(gameDisplay,ash,[X(x),Y(y)],radi,2)
        return y
    
def drop(y,h,t,clk):
    global t_state

    dt = abs(t-clk) #dt = elasped time
    H = .5*g*dt**2 #falling height
    y = int(y-H)
    if y>h:
        print("Droping...h,y = ",H,y)
        return y
    else:
        print("DOOMED\n")
        y = h
        t=0
        t_state = False
        return y
#colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,40)

light = (250, 245, 252)
paste = (189, 233, 252)
ash = (105,109,126)
p.init()

p.display.set_caption('Environment')
clock = p.time.Clock()
gameDisplay = p.display.set_mode((width,height))
def game_loop():
    crash = False
    x_change = 0
    y_change = 0
    x = 0
    y = c_y-100
    g = 9.8
    t = 0
    h = 0
    dt = 0

    while not crash:
        for event in p.event.get():
            if event.type == p.QUIT:
                crash = True
            #keyboard control
            if event.type == p.KEYDOWN:
                if event.key == p.K_LEFT:
                    x_change -=1
                elif event.key == p.K_RIGHT:
                    x_change +=1
                elif event.key == p.K_DOWN:
                    y_change -= 10
                elif event.key == p.K_UP:
                    y_change += 10
                elif event.key == p.K_SPACE: #stop all change
                    y_change = 0
                    x_change = 0
        gameDisplay.fill(light)
        axis()
      
        x += x_change
        y += y_change
        clk = p.time.get_ticks()/1000
        
        #object...
        y = ball(x,y,40,clk)
        #print(x,y,clk,t)
        #bounderies
        if X(x) > X(c_x-50):
            x = 0
        if X(x) < X(-c_x):
            x = 0

        #screening
        p.display.update()
        clock.tick(30)

game_loop()
p.quit()
