# =============================================================================
# 
# Solitaire: Shamrocks card game
# A model of a card game using classes from cards.py file
# Algorithm:
#   loop until user wants to quit
#   call function to promt for option
#   call the specific function to display the data corresponding to the option
# =============================================================================

import cards, random
random.seed(100) #random number generator will always generate 
                 #the same 'random' number (needed to replicate tests)

MENU = '''     
Input options:
    MTT s d: Move card from end of Tableau pile s to end of pile d.
    MTF s d: Move card from end of Tableau pile s to Foundation d.
    U: Undo the last valid move.
    R: Restart the game (after shuffling)
    H: Display this menu of choices
    Q: Quit the game       
'''

  
def fix_kings(tableau):
    ''' 
    Fixes all the three-card piles with kings so that kings are at the left
    end of the pile. Returns nothing.
    tableau: A list of lists with cards to be processed (list)
    '''
   
    for cards_list in tableau: #goes through the lists in the master list
        i=0 #kings counter
        index=0 #index of king
        index2=0 #index of the card that is not king
        
        for card in cards_list: #goes through each card in a list
            a=card.__repr__() #creates a string representation of the card
            if 'K' in a:
                i+=1 #increases kings counter
                index=cards_list.index(card) #finds index of king
            else:
                index2=cards_list.index(card)
        if i==1: #if only one king, then inserts it in the beginning of list
            king=cards_list.pop(index)
            cards_list.insert(0,king)
        elif i==2: #if 2 kings, finds non-king card and inserts it at the end
            last_card=cards_list.pop(index2)
            cards_list.insert(2,last_card)
              
def initialize():
    '''
    It creates and initializes the tableau and foundation and, then returns
    them as a tuple, in that order.
    foundation: Empty list of four lists (list)
    tableau: List of 17 lists, each containing 3 of the dealt cards (except
        the 17th has only one card) (list)
    stock: Collection of 52 cards (object)
    Returns: master_tup (tuple)
    '''
    foundation = [[],[],[],[]]

    stock = cards.Deck() #creates a deck of 52 cards
    stock.shuffle() #shuffles the cards
    
    tableau = [[] for i in range(18)] #creates 18 empty lists
    
    for i in range(17): #goes through every list except for the last one
        for j in range(3): #goes through every list 3 times to add 3 cards
            tableau[i].append(stock.deal())
    tableau[-1].append(stock.deal()) #adds one card to the last list
    fix_kings(tableau)
    master_tup=(tableau, foundation)
    return master_tup

def get_option():

    '''
    It prompts the user for an option and checks that the input supplied by
    the user is of the form requested in the menu. If the input is not of the
    required form, the function prints an error message and returns None.
    Takes no parameters
    Returns: None if invalis option or list if valid option
    '''
    try:
        opt = input( "\nInput an option (MTT,MTF,U,R,H,Q): " )
        opt_list = opt.strip().split()
        letter = opt_list[0][0].upper() #makes the first character uppercase
        if letter in 'URHQ' and len(opt_list) == 1:
            return [letter] #return only one letter if input was u/r/q/h
        #if the first letter is M, the 2nd and 3rd elements are numbers and
        #lentgh of the list is 3 elements
        if letter == 'M' and opt_list[1].isdigit() and len(opt_list)==3 \
        and opt_list[2].isdigit(): 
            #option is the first element of the list, turns it into uppercase
            option = opt_list[0].upper()
            if option == 'MTT' or option == 'MTF' :
                #returns the list of string, int,int
                return [option, int(opt_list[1]), int(opt_list[2])]
        else: 
            print("Error in option:", opt)
            return None
    #prints error message in case some index does not exist
    except IndexError:
        print("Error in option:", opt)
        return None

          
def valid_tableau_to_tableau(tableau,s,d):
    '''
    Checks if the move tableau to tableau is possible
    tableau: List to be processed(list)
    s: Source from where the card is moving (int)
    d: Destination where the card is moving (int)
    Returns: bool
        
    '''
    
    try:
        my_card = tableau[s][-1] #takes the last card from the source tableau
        #if length of tableaua is 1 or 2 
        if len(tableau[d])!=0 and len(tableau[d]) <=2:
            #if suits agree or ranks agree which means that tab destination
            #card is lower or higher rank by one
            if my_card.suit() ==cards.Card.suit(tableau[d][-1]) \
                or my_card.rank()== cards.Card.rank(tableau[d][-1]) - 1 or \
                    my_card.rank() ==cards.Card.rank(tableau[d][-1]) + 1:
                    return True
    #returns false in case some index does not exist
    except IndexError:
        return False
    return False

    
def valid_tableau_to_foundation(tableau,foundation,s,d):
    ''' 
    Checks if the move tableau to foundation is possible
    tableau: List to be processed(list)
    foundation: List to be processed (list)
    s: Source from where the card is moving (int)
    d: Destination where the card is moving (int)
    Returns: bool 
    '''
    
    try:
        my_card = tableau[s][-1] #takes the last card from the source tableau  
        if len(tableau[s])!=0: 
            #if foundation is empty we can only move an ace
            if len(foundation[d])==0 and my_card.rank() ==1:
                return True
            #if suits and ranks agree and foundation rank is lower by one
            elif (foundation[d][-1].suit() == my_card.suit()) \
                and (my_card.rank() == foundation[d][-1].rank()+1):
                return True
    #returns false in case some index does not exist
    except IndexError:
        return False
    return False

    
    
def move_tableau_to_tableau(tableau,s,d):
    ''' 
    Moves a card from tableau to another tableau. Returns true if move is
    possible or false if move is invalid
    tableau: List to be processed(list)
    s: Source from where the card is moving (int)
    d: Destination where the card is moving (int)
    Returns: bool
    
    '''
    #if validation function returns true and the move is possible
    if valid_tableau_to_tableau(tableau, s, d):
        #deletes the last card of source and append to destination 
        tableau[d].append(tableau[s].pop())
        return True
    else:
        return False

def move_tableau_to_foundation(tableau, foundation, s,d):
    ''' 
    Moves a card from tableau to foundation. Returns true if move is
    possible or false if move is invalid
    tableau: List to be processed(list)
    foundation: List to be processed (list)
    s: Source from where the card is moving (int)
    d: Destination where the card is moving (int)
    Returns: bool
    
    '''
    #if validation function returns true and the move is possible
    if valid_tableau_to_foundation(tableau, foundation, s, d):
        #deletes the last card of source and appends to destination 
        foundation[d].append(tableau[s].pop())
        return True 
    else:
        return False

def check_for_win(foundation):
    ''' Checks for win. Returns true if user won, False if not
    foundation: List to be processed (list)
    '''
    for cards_list in foundation:
        if len(cards_list) == 13: #if foundation has all 13 cards of one suit
            pass
        else:
            return False
    return True 

def undo(moves,tableau,foundation):
    '''
    Undo the last move;
       Parameters:
           moves: the history of all valid moves. It is a list of tuples 
                  (option,source,dest) for each valid move performed since the 
                  start of the game. 
           tableau: the data structure representing the tableau.  
       Returns: Bool (True if there are moves to undo. False if not)
    '''
       
    if moves: # there exist moves to undo
        last_move = moves.pop()
        option = last_move[0]
        source = last_move[1]
        dest = last_move[2]
        print("Undo:",option,source,dest)
        if option == 'MTT':
            tableau[source].append(tableau[dest].pop())
        else: # option == 'MTF'
            tableau[source].append(foundation[dest].pop())
        return True
    else:
        return False

def display(tableau, foundation):
    '''Display the foundation in one row;
       Display the tableau in 3 rows of 5 followed by one row of 3.
       Each tableau item is a 3-card pile separated with a vertical bar.'''
    print("\nFoundation:")
    print(" "*15,end='') # shift foundation toward center
    # display foundation with labels
    for i,L in enumerate(foundation):
        if len(L)==0:
            # padding for empty foundation slot
            print("{:d}:    ".format(i),end="  ") 
        else:
            # display only "top" card
            print("{:d}: {} ".format(i,L[-1]),end="  ") 
    print()
    print("="*80)
    print("Tableau:")
    # First fifteen 3-card piles are printed; across 3 rows
    for i in range(15):
        print("{:2d}:".format(i),end='') # label each 3-card pile
        for c in tableau[i]:  # print 3-card pile (list)
            print(c,end=" ")
        print("    "*(3-len(tableau[i])),end='') # pad with spaces
        print("|",end="")
        if i%5 == 4: # start a new line after printing five lists
            print()
            print("-"*80)
    # Final row of only three 3-card piles is printed
    print(" "*15+"|",end='')  # shift first pile right
    for i in range(15,18):
        print("{:2d}:".format(i),end='') # label each 3-card pile
        for c in tableau[i]:
            print(c,end=" ")
        print("    "*(3-len(tableau[i])),end='') # pad with spaces
        print("|",end="")
    print()
    print("-"*80)
    

def main():  
    ''' Docstring '''
    print ("\nWelcome to Shamrocks Solitaire.\n")
    
    cards_tup=initialize()
    tableau=cards_tup[0]
    foundation=cards_tup[1]
    display(tableau, foundation)
    print (MENU)
    moves=[] #collects all valid moves into a list of tuples
    
    while True: #loops until user wants to quit with "Q"
        
        option=get_option() #promts for option
        
        if option !=None: #if the return value is not None and input is valid
            option[0]=option[0].upper()
            if option[0]=='MTT':
                s=option[1] #source from where card moves
                d=option[2] #destination where card moves
                
                #if validation function returns true and the move is possible
                if valid_tableau_to_tableau(tableau, s, d):
                    move_tableau_to_tableau(tableau, s, d) #moves a card
                    #collects a move in a tuple
                    move=(option[0], option[1], option[2]) 
                    moves.append(move) #adds move to the list of moves
                    
                    #if return value is True and user won
                    if check_for_win(foundation): 
                        print ("You won!")
                        display(tableau, foundation)
                        print("\n- - - - New Game. - - - -")   
                        #restart a game by initializing tableau and foundation
                        cards_tup=initialize() 
                        tableau=cards_tup[0]
                        foundation=cards_tup[1]
                        display(tableau, foundation)
                        print (MENU)
                    else:
                        #displays the board if user did not win
                        display(tableau, foundation)
                #else statement for when validation function return false
                else:
                    if s<0 or s>17:
                        print ("Error in Source.")
                    elif d<0 or d>17:
                        print ('Error in Destination.')
                    else:
                        #makes all elements in a list strings
                        error_option_string = [str(opti) for opti in option]
                        #prints a list as a string
                        print("Error in move: " +
                              ' , '.join(error_option_string))
            
            elif option[0]=='MTF':
                s=option[1]
                d=option[2]
                #if validation function returns true and the move is possible
                if valid_tableau_to_foundation(tableau, foundation, s, d):
                    move_tableau_to_foundation(tableau, foundation, s, d)
                    move=(option[0], option[1], option[2])
                    moves.append(move) #adds move to the list of moves
                    #if return value is True and user won
                    if check_for_win(foundation):
                        print ("You won!")
                        display(tableau, foundation)
                        print("\n- - - - New Game. - - - -")  
                        #restart a game by initializing tableau and foundation
                        cards_tup=initialize()
                        tableau=cards_tup[0]
                        foundation=cards_tup[1]
                        display(tableau, foundation)
                        print (MENU)
                    else:
                        #displays the board if user did not win
                        display(tableau, foundation)
                #else statement for when validation function return false
                else:
                    if s<0 or s>17:
                        print ("Error in Source.")
                    elif d<0 or d>3:
                        print ('Error in Destination.')
                    else:
                        #makes all elements in a list strings
                        error_option_string = [str(opti) for opti in option]
                        #prints a list as a string
                        print("Error in move: " +
                              ' , '.join(error_option_string))
            #undi the last valid move
            elif 'U' in option or 'u' in option:
                #if moves list is empty
                if not moves:
                    print ("No moves to undo.")
                else:
                    #call function to undo the last valid move
                    undo(moves, tableau, foundation)
                    display(tableau, foundation)
            
            #restarts the game
            elif 'R' in option or 'r' in option:
                cards_tup=initialize()
                tableau=cards_tup[0]
                foundation=cards_tup[1]
                display(tableau, foundation)
                print (MENU)
                
            elif "H" in option or 'h' in option: #displays the menu 
                print (MENU)
            elif 'Q' in option or 'q' in option: #quits the game
                print("Thank you for playing.")
                break
         
if __name__ == '__main__':
     main()
