#
#モンテカルロ法　円の面積を求める
#

import random

def figureCheck( x, y, r):
    if (( x**2 ) + ( y**2 )) < ( r**2 ) : return True
    else : return False 

t = 0

r = int(input("Please input 円の直径: "))

for i in range(10000) :
    if figureCheck(random.uniform( 0, r ), random.uniform( 0, r ), r) :
        t += 1

print (t / 10000 * 4) 