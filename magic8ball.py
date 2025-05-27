#1/24/25
#Zaara Yousuf
#Magic 8 Ball

#Initialize
import random #Random library is imported so that computer can generate random responses
import time #Time libarary is imported so the computer can replicate the 8 ball shaking
responses = ["Yes!", "No!", "Most Likely", "Not Likely", "That's Impossible", "Don't Bet On It", "Of Course!", "There is a High Chance of This Happening", "Luck is On Your Side", "What You Want Will NOT Happen", "What You Want WILL Happen", "Not Really...", "Yes, Absolutely!", "The 8 Ball Has No Thoughts For This Question", "Eh...Maybe, or Maybe Not...", "Um. No Answer", "Yes, Yes, Yes! It's Going to Happen!"]  #Magic 8 Ball Responses found in an array

#Functions
def magic_8_ball(): #Main function to display the game
    print("\033[0;34mWelcome to the Magic 8 Ball Generator!\033[0m\n") #Displays welcome interface
    print("""
              ____
    ,dP9CGG88@b,
  ,IP  _   Y888@@b,
 dIi  (_)   G8888@b
dCII  (_)   G8888@@b
GCCIi     ,GG8888@@@
GGCCCCCCCGGG88888@@@
GGGGCCCGGGG88888@@@@...
Y8GGGGGG8888888@@@@P.....
 Y88888888888@@@@@P......
 `Y8888888@@@@@@@P'......
    `@@@@@@@@@P'.......
        ........
        """)
    while True: #Will forever loop the game
        print("\033[0;34mLet the Magic 8 Ball decide your fate...\033[0m\n")
        question = input("What is your question for the 8 Ball? ")
        check = question.endswith("?") #Checks the user's question to see if it ends with a question mark
        if check == True:
            print("shake...")#This sequence with the time and shakes replicates a magic 8 ball being shaken
            time.sleep(2)
            print("shake....")
            time.sleep(2)
            print("shake.....")
            time.sleep(2)
            print(random.choice(responses)) #Computer picks out a response from the list to display to the user
            another = input("Would you like to ask another question (yes) or quit playing (no)? ")
            if another == "no":
                print("\033[0;34mThe Magic 8 Ball has spoken...Goodbye!\033[0m\n")
                break #If user wants to quit playing, the loop will end
                        #Any other response will continue looping the game
        else:
            print("ERROR: Your question does not contain a question mark. Please re-enter the question. ") #Lets user re-submit their question if it misses a question mark


#Main
magic_8_ball() #Main function is called
