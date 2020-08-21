import random
from random import shuffle

secret_santas = ['Brendan', 'Hayden', 'Drew', 'Jacob', 'Pierce', 'Nick', 'Bryr', 'Michael', 'Mark F', 'Mark B', 'Jaymin', 'Tyler', 'Matt', 'JJ']

#Creating a function that takes the list of Santas and shuffles it into a random order.
def shuffle_list(secret_santas):
    shuffle(secret_santas)
    return(secret_santas)

#Creating a variable for the shuffled list.
secret_santas_shuffled = shuffle_list(secret_santas)


#Creating the group of partners from the list of secret santas
def partners(secret_santas):
    print('Group 1:' , (secret_santas_shuffled[0]) , 'and', (secret_santas_shuffled[1]))
    print('Group 2:' , (secret_santas_shuffled[2]) , 'and', (secret_santas_shuffled[3]))
    print('Group 3:' , (secret_santas_shuffled[4]) , 'and', (secret_santas_shuffled[5]))
    print('Group 4:' , (secret_santas_shuffled[6]) , 'and', (secret_santas_shuffled[7]))
    print('Group 5:' , (secret_santas_shuffled[8]) , 'and', (secret_santas_shuffled[9]))
    print('Group 6:' , (secret_santas_shuffled[10]), 'and', (secret_santas_shuffled[11]))
    print('Group 7:' , (secret_santas_shuffled[12]), 'and', (secret_santas_shuffled[13]))

#Entering the shuffled list into the function to be sorted and printed.
partners(secret_santas_shuffled)