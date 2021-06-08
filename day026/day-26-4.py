sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

#for word in sentence.split():
 # print(word)
# Write your code below:
result = {word:len(word) for word in sentence.split()}


print(result)

