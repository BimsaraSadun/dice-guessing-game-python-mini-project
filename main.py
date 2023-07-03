import random

guesses = 0
mistakes = 0

while True:
    number = random.randrange(1, 7)
    plr_numb = input("Bazinga! dice rolled!!!\n Enter your guess: ")
    if plr_numb.isdigit():
        plr_numb = int(plr_numb)
        if plr_numb > 6:
            mistakes += 1
            print("This is a six-sided dice! Enter lower than 6")
        if plr_numb <= 0:
            mistakes += 1
            print("This is a dice! Enter higher than 0")
    else:
        mistakes += 1
        print("This is a dice! Enter correct input")
        continue

    guesses += 1
    if plr_numb == number:
        print("YOU WIN")
        break
    else:
        print("try again PC choice " + format(number))
print("guesses count: " + format(guesses) + "\nmistakes count: " + format(mistakes))
