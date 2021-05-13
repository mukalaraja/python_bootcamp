################### Scope ####################

#enemies = 1

#def increase_enemies():
  ##print(f"enemies inside function: {enemies}")

##print(f"enemies outside function: {enemies}")


# black space
#game_level = 3
#enemies = ["aliens", "zombies", "skeleton"]
#if game_level < 5:
#  new_enemy = enemies[0]
#print(new_enemy)


#modifing global Scope

enemies = 1

def increase_enemies():
  print(f"enemies inside function: {enemies}")
  return enemies + 1

increase_enemies()
print(f"enemies outside function: {enemies}")

