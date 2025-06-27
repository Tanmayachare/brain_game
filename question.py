import math
import random
score = 0
import datetime

def square():
    num = random.randint(1,100)
    start=datetime.datetime.now().second
    a = int(input(f"enter square of {num}:"))
    stop=datetime.datetime.now().second
    timetaken=stop-start
    print(f"time taken is {timetaken}")
    global score
    if a == num**2:
        print("correct answer")
        score = score + 10
    else:
        print("wrong answer")
        score = score - 5

    

def sqroot():
    num = random.randint(1,100)
    while(math.sqrt(num)!=(int(math.sqrt(num)))):
        num = random.randint(1,100)
    start=datetime.datetime.now().second
    a = int(input(f"enter square root of {num}:"))
    stop=datetime.datetime.now().second
    timetaken=stop-start
    print(f"time taken is {timetaken}")
    global score
    if a == math.isqrt(num):
        print("correct answer")
        score = score + 10
        
    else:
        print("wrong answer")
        score = score - 5
        
