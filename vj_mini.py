# my first mini-project to determine the winner of the game
# Rock-paper-lizard-scissor-spock


import random

def number_to_name(number):
    """Function to convert a number into its corresponding choice"""  
    
    if number==0:
        result="rock"
    elif number==1:
        result="Spock"
    elif number==2:
        result="paper"
    elif number==3:
        result="lizard"
    elif number==4:
        result="scissors"
    return result
    
def name_to_number(name):
       """Function to convert a choice to its corresponding number""" 
  
       if name=="rock":
            result=0
       elif name=="Spock":
            result=1
       elif name=="paper":
            result=2
       elif name=="lizard":
            result=3
       elif name=="scissors":
            result=4
       return result
        
 
def rpsls(name): 
        """Function to calculate the winner"""
    #Convert a name to number
        player_number=name_to_number(name)      
   #Generate computer choice
        comp_number=random.randrange(0,5)
   #calculate the winner
        number_diff=(player_number-comp_number)%5
      
        if number_diff==0:
            winner=0
        elif number_diff>2:
            winner=2
        else:
            winner=1  
          
    
        comp_name=number_to_name(comp_number)
    
    #Print the result 
        print "Player chooses " + name
        print "Computer chooses " + comp_name
        if winner==0:
            print "Player and computer tie!"
        elif winner==2:
            print "Computer wins!"
        else:
            print "Player wins!"
        print "\n"     
    

    
    # test cases
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")


