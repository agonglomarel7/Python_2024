# lets guess a number

number = 7 

start = input("Write 'y' if you wanr to play : ")

if (start in ("y", "Y")):
    guess_number = int(input("Enter your number : "))
    
    if (number==guess_number):
        print("You guess the correct number")
    else:
        print("You lose")