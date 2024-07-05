#Ayden
import math
from turtle import *
def hrt0(k):
    return 15*math.sin(k)**3
def hrt1(k):
    return 12*math.cos(k)-5*\
    math.cos(2*k)-2*\
    math.cos(3*k)-\
    math.cos(4*k)
speed(0)
bgcolor("Black")
for i in range(6000):
    goto(hrt0(i)*20,hrt1(i)*20)
    for j in range(5):
        color("pink")
        goto(0,0)
        done()
#Ayden
