#Importing Random
from random import shuffle

# Edit names.txt to change the names and amount of groups
secret_santas = open("names.txt").read().split()


def partners(secret_santas):
    number_of_people = len(secret_santas)
    number_of_groups = number_of_people / 2
    if number_of_people % 2 == 1: 
        raise ValueError("# of participants must be even.")
    for group in range(int(number_of_groups)):
        group_number = group + 1
        first_index =  group * 2
        second_index = group * 2 + 1        
        print(f"Group {group_number}: {secret_santas[first_index]} and {secret_santas[second_index]}")
        

print('-----Presenting The 2020 Gift Exchange Groups!-----\n')
#Shuffling list and creating groups
shuffle(secret_santas)
partners(secret_santas)

print('\n----------Have Fun!----------\n')