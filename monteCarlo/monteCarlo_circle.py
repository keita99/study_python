#
#モンテカルロ法　円の面積を求める
#

import random

def pi( check_count):
    t = 0
    for i in range( check_count) :
        x = random.random()
        y = random.random()
        if (( x**2 ) + ( y**2 )) <=  1  : t += 1

    return ( t / check_count * 4)

r = int(input("Please input 円の半径: "))


print ( "pi check count 100 : ", pi(100))
print ( "pi check count 1000 : ", pi(1000))
print ( "pi check count 10000 : ", pi(10000))
print ( "pi check count 100000 : ", pi(100000))

print ( "円の半径 ", r ," の円の面積は ", ( r * r * pi( 100000 )))