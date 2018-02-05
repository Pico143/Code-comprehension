'''This program picks a random number between 1 and 20 
and lets user pick his name and take up to 6 guesses what this number is.'''


import random # import random library

guesses_taken = 0 # declare variable "guesses_taken" and set it's value to 0.

print('Hello! What is your name?') #show the message in quotes in the console 
myName = input() # assign user's input to "myName" variable

number = random.randint(1, 20) #pick a number between 1 and 20 (including 1 and 20)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.') # show the message in quotes in console with user's name in between

while guesses_taken < 6: #while loop that let's user take up to 6 guesses
    print('Take a guess.') #show the message in quotes in the console 
    guess = input() #assign user's input to "guess" variable
    guess = int(guess) #convert user's input to integer

    guesses_taken += 1 #increase "guesses_taken" variable by one

    if guess < number: #checking if user provided number lower than the randomly generated one
        print('Your guess is too low.') #print

    if guess > number: #checking if user provided number higher than the randomly generated one
        print('Your guess is too high.') # print

    if guess == number: #checking if user provided number equal to the randomly generated one
        break #if number is corrected - stop guessing by getting out of the while loop

if guess == number: #if while loop was ended by providing correct number
    guesses_taken = str(guesses_taken) #converting variable "guesses_taken" to string (which is not really necessary here as it can happen implicitly too!)
    print('Good job, ' + myName + '! You guessed my number in ' + guesses_taken + ' guesses!')

if guess != number: #if while loop was ended by using all the guesses and not guessing the number
    number = str(number) #converting variable "number" to string (which is not really necessary here as it can happen implicitly too!)
    print('Nope. The number I was thinking of was ' + number)
