programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}
#print(programming_dictionary["Function"])

#adding new item:
programming_dictionary ["loop"] = "the action of doing something over and over again."
#print(programming_dictionary)

#create an empty dictionary:
#empty_dictionary = {}
#programming_dictionary ={}
#print(programming_dictionary)

#edit an item in dictionary:
programming_dictionary["Bug"] = "a moth in your computer."
#print(programming_dictionary)

#loops through a dictionary:
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])
