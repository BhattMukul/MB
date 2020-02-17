import random


def winning(player_name, p_score, p_bet, dealer_score):
    ''' 
    winning function is to check whether the players playing against dealer won or losses the BET
    '''
    if p_score > 21:   # player bust out condition
        print(player_name + " You Bust Out...")
        amount_won = p_bet * -1    # player losses the bet and get loss of bet amount
        return amount_won

    elif dealer_score > 21 and p_score < 21:   # condition for dealer bust out
        print("\nDealer Is Bust..." + player_name + ' You Doubles Bet Amount')
        profit = p_bet * 2  # player gets the profit of 200%
        amount_won = p_bet + profit  # amount after profit
        return amount_won

    elif p_score == 21:    # condition for blackjack
        print(player_name + " YOU ARE A BLACKJACK...")
        profit = p_bet * 1.5   # player gets the profit of 150%
        amount_won = p_bet + profit    # amount after profit
        return amount_won


    elif p_score > dealer_score and p_score < 21:   # condition if player won against dealer
        print("\n" + player_name + "You Won...")
        profit = p_bet * 2   # player gets profit of 100%
        amount_won = p_bet + profit   # amount after profit  
        return amount_won

    elif p_score < dealer_score:   # condition if dealer won against player
        print(player_name + " You Lose...")
        amount_won = p_bet * -1   # player get loss of bet amount
        return amount_won

    elif p_score == dealer_score:  # condition for draw 
        print(player_name + " You Have A DRAW")
        return p_bet    # no profit no loss




player1_amount = 0    # player1 profit or loss before a game round 
player2_amount = 0    # when 2 players are playing : player2 profit or loss before a game round
player3_amount = 0    # when 3 players are playing : player3 profit or loss before a game round

while True:
    # all 52 cards in a deck
    total_card_list = [
        "Spade_A", "Spade_2", "Spade_3", "Spade_4", "Spade_5", "Spade_6", "Spade_7", "Spade_8", "Spade_9",
        "Spade_10", "Spade_J", "Spade_Q", "Spade_K",
        "Heart_A", "Heart_2", "Heart_3", "Heart_4", "Heart_5", "Heart_6", "Heart_7", "Heart_8", "Heart_9",
        "Heart_10", "Heart_J", "Heart_Q", "Heart_K",
        "Club_A", "Club_2", "Club_3", "Club_4", "Club_5", "Club_6", "Club_7", "Club_8", "Club_9",
        "Club_10", "Club_J", "Club_Q", "Club_K",
        "Diamond_A", "Diamond_2", "Diamond_3", "Diamond_4", "Diamond_5", "Diamond_6", "Diamond_7",
        "Diamond_8", "Diamond_9", "Diamond_10", "Diamond_J", "Diamond_Q", "Diamond_K"
    ]



    while True:
        player1 = False
        player2 = False    # confirmation for players playing
        player3 = False    # you will understand it after moving ahead
        while True:
            num_players = int(input("\nHow Many Players Are Playing : "))    # Num. of playing players
            if num_players in range(1, 4):   # condition : not more than 3 players allowed
                break
            else:
                print("More Than 3 Players Are Not Allowed")
                continue


        class BlackJack:    # The Main Game Class
            # points for all 52 cards in a deck
            card_value = {"Spade_A": 1, "Heart_A": 1, "Club_A": 1, "Diamond_A": 1,
                          "Spade_2": 2, "Heart_2": 2, "Club_2": 2, "Diamond_2": 2,
                          "Spade_3": 3, "Heart_3": 3, "Club_3": 3, "Diamond_3": 3,
                          "Spade_4": 4, "Heart_4": 4, "Club_4": 4, "Diamond_4": 4,
                          "Spade_5": 5, "Heart_5": 5, "Club_5": 5, "Diamond_5": 5,
                          "Spade_6": 6, "Heart_6": 6, "Club_6": 6, "Diamond_6": 6,
                          "Spade_7": 7, "Heart_7": 7, "Club_7": 7, "Diamond_7": 7,
                          "Spade_8": 8, "Heart_8": 8, "Club_8": 8, "Diamond_8": 8,
                          "Spade_9": 9, "Heart_9": 9, "Club_9": 9, "Diamond_9": 9,
                          "Spade_10": 10, "Heart_10": 10, "Club_10": 10, "Diamond_10": 10,
                          "Spade_J": 10, "Heart_J": 10, "Club_J": 10, "Diamond_J": 10,
                          "Spade_Q": 10, "Heart_Q": 10, "Club_Q": 10, "Diamond_Q": 10,
                          "Spade_K": 10, "Heart_K": 10, "Club_K": 10, "Diamond_K": 10,
                          }

            def hit(self, player_name):
                ''' 
                HIT MOVE in BlackJack Game
                '''
                self.player_name = player_name
                card_index = random.randint(0, len(total_card_list) - 1) 
                card = total_card_list.pop(card_index)  # Gets The Random Card From Deck
                card_value = BlackJack.card_value[card]   # value for that card
                print(self.player_name + " Your Card : ", card)
                
                # condition to select the value of card either 1 or 11 if any card is ACE 
                if card == "Heart_A" or card == "Club_A" or card == "Spade_A" or card == "Diamond_A": 
                    while True:
                        val = int(input("Want Value as 1 or 11 : "))
                        if val == 1 or val == 11:
                            card_value = val
                            break
                        else:
                            continue

                self.score = self.score + card_value     # score of player

                print(player_name + " Your Score :", self.score)

            def double_down(self, player_name):
                ''' 
                DOUBLE DOWN MOVE in BlackJack Game
                '''
                self.bet = 2 * self.bet   # bets gets double amount
                self.player_name = player_name
                print(player_name + " Your Bet : " + str(self.bet))
                
                # condition : Which player do the DOUBLE DOWN move 
                if player_name == player1_name:
                    player1.hit(player1_name)  # to select any one card 

                elif player_name == player2_name:
                    player1.hit(player2_name)   # to select any one card

                elif player_name == player3_name:
                    player1.hit(player3_name)   # to select any one card


        class Player(BlackJack):    # player class which is child class of BlackJack 
            def __init__(self, bet, player_name):
                self.player_name = player_name   # player name
                self.bet = bet   # bet amount by that player
                card1_index = random.randint(0, len(total_card_list) - 1)
                card1 = total_card_list.pop(card1_index)
                # get 2 cards in first move
                card2_index = random.randint(0, len(total_card_list) - 1)
                card2 = total_card_list.pop(card2_index)
                print(self.player_name + " First 2 Cards : ", card1, card2)
                card1_value = BlackJack.card_value[card1]   # value for 1st card
                card2_value = BlackJack.card_value[card2]   # value for 2nd card
                # condition to select the value of card either 1 or 11 if any card is ACE 
                if card1 == "Heart_A" or card1 == "Club_A" or card1 == "Spade_A" or card1 == "Diamond_A":
                    while True:
                        val = int(input("Want Value as 1 or 11 : "))
                        if val == 1 or val == 11:
                            card1_value = val
                            break
                        else:
                            continue

                # condition to select the value of card either 1 or 11 if any card is ACE 
                if card2 == "Heart_A" or card2 == "Club_A" or card2 == "Spade_A" or card2 == "Diamond_A":
                    while True:
                        val = int(input("Want Value as 1 or 11 : "))
                        if val == 1 or val == 11:
                            card2_value = val
                            break
                        else:
                            continue

                self.score = card1_value + card2_value   # score for that player
                print(self.player_name + " Score : ", self.score)


        class Dealer(BlackJack): # dealer class which is child class of BlackJack
            def __init__(self):
                # get 1 card in first move for dealer
                card1_index = random.randint(0, len(total_card_list) - 1)
                card1 = total_card_list.pop(card1_index)
                print("Dealer's  First  Card : ", card1)
                card1_value = BlackJack.card_value[card1]   # value for that card

                # condition to select the value of card is 11 if card is ACE
                if card1 == "Heart_A" or card1 == "Club_A" or card1 == "Spade_A" or card1 == "Diamond_A":
                    card1_value = 11

                self.score = card1_value  # score of dealer
                print("Dealer's Score : ", self.score)

            def hit(self, player_name):
                ''' 
                HIT move for dealer 
                '''
                self.player_name = player_name
                card_index = random.randint(0, len(total_card_list) - 1)
                card = total_card_list.pop(card_index)
                card_value = BlackJack.card_value[card]
                print(self.player_name + " Your Card : ", card)

                # condition to select the value of card either 1 or 11 if any card is ACE
                if card == "Heart_A" or card == "Club_A" or card == "Spade_A" or card == "Diamond_A":
                    if self.score + card_value > 21:
                        card_value = 1
                    else:
                        card_value = 11


                self.score = self.score + card_value  # score of dealer

                print(player_name + " Your Score :", self.score)


        if num_players == 1:
            player1_name = str(input("Your Name :"))
            player1_bet = int(input("Bet Amount : "))
            print("\n\n")
            player1 = Player(player1_bet, player1_name)  # 1st object of Game 

        if num_players == 2:
            player1_name = str(input("Player1 Name :"))
            player1_bet = int(input("Bet Amount : "))

            player2_name = str(input("Player2 Name :"))
            player2_bet = int(input("Bet Amount : "))
            print("\n\n")

            player1 = Player(player1_bet, player1_name)  # 1st object of Game
            player2 = Player(player2_bet, player2_name)  # 2nd object of Game

        if num_players == 3:
            player1_name = str(input("Player1 Name :"))
            player1_bet = int(input("Bet Amount : "))

            player2_name = str(input("Player2 Name :"))
            player2_bet = int(input("Bet Amount : "))

            player3_name = str(input("Player3 Name :"))
            player3_bet = int(input("Bet Amount : "))
            print("\n\n")

            player1 = Player(player1_bet, player1_name)   # 1st object of Game
            player2 = Player(player2_bet, player2_name)   # 2nd object of Game
            player3 = Player(player3_bet, player3_name)   # 3rd object of Game

        dealer = Dealer()    # dealer object of game

        print('''Moves :-
        - HIT
        - STAY
        - DOUBLE DOWN''')

        # second move Onwards
        while True:   # runs till the game ends
            if player1:   # if player 1 is playing
                while True:
                    p1_chance = ''    # to over the move you will understand it ahead
                    if player1.score == 21:   # condition for blackjack
                        print(player1_name + " YOU ARE A BLACKJACK...")
                        break
                    elif player1.score > 21:  # condition for player bust
                        print(player1_name + " You are BUST and losses all bet")
                        p1_chance = 'over'
                        loss = player1.bet  
                        player1_amount = player1_amount - loss  # loss of player 1 
                        player1 = False   # player 1 game end

                        break   # no more moves for player 1
                    next_move = str(input(player1_name + " What's Your Next Move : "))  # next move of player 1
                    if next_move == 'HIT' or next_move == 'Hit' or next_move == 'hit':  # condition : player1 choose hit  
                        player1.hit(player1_name)   # call for hit function for player 1
                    elif next_move == 'STAY' or next_move == 'Stay' or next_move == 'stay':  # player choose to STAY     
                        p1_chance = 'over'
                        break   # no more moves for player 1
                    elif next_move == 'DOUBLE DOWN' or next_move == 'double down':   # 
                        player1.double_down(player1_name)
                        p1_chance = 'over'
                        break   # no more chance for player 1
                    else:
                        continue


                    if p1_chance == 'over':
                        break
                        
            # if player 2 is playing
            # all moves and functionality as Player 1 
            if player2:
                while True:
                    p2_chance = ''
                    if player2.score == 21:
                        print(player2_name + " YOU ARE A BLACKJACK...")
                        break
                    elif player2.score > 21:
                        print(player2_name + " You are BUST and losses all bet")
                        p2_chance = 'over'
                        loss = player2.bet
                        player2_amount = player2_amount - loss
                        player2 = False

                        break
                    next_move = str(input(player2_name + " What's Your Next Move : "))
                    if next_move == 'HIT':
                        player2.hit(player2_name)
                    elif next_move == 'STAY':
                        p2_chance = 'over'
                        break
                    elif next_move == 'DOUBLE DOWN':
                        player2.double_down(player2_name)
                        p2_chance = 'over'

                    if p2_chance == 'over':
                        break

            # if player 3 is playing
            # all moves and functionality as Player 1 and Player 2 
            if player3:
                while True:
                    p3_chance = ''
                    if player3.score == 21:
                        print(player3_name + " YOU ARE A BLACKJACK...")
                        break
                    elif player1.score > 21:
                        print(player3_name + " You are BUST and losses all bet")
                        p3_chance = 'over'
                        loss = player3.bet
                        player3_amount = player3_amount - loss
                        player3 = False

                        break
                    next_move = str(input(player3_name + " What's Your Next Move : "))
                    if next_move == 'HIT':
                        player3.hit(player1_name)
                    elif next_move == 'STAY':
                        p3_chance = 'over'
                        break
                    elif next_move == 'DOUBLE DOWN':
                        player1.double_down(player1_name)
                        p3_chance = 'over'

                    if p3_chance == 'over':
                        break
            break
            
        # all players played there chances
        # now its time for dealer to open his cards
        print(20 * "*")
        print("NOW IT'S DEALER's TURN")
        print(20 * "*")
        while True:
            if dealer.score < 17:
                dealer.hit("Dealer")   # dealer will keeps on adding card to his side till dealer score > 16
            else:
                break
        dealer_score = dealer.score   # dealer score after all cards added to dealer side

        if player1:   # if player 1 is in the game or not busted out
            p1_score = player1.score
            p1_bet = player1.bet
            p1_won = winning(player1_name, p1_score, p1_bet, dealer_score)  # call winning function & get loss or profit
            player1_amount = player1_amount + p1_won   # now final amount after loss or profit

        if player2:    # if player 2 is in the game or not busted out
            p2_score = player2.score
            p2_bet = player2.bet
            p2_won = winning(player2_name, p2_score, p2_bet, dealer_score)  # call winning function & get loss or profit
            player2_amount = player2_amount + p2_won   # now final amount after loss or profit

        if player3:    # if player 3 is in the game or not busted out
            p3_score = player3.score
            p3_bet = player3.bet
            p3_won = winning(player3_name, p3_score, p3_bet, dealer_score)  # call winning function & get loss or profit
            player3_amount = player3_amount + p3_won   # now final amount after loss or profit

        print("\n" + player1_name + " YOU HAVE TOTAL MONEY : ", player1_amount)
        if player2:
            print(player2_name + " YOU HAVE TOTAL MONEY : ", player2_amount)
        if player3:
            print(player3_name + " YOU HAVE TOTAL MONEY : ", player3_amount)

        break

    again = str(input("Press Enter To Play Again or Type 'Exit' To Exit : "))   # ask to play the game again
    if again == '':
        continue
    else:
        break
