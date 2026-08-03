pet = input("Enter your pet : ")
year = int(input("Enter's the pets age : "))

if pet == "dog":
    if year <= 2:
        print("Puppy Dog Food")
    else:
        print("Aduld Dog Food")    

elif pet == "cat":
    if year >= 5:
        print("Senior Cat Food")
    else:
        print("litle Cat Food") 

else :
    print("Invaild Pet")                           