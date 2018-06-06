#while loops

x = True

while x == True:
    print("x is True")
    
#Don't run the above code.  It's an infinite loop that will never stop
#until you press Ctrl-C to break out of it

x = False

while x == True:
    print("x is True")
    
#This is not an infinite loop.  It would run once and stop.

x = 0
while x < 10:
    print("x is less than 10")
    x = x + 1
    
answer = raw_input('Enter a number: ')
#Note that in Python 3 it's "input" instead of "raw_input"

#Guess a number program follows

x = 3
while x > 0:
    answer = int(raw_input("Guess a number between one and ten: "))
    if answer == 8:
        print("Congrats, you win a No-Prize!")
        x = 0
    else:
        print("Sorry, that's not it.  You have " + str(x-1) + " tries remaining.")
        answer = int(raw_input("Guess a number between one and ten: "))
    x = x - 1
    
#Second attempt, where you don't know the number
import random
x = 5
correct = random.randint(1,20)
print("Welcome to the guessing game. You have five chances to guess a number between one and twenty correctly.")
while x > 0:
    answer = int(raw_input("Guess a number: "))
    if answer == correct:
        print("Congrats, you win a No-Prize!")
        x = 0
    else:
        print("Sorry, that's not it.  You have " + str(x-1) + " tries remaining.")
        x -= 1
print("The correct answer was " + str(correct) + ". Game over, man!")

#Testing a brute-force algorithm

x = 0.25
epsilon = 0.01
step = epsilon**2
numGuesses = 0
ans = 0.0
while abs(ans**2 - x) >= epsilon and ans <= x+1:
    ans += step
    numGuesses += 1
print "number of guesses = ", numGuesses

if abs(ans**2 - x) >= epsilon:
    print "Unable to find answer to ", x
    print "Last guess was ", ans
else:
    print ans, " is a close approximation"
    
#bisection search for the ans**X root
x = 27
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2
while abs(ans**3 - x) >= epsilon:
    print "low = ", low, ', high = ', high, " ans = ", ans
    numGuesses += 1
    if ans**3 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2
    
print 'numGuesses = ', numGuesses
print 'answer = ', ans
