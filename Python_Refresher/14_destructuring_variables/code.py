# we use destructuring to split a collection int a separate variables

x, y = 4 , 5

job = [("Bob", 45, "Mechanic"), ("Asheley",12,"Student")]

for name , age, title in job:
    print(f"Name: {name}, age :{age} and is {title}")