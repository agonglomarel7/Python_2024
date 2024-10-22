
# between set we can do on operations like intersection, union and many others

art = {"Ben","Jen","Cody","Messi"}
science = {"Messi","Lamine", "Jorge"}

# to know student who attend both art and science course

both = art.intersection(science)

print(both)
# to see student who attend art class but not science class

diff = art.difference(science)

print(diff)