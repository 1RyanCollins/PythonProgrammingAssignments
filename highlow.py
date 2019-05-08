#High/low Game Script

#Rules for High/Low 
#        1. Royal > common
#        2. if castes equal Castes, Suit determines which is higher
#        3. Pentagons > squares > triangles
#        4. if suit and caste equal suit and caste , then rank decides which is higher

from cards import (Card, Deck)

counter_user = 0
counter_computer = 0 


print("Let's a Round of High / Low")


print("\n")



    #create a new deck 
New_Deck = Deck()

print("I am shuffling the deck")

print("\n")

    #shuffles the deck
New_Deck.shuffle()



    #deal a card

print("Here's your card: ") 
Dealthis = New_Deck.deal()
print(Dealthis)

    
print("\n")    

   

print("Is the next card higher or lower?")
print("Please type in 'lower', 'higher', 'Lower', or 'Higher'")
user_input = input()

print("\n")

Dealthisagain = New_Deck.deal()
print("Your Card: ")
print(Dealthisagain)


if user_input.lower() == "lower" and Dealthis > Dealthisagain:
    print("You win")                        #1          #2

elif user_input.lower() == "higher" and Dealthis < Dealthisagain:
    print("You win")

elif user_input.lower() == "lower" and Dealthis < Dealthisagain:
    print("You lose")

elif user_input.lower() == "higher" and Dealthis > Dealthisagain:
    print("You lose")

print("\n")

print("Good Game!")















      


