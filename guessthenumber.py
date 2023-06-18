import random

SecretNum = random.randint(0,9)

while True:
    print("I have a number in mind, and you need to guess it")
    Guess = int(input("Enter any number: "))
    if Guess == SecretNum:
        print("Wow you got it")
        print("Thanks for playing")
        break
    else:
        print("Sorry but no you suck, I'll give you a hint")
        if Guess > SecretNum:
            print("Too high")
        else:
            print("Too low")
            print("...............................")





