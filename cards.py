#Lab Assignment 12

from random import shuffle 

class Card:
    """Stores information about the suit, caste, and rank.

    Attributes:

    rank
        an int: (0,1,2,3,4,5,6,7,8,9)

    suit
        a str: "triangles", "squares", "pentagons"

        # pentagons > squares > triangles 

    caste
        a str: "royal" or "common"

        #Royal > Common

        #total of 60 cards

        Rules:
        1. Royal > common
        2. if castes == Castes, Suit determines which is higher
        3. Pentagons > squares > triangles
        4. if suit, caste == suit, caste , then rank decides which is higher 
        
    #Non Public"""


    def __init__(self, rank, caste, suit):
        """initializes self.

        Card, int, str, str -> None"""

        self._rank = int(rank)
        
        self._caste = str(caste)
        self._suit = str(suit)

    def __repr__(self):
        """returns a string of the form
        Card(rank, suit, caste)

        Card -> str"""
#iii
        

        return "Card(" + repr(self._rank) + ", " + repr(self._caste) + ", " + repr(self._suit) +   ")"

    def __str__(self):
        """returns a string of the form
        "rank of caste suit" 

        Card -> str"""

        return str(self._rank) + " " +  "of" + " " + self._caste + " " + self._suit

#ii



    def get_rank(self):
        """returns the rank as a integer

        Card -> int"""

        return self._rank

    def get_caste(self):
        """returns the caste of a caste a string

        Card -> str"""

        return self._caste

    def get_suit(self):
        """returns the suit of a card as a string

        Card -> str"""

        return self._suit

    def get_value(self):
        """Returns the value of a card as a tuple

        Card -> tuple-of-int"""

        #Example 5, "Royal", "Pentagon"

        #returns (100, 50, 5) 

        

        if self._caste == "Royal":
            self._caste = 100
        elif self._caste == "Common":
            self._caste = 0 

        if self._suit == "Triangle" or "Triangles":
            self._suit = 5
        elif self._suit == "Pentagon" or "Pentagons":
            self._suit =50

        elif self._suit == "Square" or "Squares":
            self._suit = 25
            

        self._rank 
    
        return (self._caste,  + self._suit,  + self._rank) 



#iv #compare operators


    def __gt__(self, other):
        """returns True if self (the first card) is larger than other (the next card)

        Card , Card - > bool"""
            
        
        return self.get_value() > other.get_value()

    
    def __lt__(self,other):
        """returns True if self (the first card) is smaller than other (the next card)

        Card , Card - > bool"""

        return self.get_value() < other.get_value()
        




class Deck:
    """stores a list of Cards

    Attributes:

    Cards
        (list of Cards)

    #non public"""

#Note: This is the long way, but it worked fine

   

    def __init__(self, Cards = None):
        """intializes self with a given (long) list of cards. If the list is empty,
        the deck is automatically loaded

        Deck[, Cards] -> None"""


        card1 = Card(9, "Royal", "Pentagon")     
        card2 = Card(8, "Royal", "Pentagon")
        card3 = Card(7, "Royal", "Pentagon")
        card4 = Card(6, "Royal", "Pentagon")
        card5 = Card(5, "Royal", "Pentagon")
        card6 = Card(4, "Royal", "Pentagon")
        card7 = Card(3, "Royal", "Pentagon")
        card8 = Card(2, "Royal", "Pentagon")
        card9 = Card(1, "Royal", "Pentagon")
        card10 = Card(0, "Royal", "Pentagon")

        card11 = Card(9, "Common", "Pentagon")   
        card12 = Card(8, "Common", "Pentagon")   
        card13 = Card(7, "Common", "Pentagon")
        card14 = Card(6, "Common", "Pentagon")
        card15 = Card(5, "Common", "Pentagon")
        card16 = Card(4, "Common", "Pentagon")
        card17 = Card(3, "Common", "Pentagon")
        card18 = Card(2, "Common", "Pentagon")
        card19 = Card(1, "Common", "Pentagon")
        card20 = Card(0, "Common", "Pentagon")

        card21 = Card(9, "Royal", "Triangle")  
        card22 = Card(8, "Royal", "Triangle")  
        card23 = Card(7, "Royal", "Triangle")  
        card24 = Card(6, "Royal", "Triangle")  
        card25 = Card(5, "Royal", "Triangle")  
        card26 = Card(4, "Royal", "Triangle")  
        card27 = Card(3, "Royal", "Triangle")  
        card28 = Card(2, "Royal", "Triangle")  
        card29 = Card(1, "Royal", "Triangle")  
        card30 = Card(0, "Royal", "Triangle")

        card31 = Card(9, "Common", "Triangle")  
        card32 = Card(8, "Common", "Triangle")  
        card33 = Card(7, "Common", "Triangle")  
        card34 = Card(6, "Common", "Triangle")  
        card35 = Card(5, "Common", "Triangle")  
        card36 = Card(4, "Common", "Triangle")  
        card37 = Card(3, "Common", "Triangle")  
        card38 = Card(2, "Common", "Triangle")  
        card39 = Card(1, "Common", "Triangle")  
        card40 = Card(0, "Common", "Triangle")

        card41 = Card(9, "Royal", "Square") 
        card42 = Card(8, "Royal", "Square") 
        card43 = Card(7, "Royal", "Square") 
        card44 = Card(6, "Royal", "Square") 
        card45 = Card(5, "Royal", "Square") 
        card46 = Card(4, "Royal", "Square") 
        card47 = Card(3, "Royal", "Square") 
        card48 = Card(2, "Royal", "Square") 
        card49 = Card(1, "Royal", "Square") 
        card50 = Card(0, "Royal", "Square")

        card51 = Card(9, "Common", "Square")
        card52 = Card(8, "Common", "Square")
        card53 = Card(7, "Common", "Square")
        card54 = Card(6, "Common", "Square")
        card55 = Card(5, "Common", "Square")
        card56 = Card(4, "Common", "Square")
        card57 = Card(3, "Common", "Square")
        card58 = Card(2, "Common", "Square")
        card59 = Card(1, "Common", "Square")
        card60 = Card(0, "Common", "Square")
        


        Deck_of_cards = [card1,card2, card3, card4, card5, card6, card7, card8, card9, card10, card11, card12, card13, card14, card15, card16, card17 , 
                         card18, card19, card20, card21, card22, card23, card24, card25, card26, card27, card28, card29, card30, card31, card32, card33, 
                         card34, card35, card36, card37, card38, card39, card40, card41, card42, card43, card44, card45, card46, card47, card48,
                         card50, card51, card52, card53, card54, card55, card56, card57, card58, card59, card60] 
       

        if Cards == None:
            self._Deck = Deck_of_cards
            

            
        else:
            self._Deck = Card
       
    

        

    def __repr__(self):
        """returns a string in the form
        Deck(self._Deck)

        Deck -> str"""
        
        return "Deck(" +  repr(self._Deck) + ")"

    def __str__(self):

        """returns a string in the form
            rank of caste suit

            Deck -> str """

        Card = ""

        
        
        for x in self._Deck:


            Card += str(x)

            

        return Card 

       
    
        

#GO BACK 


    


#  iii

    def shuffle(self):
        """shuffles a deck of cards and returns the result

        Deck -> None"""

        
        x = shuffle(self._Deck)


       

    def deal(self):
        """Removes the first Card from the Deck and returns that Card

        Deck -> Card -> Deck""" #think that's right

        x = self._Deck[0]

        self._Deck.remove(x)


 
        return x
        



    
        

       


    



    

