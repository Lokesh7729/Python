import random
jack = random.randint(1,100)
counter=1
# print(jack)

guess = int (input("guess the number - "))


while guess!=jack :
    if guess < jack:
        print("guess higher ")
    else: 
        print("guess lower")
    guess = int (input("guess the number - "))
    counter+=1

print("you win !")
print("you took ",counter,"attemps ")


