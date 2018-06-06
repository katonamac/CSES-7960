#here are some fun errors
import doubledutch

int('two')

print(greenGrass)

myList = [1,2,3]
myList[4]

#Fix the last one like this
myList = [1,2,3]
try:
    print(myList[4])
except IndexError:
    print("The list is only " + str(len(myList)) + " objects long.")
    
#This is a program to multiply two numbers but to tell the user
#that they have to enter a number if they try to enter a string

def mult(x,y):
    try:
        chunk = float(x)*float(y)
        return chunk
    except ValueError:
        print("Sorry, you have to enter two numbers.")
        
x = raw_input("Enter a number to multiply:")
y = raw_input("Enter another number to get the answer:")
mult(x,y)

#Homework for the next week: Hangman problem
