import random

#esto es un cambio sin importancia
#para seguir la clase de freddy

##################################
#modificacion en el header
################################
#estos son otros cambios sin importancia hechos desde github
def decision():
    choice = input("If you want to continue playing write yes, if not, write no:  ")
    choice = choice.replace(" ","")
    choice = choice.lower()
    if choice == "yes":
        return True
    else:
        return False

def run():
    menu = """ Hello and welcome to my roullete.
       
    In this game you have to choose a random number between
    1 and 49, if you chose the correct number you
    win 50 times your bet. However, if you do not
    choose the correct number you loose all your bet.
    But, if you want to exit, you just have to write 
     """
    print(menu)
    money = 50 
    print("Oh by the way, you have " + str(money) + " to bet")
    random_number = random.randint(0,49)
    
    
    number = int(input("Please choose a number to bet: "))
    while number > 49:
        if number > 49:
            print("please choose a number between 1 and 49")
            number = int(input("introduce the new number: "))

    
    amount = int(input("Now, introduce the money you want to bet: "))    
    while amount > money:
        if amount > money:
            print("You do not have so much money")
            amount = int(input("Please introduce a valid lower than 50: "))


    while money > 0:
        if number == random_number:
            money = money * 50
            print("congratualtion!!!!, yoy have won, now you have " + str(money))
            if decision() == True:
                number = int(input("ok, let's keep playing, choose another number: "))
                while number > 49:
                    number = int(input("plase choose a number between 1 and 49: "))
                amount = int(input("write the money you want to bet: "))
                while amount > 50:
                    amount = int(input("you do not have so much money, please choose an amount you can afford: "))
            else:
                break
        elif number != random_number:
            money -= amount
            print("Oh, you have lost, your remaining money is " + str(money))
            if decision() == True:
                number = int(input("ok, let's keep playing, choose another number: "))
                while number > 49:
                    number = int(input("please choose a number between 1 and 49"))
                amount = int(input("write the money you want to bet: "))
                while amount > 50:
                    amount = int(input("plase choose something you can afford: "))
            else:
                break


    print("it was a pleasure to play with you!!, you now have: " + str(money))    
    print("Oh, the correct number was: " + str(random_number))


if __name__ == "__main__":
    run()



