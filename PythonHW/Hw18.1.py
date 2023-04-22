# guess the number
import random
guessesTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(0, 50)
print(myName + "I am thinking of number between 0 and 50")

for guessesTaken in range(7):
    print("Take a guess")
    guess = input()
    guess = int(guess)

    if guess < number:
        print('The value is too low')

    if guess > number:
        print('The value is too high')

    if guess == number:
        break

guessesTaken = (guessesTaken + 1)
print('You guessed correctly' + myName)

