
import random
import string
import time
from datetime import timedelta
from datetime import datetime
from random import randrange
import csv




def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str




def random_date(start, end):

    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)



'''
Creating the two parametes we will use in the date function.
First one we specify the earliest date we want to have, 
the second one returns the currect date and time this will be max date we will be able to generate.
'''
d1 = datetime.strptime('1/1/1960 1:30 PM', '%m/%d/%Y %I:%M %p')
d2 = datetime.now()


# Random boolean function 
def random_bool():

    mylist = ['True','False']
    return random.choice(mylist)







# genertaor function 
def generator_func(n):
   
   for i in range(n): 
        yield [i, get_random_string(7), random_date(d1, d2) , random_bool()]
        

gen = generator_func(10)

     


import csv

with open('file.csv', mode = "w", newline='') as file1:
    #fieldnames = ['row', 'string', 'date', 'bool']
    
    writes = csv.writer(file1, delimiter=',',quotechar='"', quoting=csv.QUOTE_ALL) 
    writes.writerow(next(gen))
    writes.writerow(next(gen))
    writes.writerow(next(gen))
    writes.writerow(next(gen))
    writes.writerow(next(gen))
    writes.writerow(next(gen))
    writes.writerow(next(gen))
    writes.writerow(next(gen))
    writes.writerow(next(gen))
    writes.writerow(next(gen))
    



   

     
   
    
    #writes.writerows({"row": next(gen), "string": str(get_random_string(7)), "date":str(random_date(d1, d2)), "bool": str(random_bool())})

     
   

