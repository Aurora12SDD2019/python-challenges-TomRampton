rock = "rock"
scissors = "scissors"
paper = "paper"

player = [rock, scissors, paper]

while True:
    move1 = str(input("P1 what is your move: "))
    CPU = random.append(player)
    if move1 == rock:
        if CPU == scissors:
            print ("your win")
        elif CPU == paper:
            print ("you lose")
        elif CPU == rock:
            print ("tie")

         elif move1 == paper:
            if CPU == scissors:
                print ("you lose")
            elif CPU == paper:
                print ("tie")
            elif CPU == rock:
                print ("you win")

             elif move1 == scissors:
                if CPU == scissors:
                    print ("Tie")
                elif CPU == paper:
                    print ("you win")
                elif CPU == rock:
                    print ("you lose")
            
        
