#3/13/25
#Closet Builder

#Initialize
closet = [] #Empty list allows for users to fill it up on their own and make their own "closet"
#"clothesinspo" is used so that users can search through a "library" of clothing options they may want to add as inspiration to their closet
clothesinspo = ["blouse", "jeans", "overalls", "t-shirt", "sweatshirt",
                "beanie", "earrings", "sneakers", "boots", "long-sleeve shirt",
                "zip-up hoodie", "sweatpants", "sandals", "high heels", "formal shoes",
                "baseball cap", "necklace", "bracelet", "dress", "suit",
                "shorts", "cargo pants", "boots", "wrist watch", "sunhat",
                "sunglasses", "scarf", "gloves", "glasses", "rings",
                "purse", "backpack", "belt", "necktie"]
#"outfits" carries images of outfits found online, and computer will randomly select one of the images to be displayed to the user
outfits =["https://assets.vogue.com/photos/67d36c0be9b09e9e688a202e/master/w_1600,c_limit/9PFW_FW25_STREETSTYLE_DAY5_PHILOH.jpg",
          "https://cdn.mos.cms.futurecdn.net/whowhatwear/posts/299752/colorful-outfit-ideas-299752-1702442597752-main-768-80.jpg.webp",
          "https://stylegirlfriend.com/wp-content/uploads/2024/01/willhalbert-fisherman-aesthetic.jpg",
          "https://assets.vogue.com/photos/66ec95f9a929f957f62a7b79/master/w_1600,c_limit/CPHFW%20FW23%20by%20STYLEDUMONDE0K3A5799FullRes.jpeg"]
#Image 1
#Website Name: VOGUE
#Author: Laura Jackson
#URL: https://www.vogue.com/article/fashion-week-trends
#Article Name: "Au Revoir Paris! 10+ Street Style Trends to Recreate"
#Date: 03/14/25

#Image 2
#Website Name: Who What Wear
#Author: Banna Girmay
#URL: https://www.whowhatwear.com/colorful-outfit-ideas
#Article Name: "Who Else Is on a "Sad Beige" Strike? These Colorful Outfits Are in My Rotation"
#Date: 12/20/23

#Image 3
#Website Name: Style Girlfriend
#Author: Megan Collins
#URL: https://stylegirlfriend.com/mens-fashion-trends/
#Article Name: "These are the 25 Best Men’s Fashion Trends to Try in 2025"
#Date: 01/21/25

#Image 4:
#Website Name: VOGUE
#Author: Christina Holevas
#URL: https://www.vogue.com/article/baggy-jean-outfits
#Article Name: "Intimidated by Baggy Jeans? Here Are 8 Effortless Ways to Style the Trend"
#Date: 08/20/24

import random #Random library is imported for the computer to randomly select images that will be displayed to the user
import time #Time library is imported so that text and images will be delayed before being dislayed onto the screen

#The following three lines were provided by my teacher previous to this project so that I could learn how to incorporate images into my code
from PIL import Image #These libraries are imported so that images can be developed in the Interactive Window
import requests
from io import BytesIO

#Functions
#This function enables the user to add items to their closet (unless they do not want to)
def addToCloset():

    item = input("What item would you like to add to your closet? (Press q if you would like to escape.)") #Gathers user's input into a variable containing what they type
    if item != "q": #If the user's input is NOT "q..."
        closet.append(item) #Adds user's input to "closet" array (parameter contains initial variable)
        print("\n") #Any line containing this print statement allows for outputs on screen to be spaced out and more visually appealing
        print("\033[1m" + item + "\033[0m" + " has been added to your closet.")
        #Use of "\033[1m" and "\033[0m" throughout the program was code provided by my school teacher to help bold words and add more visual appeal to the program
        time.sleep(3) #Any line containing "time.sleep(number)" will delay text or images for a certain number of seconds
        print("\n")

 #This function enables the user to remove items from their closet (unless they do not want to)
def takeFromCloset():
    removal = input("What item would you like to remove from your closet? (Press q if you would like to escape.)") #Gathers user's input into a variable containing what they type
    if removal != "q":
        closet.remove(removal) #Takes away user's input from "closet" array (parameter contains initial variable)
        print("\n")
        print("\033[1m" + removal + "\033[0m" + " has been removed from your closet.")
        time.sleep(3)
        print("\n")

#This function allows for the computer to display images to users
def open_image(url):

#The following three lines are code provided by my teacher previous to this project so that I could learn how to incorporate images into my code
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()

#This function enables computer to choose an image from the "outfits" array and display it as potential inspiration for the user when building their closet
def recommendOutfits():

    ask = input("Do you want a recommendation for a clothing item to be incorporated into your personal outfit? (yes) or (no) ")
    if ask == "yes": #If user chooses "no," they will be sent back to options screen
        image = random.choice(outfits) #Random function is called using the "outfits" list so that one of the indexes chosen gets stored in a variable
        open_image(image) #This function is called using the "image" variable as a parameter
        print("\n")
        print("This is a cool outfit to take inspiration from!")
        time.sleep(3)
        print("\n")

#This function lets the user see what currently is found inside their "closet" (the list itself)
def viewCloset():

    open_image("https://www.domino.com/wp-content/uploads/2021/07/02/painted-closet-ideas-domino-oyster-shoal.jpg?strip=all&quality=85")
    #Function is called with a link to an image of the inside of a closet as the parameter
#Image 5:
#Website Name: domino
#Author: Lydia Geisel
#URL: https://www.domino.com/content/painting-closet-doors/
#Article Name: "We Pinpointed the Swatches Behind Our Favorite Painted Closets"
#Date: 10/12/2018

    print("Here is your closet!")
    time.sleep(3)
    print("\n")
    print(closet)
    time.sleep(3)
    print("\n")

#This function enables the user to search for clothes in a curated list ("clothesinspo"); if the item they are looking for is available, they can add it to "closet"
def clothesSearch(answer):

    for i in range(len(clothesinspo)): #For-loop is used here to read each index of the "clothesinspo" array
        if answer.lower() in clothesinspo[i]: #If user's input--converted to lowercase--matches an index in the array...
            closet.append(clothesinspo[i]) #Add that item to the user's "closet" array
            print("The " + "\033[1m" + clothesinspo[i] + "\033[0m"
                  + " you wish to include has been added to your closet.")
            time.sleep(3)
    print("\n")

#This function is the main one that, when called, initiates the program to start
def closetBuilder():
    print("\033[1m" + "Welcome to the..." + "\033[0m")
    time.sleep(2)
    print("""
╔═╗┬  ┌─┐┌─┐┌─┐┌┬┐  ╔╗ ┬ ┬┬┬  ┌┬┐┌─┐┬─┐┬
║  │  │ │└─┐├┤  │   ╠╩╗│ │││   ││├┤ ├┬┘│
╚═╝┴─┘└─┘└─┘└─┘ ┴   ╚═╝└─┘┴┴─┘─┴┘└─┘┴└─o
          """) #Ascii text art taken from https://patorjk.com/software/taag/#p=display&f=Calvin%20S&t=Closet%20Builder!
    print("\n")
    time.sleep(4)
    print("Use this program to help you build your closet for any occasion--school, work, or just for a regular day with your favorite clothes!")
    print("\n")
    time.sleep(3)
    while True: #While loop is used so that the user can do options more than once--unless they are ready to end the program
        try: #"try" and "except" are for checking the user's input-
            #-if the input is NOT one of the following options, then the program will tell them that there is an error
            print("Please select one of the following options: ")
            print("1. Add to closet \n2. Take Away from Closet \n3. Find Clothes To Take Inspiration From \n4. Find Pictures of Outfits for Inspiration \n5. View Your Closet \n6. Quit")
            print("\n")
            option = int(input("Select a number between 1-6: ")) #Gets user's input
            if option == 1: #Depending on what option the user inputs, a specific function out of the others will be done and displayed to the user
                addToCloset()
            elif option == 2: #"if," "elif," and "else" statements separate functions from their options
                takeFromCloset()
            elif option == 3:
                print("Here you can search for basic clothes in the program's clothing library that you are interested in adding to your closet!")
                time.sleep(2)
                print("\nIf the item you are looking for is not found in the library, the program will take you back to the options page.")
                print("\n")
                time.sleep(3)
                answer = input("What kind of BASIC clothing item are you interested in including into your wardrobe?") #Input acts as the parameter for the function
                print("\n")
                clothesSearch(answer)
            elif option == 4:
                recommendOutfits()
            elif option == 5:
                viewCloset()
            else:
                print("\033[1m" + "----Thanks for using the Closet Builder!----" + "\033[0m") #Acts as an exit page saying "thank you" for using the "Closet Builder"
                print("\n")
                time.sleep(3)
                print("Wear what you want, & express yourself! :)")
                break #"break" completely ends the program by ending the while loop from being continuous
        except:
            print("ERROR: Please enter a number.") #Tells user that their input is not a number option listed
            time.sleep(4)
#Main
closetBuilder() #This is the final main function being called for program to initiate
