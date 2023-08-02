import random
names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")

names_length = len(names)
random_index = random.randint(0, names_length - 1)

TheLoser = names[random_index]

print(f"{TheLoser} is going to buy the meal today!")



