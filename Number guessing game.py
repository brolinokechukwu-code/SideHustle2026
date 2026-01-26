# Number guessing game
import random
count = 0
limit = int(input("Enter maximum number: "))
rand_num = random.randint(1,limit)


while True:
    guess = int(input("Enter a number between 1 and your limit: "))
    count += 1
    if guess == rand_num:
        print("Correct!")
        print(f"You guessed it in {count} tries")
        break
    elif  guess < rand_num:
        print("Too low")
    elif guess > rand_num:
        print("Too high")
    if count >= 7:
        print("You have used all your guesses - YOU LOSE!")
        break
   

