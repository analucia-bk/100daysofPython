"""You are going to write a program that will select a random name from a list of names. The person selected
 will have to pay for everybody's food bill."""
import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
random_name = names[random.randint(0, (len(names)-1))]
print(f"{random_name} is going to buy the meal today")
f