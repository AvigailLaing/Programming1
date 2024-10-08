#Game loop that helps you go from one game to another
#Beginning of every game prints Start Game #_
#But within each game, you need a smaller loop to give the player decisions
import p1_random as p1
rng = p1.P1Random()

#STARTING VARIABLES
game_num = 0
player_win = 0
dealer_win = 0
game_ties = 0
in_progress = True
#Game is in progress

while in_progress:
    #New game loop
    game_num += 1
    print(f"\nSTART GAME #{game_num}")
    cardValue = rng.next_int(13) + 1
    if cardValue <=10:
        handTotal = cardValue
        if cardValue == 1:
            cardName = "ACE"
        else:
            cardName = cardValue
    else:
        handTotal = 10
        if cardValue == 11:
            cardName = "JACK"
        elif cardValue == 12:
            cardName = "QUEEN"
        else:
            cardName = "KING"
        #Sets the value of the hand to 10 for Jack, Queen, and King
    #Generates value from 0-12 + 1, so 0-13
    print(f"\nYour card is a {cardName}!")
    print(f"Your hand is: {handTotal}")
    #Add function to set number equal to value

    #INNER GAME LOOP
    def choiceMenu():
        print("\n1. Get another card")
        print("2. Hold hand")
        print("3. Print statistics")
        print("4. Exit")
    while True:
        choiceMenu()
        choice = int(input("\nChoose an option: "))
        if choice == 1:
            cardValue = rng.next_int(13) + 1
            if cardValue == 1:
                handTotal += 1
                print(f"\nYour card is a ACE!")
                print(f"Your hand is: {handTotal}")
            elif 2<=cardValue<=10:
                handTotal += cardValue
                print(f"\nYour card is a {cardValue}!")
                print(f"Your hand is: {handTotal}")
            else:
                handTotal += 10
                if cardValue == 11:
                    cardName = "JACK"
                elif cardValue == 12:
                    cardName = "QUEEN"
                else:
                    cardName = "KING"
                print(f"\nYour card is a {cardName}!")
                print(f"Your hand is: {handTotal}")

            if handTotal == 21:
                player_win += 1
                print("\nBLACKJACK! You win!")
                break
            elif handTotal > 21:
                dealer_win += 1
                print("\nYou exceeded 21! You lose.")
                break
        elif choice == 2:
            #Dealer's draw
            dealerHand = rng.next_int(11) + 16
            print(f"\nDealer's hand: {dealerHand}")
            print(f"Your hand is: {handTotal}")
            if dealerHand == 21:
                dealer_win += 1
                print("\nDealer wins!")
                break
                #Stops inner game loop
            elif dealerHand > 21:
                player_win += 1
                print("\nYou win!")
                break
            elif handTotal == dealerHand:
                print("\nIt's a tie! No one wins!")
                game_ties += 1
                break
            elif handTotal > dealerHand:
                player_win += 1
                print("\nBLACKJACK! You win!")
                break
            elif dealerHand > handTotal:
                dealer_win += 1
                print("\nDealer wins!")
                break
        elif choice == 3:
            print(f"\nNumber of Player wins: {player_win}")
            print(f"Number of Dealer wins: {dealer_win}")
            print(f"Number of tie games: {game_ties}")
            print(f"Total # of games played is: {game_num - 1}")
            #Have to subtract 1 because we are in the middle of a game
            percentWins = (player_win/(game_num - 1)) * 100
            print(f"Percentage of Player wins: {percentWins:.1f}%")
            #Print stats
        elif choice == 4:
            in_progress = False
            break
            #Inner loop breaks
        else:
            print("Invalid input!")
            print("\nPlease enter an integer value between 1 and 4.")