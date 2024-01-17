import random
guracoinprice = 100 # Sets the price for gura
money = 100 # User money
guracoininventory = 0 # The amount the player has
turns = 0 #Which day it is, late id like to change this so theres a morning night cycle
startingturns = 21 #Decided with 21 to do a 7 day week in the future I want to have a Morning Afternoon Night phase. For Morning

while turns < startingturns:
    raiseorlower = random.randint(-150, 150)
    print("Turns left : ", startingturns-turns)
    print("Gura Price : ",guracoinprice)
    print("Gura Coins in Inventory: ", guracoininventory)
    print("Money: ",money)
    print("\n1: Buy One Gura Coin")
    print("\n2: Sell One Gura Coin")
    print("\n3: Wait one turn\n")
    selection = input("Please Select:\n") # reading the selection for the menu above
    if selection =='1':
        if money < guracoinprice:
            print("You don't have enough money for this transaction.\n")
        else:
            print("You bought one Gura coin and ended your turn.\n")
            guracoininventory += 1
            money -= guracoinprice
            turns += 1
    elif selection == '2':
        if guracoininventory < 1:
            print("You don't have enough coins for this transaction.\n")
        else:
            print("You sold one Gura coin and ended your turn.\n")
            guracoininventory - 1
            money += guracoinprice
            turns += 1        
    elif selection == '3':
        print("You waited one turn.\n")
        turns += 1
    else:
        print("Please pick between 1 2 or 3\n")
    
    guracoinprice+=raiseorlower
    if guracoinprice< 0:
        guracoinprice = 100
        print("Gura's coin fell below 0 and was injected with 100 in value.\n")
print("Thank you for playing the game.\n")
