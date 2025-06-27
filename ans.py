import question as q
import random
name = input("Enter your name: ")



while True:
    func=[q.sqroot,q.square]
    cont = int(input("if you want to continue 1/0:"))
    if cont == 1:
        choose=random.choice(func)
        choose()
    else :
        print(f"your final score is {q.score}")
        break

