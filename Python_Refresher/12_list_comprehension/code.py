# create a new list based on a preview list

numbers = [1,4,5,8,7,6]

doubled = []

for x in numbers:
    doubled.append(x*7)


# you can do it directly 

second_list = [ x*2 for x in numbers]

friends = ["John","Bob", "Basile", "Kami"]

start_s = [friend for friend in friends if friend.startswith("S")]

print(start_s)
