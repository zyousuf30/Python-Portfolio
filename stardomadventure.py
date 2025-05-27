#1/15/25
#Zaara Yousuf
#Semester 1 Final
#Stardom Adventure Game

#Init
#popstar_name = input("What is your Popstar Name?")
fan_base = 0 #Number of fans your popstar has
talent_score = 0 #Level of how much talent your popstar has
reputation = 0 #Level of good your popstar's reputation is
popstar_name = input("What is your Popstar Name? ") #In order to build up your star's story, you need to choose your popstar's name!

#Functions
def practice(): #This determines how your popstar will train and level up their skills
    global talent_score
    global popstar_name
    print("In order to become a successful popstar, you NEED to build up your skills and practice!")
    print(popstar_name + ", you can either practice singing, or you could practice dancing!")
    train = input("Will you sing (s) or dance (d) in the studio of your company?: ")
    if train == "s":
        print("Nice work! You practiced singing some new songs and built up strength in your voice!")
        talent_score = talent_score + 20
    else:
        print("You busted a few moves for future performances and ended memorizing them! Good job!")
        talent_score = talent_score + 25

def perform(): #This determines where your popstar decides to perform for a crowd and possibly gain new fans
    global fan_base
    print("Woah! You scored up 2 gigs! The problem is, you need to choose one or the other because they're both on the same day...")
    show = int(input("(1-2) Will you 1. Perform at a restaurant OR 2. Perform at a local music festival: "))
    if show == 1:
        print("You performed at a small town restaurant and managed to gain some new fans from residents!")
        fan_base = fan_base + 15
    else:
        print("Good job! " + popstar_name + " headlined a very small music festival in your town called Lollipopalooza! You accidentally messed up out of fear, but you had fun and gained new fans!")
        fan_base = fan_base + 10

def have_fun(): #This function allows your popstar to choose what to do during some free time they have; it may or may not boost your star's stats
    global talent_score
    global fan_base
    global reputation
    print("Looks like you have some free time! What will your popstar self do next outside of training to become a star?")
    fun = int(input("(1-3) 1.Go on Instagram Live to talk to fans and share your skills 2.Do an online photoshoot to gain attraction 3.Stare at a wall and do nothing instead of taking time for yourself: "))
    if fun == 1:
        print("You went on Instagram Live to talk about your drive to become famous. You ended up getting many new followers and support!")
        talent_score = talent_score + 15
        fan_base = fan_base + 45
        reputation = reputation + 30

    elif fun == 2:
        print("You got called up to do a photoshoot and interview by your favorite magazine! It got published for the world to see, too!")
        fan_base = fan_base + 75
        reputation = reputation + 50

    else:
        print("Well, you were very unproductive. Your fans want to see and hear you, you know...")
        talent_score = talent_score - 30
        fan_base = fan_base - 30
        reputation = reputation - 30

def rest(): #This displays your popstar's current stats in order to reach STARDOM
    global fan_base
    global talent_score
    global reputation
    print("Great idea! Take a good rest and see how you're doing as a future popstar!")
    print("Remember, if you want to become the ultimate popstar, you need to build up your popstar stats to the MAX...")
    print("Number of fans: " + str(fan_base))
    print("Your talent score: " + str(talent_score))
    print("Your reputation score: " + str(reputation))

def stardom_adventure(): #This is the final function that contains every other one and generates the Stardom Adventure game!
    while True:
        print("Welcome to Stardom Adventure!")
        print("Choose an activity so that you can work your way up to become a POPSTAR!")
        print("""
            1.Practice
            2.Perform at a Show
            3.Free Time!
            4.Rest(Display info)
            5.Quit Playing""")
        option = int(input("(1-5) Choose an Activity: ")) #Displays options for what player's popstar can do in this game
        if option == 1:
            practice()
        if option == 2:
            perform()
        if option == 3:
            have_fun()
        if option == 4:
            rest()
        if option == 5:
            break

    #These list out what happens when your popstar reaches certain levels in their stats
        if fan_base >= 100:
            print("Congrats! You went on a North American tour! Go be a STAR for your fans!")
        if talent_score >= 150:
            print("Your talent and skills have grown so much that you got to be signed by a label! Congrats!")
        if reputation >= 150:
            print("Woah! Your training has worked so well that your music and shows have gained so much recognition and many awards!")
            print("You just won a GRAMMY!! You're on the way to becoming an ULTIMATE POPSTAR!")
        if fan_base >= 200 and talent_score >= 200 and reputation >= 200:
            print("You have OFFICIALLY become a certified platinum artist! The WHOLE WORLD knows your name!")
            print("Congrats on becoming the ULTIMATE POPSTAR now, " + popstar_name + "!")
            print("Your story might have ended, but feel free to continue playing this game! Have fun! :)")

#Main
stardom_adventure()
