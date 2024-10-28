
liste=[58,48,96,25,47]

amount = len(liste)

for i in range(5):
    print("Joyeux annif")

for sum in liste:
    sum+=sum

print (sum/amount)


enter = input('Would you like te play ? (Y/n)')

while enter != "n" :
    
    nbr = int(input("Enter a number"))
    if nbr > 5:
        print(f"{nbr} is greater than 5")


    enter = input('WOuld you like te play ? (Y/n)')

