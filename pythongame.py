# Python 3.9.6
#
# Author: Phil Marino
#
#
#Purpose:   Creating our first Python program together.
#           Demonstrating how to pass variables from function to function while producing a functional game.





def start(nice=0, mean=0, name=""):
    # get user's name
    name = describe_game(name)
    nice, mean, name = nice_mean(nice, mean, name)


def describe_game(name):
    """
        check if this is a new game or not.
        If it is new, get the new user's name.
        If it is not a new game, thank the player for
        playing again and continue with the game
    """
    #meaning, if we do not already have this user's name,
    #then they are a new player and we need to get their name
    if name != "":
        print("\nThank you for playing again, {}".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name> \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean")
                    stop = False
    return name



def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nYou approach a weary traveler in need.\nWill you help or keep on your adventure? (N/M) \n>>>: ").lower()
        if pick == "n":
            print("\nThe traveler thanks you and appears relieved for you compassion")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe The traveler lowers his head \nand continues in the opposite direction")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) # pass the 3 variables to the score()
        



def show_score(nice,mean,name):
    print("\n{}, your current total: \n ({}, Nice) and ({}, Mean)".format(name,nice,mean))
    


def score(nice,mean,name):
    # score function is being passed the values stored within the 3 variables
    if nice > 2:  # if condition is valid, call win function passing in the variables so it can use them
        win(nice,mean,name)
    if mean > 2:  # if condition is valid, call lose function passing in the variables so it can use them
        lose(nice,mean,name)
    else:         # else, call nice_mean function passing in the variables so it can use them
        nice_mean(nice,mean,name)
        

def win (nice,mean,name):
    print("\nNice job, {}, you win! \nEveryone loves you and you've \nmade lots of new friends along the way!".format(name))
    again(nice,mean,name)
    

def lose(nice,mean,name):
    # Substitute the {} wildcards with out variable values
    print("\nDamn too bad {}, you lose! \nEveryone hates you now!".format(name))
    # call again function and pass in our variable
    again(nice,mean,name)



def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'YES', ( N ) for 'NO':\n>>> ")


def reset(nice,mean,name):
    nice = 0
    mean = 0
    # Not resetting name variable because same user has selected to play again
    start(nice,mean,name)






if __name__ == "__main__":
    start()
