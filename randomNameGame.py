import time
import random
print("Wanna play a game?")
choice = input()
if choice == 'yes':
    print("Rules are pretty simple.")
    time.sleep(3)
    print("I will choose a number at random between 1-100")
    time.sleep(3)
    print("You do get unlimited tries, but every wrong answer you get your score will be deducted by 10")
    time.sleep(3)
    print("Your initial score will be 100 and the score can go beyond 0")
    time.sleep(3)
    print("So, let's start the game")
    time.sleep(3)
    answer = random.randint(0, 100)
    loop = 0
    score = 100
    x = 0
    y = 100
    turn = 0
    while loop == 0:
        choice = int(input("Enter your choice "))
        if choice == answer:
            print("Congratulations!! It's the right answer ")
            turn = turn + 1
            print("You tried ", turn, "times")
            print("Your score is ", score)
            loop = 1
            time.sleep(5)
        if choice != answer:
            print(choice)
            print("Wrong guess. Try Again!! 10 points deducted ")
            score = score - 10
            turn = turn + 1
            if turn == 1:
                c = (x + y)/2
                if answer <= c:
                    print("The number is between ", x, " & ", c)
                    y = c
                if answer > c:
                    print("The number is between ", c, " & ", y)
                    x = c
            if turn == 2:
                nprime = 0
                for i in range(2, 9):
                    if answer % i == 0:
                        print("The number is divisible by ", i)
                        nprime = 1
                        break
                if nprime == 0:
                    print("The number is a prime number")
            for i in range(3, 6):
                if turn == i:
                    c = (x + y)/2
                    if answer <= c:
                        print("The number is between ", x, " & ", c)
                        y = c
                    if answer > c:
                        print("The number is between ", c, " & ", y)
                        x = c
