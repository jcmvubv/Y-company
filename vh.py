import random
 
symbols = ["a", "b", "c"]
 
 
while True:
    tokens = 10000
    print("Welcome to slots game.")
    while tokens > 0:
        print("You have", tokens, "tokens.")
        try:
            bet = int(input("Bet amount: "))
        except:
            print("Please enter a whole number of tokens.")
            continue
        if bet > tokens:
            print("Not enough tokens!! 10% off buffet on your players card, come back later plzz")
        else:
            tokens -=bet
            sq_one = random.choice(symbols)
            sq_two = random.choice(symbols)
            sq_three = random.choice(symbols)
 
            print()
 
            print("|", random.choice(symbols), "|", random.choice(symbols), "|" ,random.choice(symbols), "|")
            print("-----------------------")
 
            print("|", sq_one, "|", sq_two, "|", sq_three, "|")
            print("-----------------------")
 
            print("|", random.choice(symbols), "|", random.choice(symbols), "|" ,random.choice(symbols), "|")
            print()
 
            if sq_one == sq_two and sq_two == sq_three:
                amountwon = bet*5
                print("Hey idiot put it back in by the way, you won,", amountwon, "tokens.")
                tokens += amountwon
            else:
                print("Poop, you lost :( :( ")
                print("Try your luck again right now sucker!")
                print()
 
 