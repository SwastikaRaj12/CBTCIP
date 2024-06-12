import random
num = random.randrange(1000, 10000)
print(num)
chances = 5
guess = eval(input("guess a 4 digit number, you have 5 chances: "))
if guess == num:
    print("Great you won, now you are a mastermind")
else:
    tries = 0
    while guess != num and chances:
        tries += 1
        chances -= 1
        correctdigits = 0
        guess = str(guess)
        num = str(num)
        correct = ['X']*4
        for i in range(0, 4):
            if guess[i] == num[i]:
                correctdigits += 1
                correct[i] = num [i]
        if correctdigits < 4 and correctdigits > 0 and chances:
            print("Not the right guess, but you guessed", correctdigits, "numbers right")
            print("current status is: ")
            for char in correct:
                print(char, end='  ')
            print('\n')
            print('\n')
            guess = eval(input("guess a 4 digit number, you have 5 chances: "))
        elif correctdigits == 0 and chances:
            print("none of the digits you guessed is right")
            guess = eval(input("guess a 4 digit number, you have 5 chances: "))
        if guess == num:
            print("great you win", tries, "guesses, now you are a mastermind")
        if chances == 0:
            print("sorry, you lost, as you ran out of chances")
            print("number is", num)
