import random
guracoinprice = 100 # Sets the price for gura
money = 100 # User money
guracoininventory = 0 # The amount the player has
turns = 0 #Which day it is, late id like to change this so theres a morning night cycle
startingturns = 21 #Decided with 21 to do a 7 day week in the future I want to have a Morning Afternoon Night phase. For Morning
turnend = 0
while turns < startingturns:
    raiseorlower = random.randint(-150, 150)
    purchaseamount = None
    sellamount = None
    print("Turns left : ", startingturns-turns)
    print("Gura Price : ",guracoinprice)
    print("Gura Coins in Inventory: ", guracoininventory)
    print("Money: ",money)
    print("\n1: Buy Gura Coin")
    print("\n2: Sell Gura Coin")
    print("\n3: Wait one turn\n")
    selection = input("Please Select:\n") # reading the selection for the menu above
    if selection =='1':
        if money < guracoinprice:
            print("You don't have enough money for this transaction.\n")
        else:
            while purchaseamount is None: # I read in a tutorial, thile while purchase amount is none is supposed to help so users cant throw a string
                try:
                    purchaseamount = int(input("Please put a number for how much you'd like to purchase.\n")) #This converts the string into a int
                except ValueError:      
                    print("Please enter a valid number.\n") # and if it cant turn it into a int it gives the above valueerror and throws the user a fuck you
                if guracoinprice*purchaseamount < money:
                    guracoininventory += purchaseamount
                    money -= guracoinprice*purchaseamount
                    turns += 1
                    turnend = 1
            else:
                ("Print you don't have enough for that purchase.\n")
    if selection =='2':
        if guracoininventory < 0:
            print("You don't have enough coins for this transaction.\n")
        else:
            while sellamount is None: 
                try:
                    sellamount = int(input("Please put a number for how much you'd like to purchase.\n"))
                except ValueError:      
                    print("Please enter a valid number.\n")
                if guracoininventory*sellamount > 0:
                    guracoininventory -= sellamount
                    money += guracoinprice*sellamount
                    turns += 1
                    turnend = 1
            else:
                ("Print you don't have enough for that purchase.\n")
    elif selection == '3':
        print("You waited one turn.\n")
        turns += 1
        turnend = 1
    else:
        print("Please pick between 1 2 or 3\n")
    if turnend == 1:
        guracoinprice+=raiseorlower
        if guracoinprice< 0:
            guracoinprice = 100
            print("Gura's coin fell below 0 and was injected with 100 in value.\n")
print("Thank you for playing the game.\n")
