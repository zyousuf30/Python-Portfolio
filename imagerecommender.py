#2/26/25
#Zaara
#Random Image Recommender

#Init
from PIL import Image #From lines 6-8, these libraries are imported initally so that the computer can process images and requests to showcase those images found online
import requests
from io import BytesIO
import random #Random library is imported so computer can make random choices of which pictures are to be showcased on screen
import time #Time library is imported so that text can be displayed after a certain number of seconds
images = ["https://tinyurl.com/3n699t4v", "https://tinyurl.com/4htjdjrm", "https://tinyurl.com/bdhcma7t", "https://tinyurl.com/5ys6khmf", "https://tinyurl.com/4uwtrkeh"] #This is the array that stores all of the image URLs
#https://tinyurl.com/3n699t4v : Copenhagen, Denmark
#Website: Visit Copenhagen
#Author: @alisa_kb_ (Instagram)
#Date: 09/30/2024
#CC: Visit Copenhagen © 2025

#https://tinyurl.com/4htjdjrm : Grenada, Spain
#Website: España: Spain's Official Tourism Website
#Author: España Website
#Date: 2025
#CC: © Instituto de Turismo de España, TURESPAÑA

#https://tinyurl.com/bdhcma7t : Amsterdam, The Netherlands
#Website: I amsterdam
#Author: Koen Smilde
#Date: 2024
#CC: © 2024 I amsterdam

#https://tinyurl.com/5ys6khmf : Amalfi Coast, Italy
#Website: lonely planet
#Author: Marco Bottigeli/Getty Images
#Date: 02/07/25
#CC: © 2025 Lonely Planet

#https://tinyurl.com/4uwtrkeh : Vienna, Austria
#Website: UNESCO World Heritage Convention
#Author: Silvan Rehfeld
#Date: 27/08/2011
#CC: © Silvan Rehfeld

url = "" #Initial url variable is empty so it can get changed later

#Functions
def open_image(url): #This function allows for the computer to display images to users
    response = requests.get(url) #Lines 20-22 were taken from an example code for this assignment
    img = Image.open(BytesIO(response.content))
    img.show()

def image_descriptions(): #This function generates each corresponding descriptions depending on the image that's chosen to be displayed
    global url #Global variable allows for following code to use and change the url variable
    if url == "https://tinyurl.com/3n699t4v": #"if," "elif," and "else" statements determine the description depending on what image url is selected by the computer from the array
        print("\033[1m" + "Destination: " + "\033[1m" + "Copenhagen, Denmark") #The random numbers in between words makes the text bold
        print("\033[1m" + "Why HERE?: " + "\033[1m" + "It is known for its sustainable city; and the food is widely reknowned for being very delicious. The place itself runs through stunning rivers and historic neighborhoods.")
    elif url == "https://tinyurl.com/4htjdjrm":
        print("\033[1m" + "Destination: " + "\033[1m" + "Grenada, Spain")
        print("\033[1m" + "Why HERE?: " + "\033[1m" + "This is a lively city full of so much culture and excitement. It contains the historic UNESCO World Heritage Site Alhambra! The people are very friendly, and the sites are wonderful as there are many mountains surrounding the area.")
    elif url == "https://tinyurl.com/bdhcma7t":
        print("\033[1m" + "Destination: " + "\033[1m" + "Amsterdam, The Netherlands")
        print("\033[1m" + "Why HERE?: " + "\033[1m" + "This is a sustainable city; most people don't drive and prefer to ride bikes! The architecture is known for being very cute and historic. There are many places to explore both within the capital and outside of the city!")
    elif url == "https://tinyurl.com/5ys6khmf":
        print("\033[1m" + "Destination: " + "\033[1m" + "Amalfi Coast, Italy")
        print("\033[1m" + "Why HERE?: " + "\033[1m" + "This area of Italy actually consists of many villages and towns that lie along the coast of the Amalfi. They are known for being very scenic and beautiful as they sit right along beaches and views of the ocean.")
    else:
        print("\033[1m" + "Destination: " + "\033[1m" + "Vienna, Austria")
        print("\033[1m" + "Why HERE?: " + "\033[1m" + "Vienna consists of lots of history and culture. The architecture is a blend of Gothic and Baroque; people can explore a fairytale-like city full of so much character!")

def random_image_recommender(): #This is the main function that contains introduction to code and the functions that let user see new places!
    print("Welcome to the Random European Places Generator!")
    time.sleep(4) #Time.sleep is used so text is displayed after certain number of seconds
    print("Here you will be able to learn about different places across Europe that you should travel to...")
    time.sleep(4)
    print("...including IMAGES of these places!")
    time.sleep(4)
    while True: #While loop allows for the computer to constantly pick images if user does not want to end program
        print("generating image...")
        url = random.choice(images) #random function allows for the image to be selected at random
        time.sleep(5)
        open_image(url) #Contains url parameter
        image_descriptions()
        time.sleep(10)
        try: #Try and except function allows for user to re-input their answer to the question if there's an error to their spelling
            next = input("Would you like to see another recommended place? (yes) or (no)")
            if next == "no":
                break #Ends the while loop and program
        except:
            print("ERROR: You must enter either 'yes' or 'no' to determine if you want to continue.")
#Main
random_image_recommender() #Main function is called so program can be used



