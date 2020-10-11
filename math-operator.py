#Program for different math operations
from random import*
from math import*

print()
print("Welcome to math operator program!")
print()
print("Here, you can make such basic operations like multiplication or subtraction, solving quadratics as well as playing games!")
print()
print("Choose what operation you would like to do:")

print()

print("Please enter 1 if you want to do simple math operations")
print("Please enter 2 if you want to do more complex math operations")
print("Please enter 3 if you want to play in games involving mathematics")

print()

choice=int(input("Enter the number to proceed =>"))

print()
print()

#Simple Mathematics
if choice==1:
    print("Simple math involves addition, substraction, division and multiplication.")
    print("Consider the information below:")
    print()
    print("Please enter 1 if you want to add")
    print("Please enter 2 if you want to substracte")
    print("Please enter 3 if you want to divide")
    print("Please enter 4 if you want to multiply")
    print("Please enter 5 if you want to find the average of positive and negative numbers")
    print("Please enter 6 if you want to find the sum of a sequence of numbers")
    print("Please enter 7 if you want to raise a number to power")
    print("Please enter 8 if you want to find the square root")
    print()
    command=int(input("Choose a number for further operations => "))
    
    print()
    
    #Addition
    if command==1:
        print("Addition! The general formula for this operation is 'a+b=c'")
        a=float(input("Choose your a =>"))
        b=float(input("Choose your b =>"))
        c=float(a+b)
        print()
        print("The addition is complete! Your a + b =" , round (c, 2))

    #Subtraction
    elif command==2:
        print("Subtraction! The general formula for this operation is 'a-b=c'")
        a=float(input("Choose your a =>"))
        b=float(input("Choose your b =>"))
        c=float(a-b)
        print()
        print("The subtraction is complete! Your a - b =" , round (c, 2))

    #Division
    elif command==3:
        print("Division! The general formula for this operation is 'a/b=c'")
        a=float(input("Choose your a =>"))
        b=float(input("Choose your b =>"))
        c=float(a/b)
        print()
        print("The division is complete! Your a / b =" , round (c, 2))

    #Multiplication
    elif command==4:
        print("Multiplication! The general formula for this operation is 'a*b=c'")
        a=float(input("Choose your a =>"))
        b=float(input("Choose your b =>"))
        c=float(a*b)
        print()
        print("The multiplication is complete! Your a * b =" , round (c, 2))
        
    #Finding average of negative and positive numbers
    elif command==5:
        n=int(input("please tell us how many numbers you want to enter => "))
        a=0    #responsible for postive sum
        b=0    #responible for negative sum
        p=0    #responsible for positive number of numbers
        l=0    #responsible for negative number of numbers
        if n==0:
            print("You need to enter the positive number! try again!")
        elif n<0:
            print("Please enter the positive number!")
        else:
            for x in range(n):
                x=int(input("Enter your numbers => "))
                if x==0:
                    print("You need to enter only either positive or negative answers!")
                    break
                elif x<0:
                    b=b+x
                    l=l+1
                else:
                    a=a+x
                    p=p+1
            print()
            if a==0:
                print("Here is your average of negative numbers:",b/l)
                print("There is no average for positives since you didn't input any positive number")
            elif b==0:
                print("Here is your average of positive numbers:",a/p)
                print("There is no average for negatives since you didn't input any negative number")
            else:
                print("Here is your average of negative numbers:",b/l)
                print("Here is your average of positive numbers:",a/p)

    #Finding the sum of numbers
    elif command==6:
        m=int(input("Please enter your starting number => "))
        n=int(input("Please enter your final number => "))
        i=0
        s=0
        for i in range(m,n+1):
            s=s+i
        print("Here is your sum:",s)

    #Raise to a power
    elif command==7:
        pass
        
        
    #in case if user entered the wrong value for 'command'
    else:
        print("Error 404")
        print()
        print("Math operator is not found. You entered the wrong number")



#More complex mathematics (the quadratic in particular)
if choice==2:
    print("In this section you can calculate quadrarics!")
    equation=("ax^2+bx+c=0")
    
    print()

    print("The general formula for finding the roots of quadratic equation:" ,equation)

    print()
    
    a=float(input("Choose coefficient 'a' =>"))
    b=float(input("Choose coefficient 'b' =>"))
    c=float(input("Choose coefficient 'c' =>"))

    print()

    if a==0:
        print("Your coefficient 'a' is zero.")
        print()
        print("It is not a quadratic equation! It is linear!")
        print()
        print("The general formula in this case is the following: bx+c=0")
        print()
        print("x=", round(-(c/b), 2))

    else:
        d=float(b*b-4*a*c)
        xx1=((-b+d**0.5)/(2*a))
        xx2=((-b-d**0.5)/(2*a))
        xx3=((-b)/(2*a))
    
        if  d>0:
            print("x1=", round(xx1, 2))
            print("x2=", round(xx2, 2))

        if d==0:
            print("There is only one root")
            print("x=", round(xx3, 2))

        if d<0:
            print("Discriminant is negative. Therefore, equation has no roots")
#Math Games
if choice==3:
    print("Ohhh, math games! Let's get started!")
    print("There are different games, please consider and choose from below:")

    print()

    print("Enter '1' if you want to play 'positive or negative!'")
    print("Enter '2' if you want to play 'Guess the number!'")
    print("Enter '3' if you want to play in 'head or tail'!")
    
    print()

    gamek=int(input("Please enter the number here =>"))

    print()

    if gamek==1:
        print("You chose to play in 'positive or negative'")

        print()

        print("!Rules!")
        print("You need to choose the min and max limits for the numbers that will be automaticly generated)")
        print()
        print("Computer will automatically generate the number in the limits that you established.")
        print("You will not know what number the computer generated.")
        print()
        print("However, in case if the 1st number generated is bigger thean the 2nd, you win!")
        print("In case if the 2st is bigger than the 1st, you lose!")
        print("Ready to get sturted? Go!")
        
        print()

        min=int(input("Please enter the min limit:"))
        max=int(input("Please enter the max limit:"))

        b=randint(min,max)
        a=randint(min,max)


        if a>b:
            print("You win!")

        if b>a:
            print("Unluckly! You lost!")

        if a==b:
            print("Your are the GOD! The difference is zero!")

        print("1st number a was equal to",a)
        print("2nd number a was equal to",b)
    if gamek==2:
        print("Program generates the random number from 1 to 100, try to guess!")
        print()
        x=randint(1,100)
        k=0
        while True:
            a=int(input("What is your guess? => "))
            k=k+1
            if a==x:
                if k==1:
                    print("Are you a god? Your guess is correct! Or maybe it wasn't a guess? What's your secret?")
                elif k<=5:
                    print("Congrats! It is correct! You are very lucky and smart! Got it on the try #",k)
                else:
                    print("Congrats! It is correct! Got it on the try #",k)
                    break
            if a>x:
                print("Your guess is too big! Try again.")
            if a<x:
                print("Your guess is too small! Try agin.")
    if gamek==3:
        print("Rules are simple, just follow the instructions that appear on the screen!")
        print()
        bank=float(input("How much money($) do you have? =>"))
        print()
        print("You can make the bets. If you win, you get back twice more than your bet. If you lose, you lose.")
        print()
        while True:
            bet=float(input("How much money do you want to bet for the next round? =>"))
            if 0<bet<=bank:
                guess=int(input("What do you bet on: head(1) or tail(2) =>"))
                number=randint(1,2)
                if number==guess:
                    bank=bank+bet
                    print("You won! Now you have this amount of money:",bank)
                if number!=guess:
                    bank=bank-guess
                    print("You lost this bet!")
            else:
                print("Not possible!")
    
