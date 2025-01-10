#10/24/24
#Zaara - per. 3
#99 Bottles

#Init
def bottles():
    milk = 99
    while milk > 1:
        for i in range(98):
            print(str(milk) + " bottles of milk on the wall, " + str(milk) + " bottles of milk. You take one down, pass it around, " + str(milk - 1) + " bottles of milk on the wall!")
            milk = milk - 1
            if milk == 1:
                print(str(milk) + " bottle of milk on the wall, " + str(milk) + " bottle of milk. You take one down, pass it around, no more bottles of milk on the wall!")

    print("No more bottles of milk on the wall, no more bottles of milk. You take none down, pass none around, no more bottles of milk on the wall!")



#Main
bottles()
