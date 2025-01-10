#Zaara
#10/17/24
#Nested IF Project

print("Welcome to Your Painting Name 2000")
print("Answer the Questions to Find Out Which Classic Painting You Are")
ans = input("cake (c) or ice cream (i) ?")
if ans == "c":
    ans = input("strawberries (str) or blueberries (blu) ?")
    if ans == "str":
        ans = input("mars (m) or venus (v) ?")
        if ans == "m":
            print("Your painting is The Scream!")
        else:
            print("Your painting is The Kiss!")
    if ans == "blu":
        ans = input("earth (e) or pluto (p) ?")
        if ans == "e":
            print("Your painting is Sunday Afternoon on the Island of La Grande Jatte!")
        else:
            print("Your painting is The Persistance of Memory!")
if ans == "i":
    ans = input("oranges (ora) or apples (app) ?")
    if ans == "ora":
        ans = input("stars (s) or sun(u) ?")
        if ans == "s":
            print("Your painting is The Starry Night!")
        else:
            print("Your painting is Sunflowers!")
    if ans == "app":
        ans = input("moon (o) or saturn (a) ?")
        if ans == "o":
            print("Your painting is Nighthawks!")
        else:
            print("Your painting is Mona Lisa!")
