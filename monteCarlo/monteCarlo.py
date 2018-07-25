import random

def figureCheck( x, y ):
    if x < 0.5 : return True
    else : return False 

t = 0
f = 0

for i in range(10000) :
    if figureCheck(random.random(), random.random()): t += 1
    else: f += 1

print (t / 10000)