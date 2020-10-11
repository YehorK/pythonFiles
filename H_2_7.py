from random import*

#1
print("Program generates the random number from 1 to 100, try to guess!")
print()
x=randint(1,100)
print(x)
k=0
while True:
    a=int(input("What is your guess? => "))
    k=k+1
    if a==x:
        if k==1:
            print("Are you a god? Your guess is correct! Or maybe it wasn't a guess? What's your secret?")
        elif k<5:
            print("Congrats! It is correct! You are very lucky and smart! Got it on the try #",k)
        else:
            print("Congrats! It is correct! Got it on the try #",k)
        break
    if a>x:
        print("Your guess is too big! Try again.")
    if a<x:
        print("Your guess is too small! Try agin.")


#2
print("Program generates the random number from 1 to 100, try to guess!")
print()
x=randint(1,100)
print(x)
k=0
a=int(input("What is your guess? => "))
while a!=x:
    a=int(input("What is your guess? => "))
    k=k+1
    if a==x:
        if k==1:
            print("Are you a god? Your guess is correct! Or maybe it wasn't a guess? What's your secret?")
        elif k<5:
            print("Congrats! It is correct! You are very lucky and smart! Got it on the try #",k)
        else:
            print("Congrats! It is correct! Got it on the try #",k)
        break
    if a>x:
        print("Your guess is too big! Try again.")
    if a<x:
        print("Your guess is too small! Try agin.")
