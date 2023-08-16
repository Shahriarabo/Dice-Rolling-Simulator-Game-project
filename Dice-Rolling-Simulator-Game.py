import random

drolling = True

while drolling:
    print(random.randint(1,6))
    play = input("Do you want to play [y/n] : ")
    if play == "y":
        continue
    else:
        print("The Game is Over")
        break
