import random
guracoinprice = 100
money = 100
guracoininventory = 0
turns = 0
while turns < 5:
    print("Turns left : ", 5-turns)
    print("Gura Price : ",guracoinprice)
    print("Gura Coins in Inventory: ", guracoininventory)
    print("Money: ",money)
    print("\n1: Buy One Gura Coin")
    print("\n2: Sell One Gura Coin")
    print("\n3: Wait one turn")
    selection = input("Please Select:\n")
    if selection =='1':
        if money < guracoinprice:
            print("You don't have enough money for this transaction.")
        else:
            print("You bought one Gura coin and ended your turn.\n")
            guracoininventory += 1
            money -= guracoinprice
            turns += 1
    elif selection == '2':
        if guracoininventory < 1:
            print("You don't have enough coins for this transaction.")
        else:
            print("You sold one Gura coin and ended your turn.\n")
            guracoininventory - 1
            money += guracoinprice
            turns += 1        
    elif selection == '3':
        print("You waited one turn.")
        turns += 1
    else:
        print("Try again retard. 1 2 or 3")
print("Thank you for playing the game.\n")
