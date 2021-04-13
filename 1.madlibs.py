# string concatenation (how to put strinfs together)
# suppose we want to create a string thet says "subscribe to ______"

#youtuber = "Nazim" # some string variable

# a few ways to do this
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")


adj = input("adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Femous person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time bexause \
I love to {verb1}. stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)