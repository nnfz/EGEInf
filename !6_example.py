# 1 Example № 21892

from turtle import *# *

k = 20# **
tracer(0)# *
screensize(1000, 1000)# ** window size

rt(90)#turn right 90

for x in range(7):#repeat 7 times
    rt(45)#turn right 45
    fd(11*k)#go forward 11 * 20
    rt(45)#turn right 45

pu()# * tall up
for x in range(-20, 20):# **
    for y in range(-20, 20):# **
        goto(x * k, y * k)# *
        dot(3)# **
done()# *

# 2 Example № 21405

from turtle import *# *

k = 30# **
tracer(0)# *
screensize(1000, 1000)# ** window size

rt(30)# turn right 30

for x in range(3):# repeat 3 times
    rt(150)# turn right 150
    fd(6 * k)# go forward 6
    rt(30)  # turn right 30
    fd(12 * k)# go forward 12

pu()# * tall up

for x in range(-20, 20):# *
    for y in range(-20, 20):# *
        goto(x * k, y * k)# *
        dot(3)# *

done()

# Example 3 № 21701

from turtle import *# *

tracer(0)# *
screensize(2000, 1000)# ** window size
k = 20# **

for x in range(2):# repeat 2 times
    fd(28 * k)# go forward 28
    rt(90)#turn right 90
    fd(18 * k)# go forward 18
    rt(90)#turn right 90

pu()# tall up

fd(14 * k)# go forward 14
rt(90)#turn right 90
fd(10 * k)# go forward 10
lt(90)#turn left 90

pd()

for x in range(2):
    fd(30 * k)# go forward 30
    rt(90)#turn right 90
    fd(7 * k)# go forward 10
    rt(90)#turn right 90

pu()

for x in range(-20, 50):
    for y in range(-20, 20):
        goto(x * k, y * k)
        dot(3)
done()

