#Эта программка подставляет значения, написанные пользователями в историю, делая ее смешной и необычной

# The template for the story

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."


"Hello, my friend"
name = input("Enter a name: ")
adj1 = input ("One adjective pls: ")
adj2 = input ("One more pls: ")
adj3 = input ("And the last one: ")
verb1 = input ("After all, one verb pls: ")
noun1 = input ("I need one noun: ")
noun2 = input ("And one more: ")
animal = input ("Name an animal: ")
food = input ("One dish: ")
fruit = input ("favourite fruit: ")
shero = input ("best superhero: ")
country = input ("your country: ")
dessert = input ("sweety dessert: ")
year = input ("WW2 started year: ")

print (STORY % (name, adj1, adj2, animal, food, verb1, noun1, fruit, adj3, name, shero, name, country, name, dessert, name, year, noun2))