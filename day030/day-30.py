#To Find Errors
try:
  file = open("a_file.text")
  a_dictionary = {"key": "value"}
  print(a_dictionary["key"])

except FileNotFoundError:
  file = open("a_file.text", "w")
  file.write("something")

except KeyError as error_message:
  print(f"the key {error_message} dosen't exist")

else:
  content = file.read()
  print(content)

finally:
  file.close()
  #print("File was closed")