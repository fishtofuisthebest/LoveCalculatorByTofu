import random

print(" Love Calculator By Tofu ")
print("-------------------------")

#get name

yourName = input("What is your name?: ")
theirName = input("What is their name?: ")

#get percentage

percentage = random.randint(0, 101)

if (percentage == 0):
    print("You and", theirName, "have a love percentage of", percentage, "!")
    print("No. Just. No.")

elif (1 <= percentage <= 25):
    print("You and", theirName, "have a love percentage of", percentage, ".")
    print("I'm sowwy, but it won't last... </3")

elif (26 <= percentage <= 49):
    print("You and", theirName, "have a love percentage of", percentage, ".")
    print("Maybe you guys are better off as just friends?")

elif (percentage == 50):
    print("You and", theirName, "have a love percentage of", percentage, "!")
    print("It might last. It might not last. I don't know.")

elif (51 <= percentage <= 75):
    print("You and", theirName, "have a love percentage of", percentage, ".")
    print("You're getting there.")

elif (76 <= percentage <= 99):
    print("You and", theirName, "have a love percentage of", percentage, ".")
    print("Yay! It'll last!!! <3")

else:
    print("You and", theirName, "have a love percentage of", percentage, "!")
    print("When's the wedding???")

print("-------------------------")

