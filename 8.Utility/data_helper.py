# data_helper.py

import random
import string
import time
from datetime import timedelta
from datetime import datetime
from random import randrange
import csv

def random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def random_date():
    d1 = datetime.strptime('1/1/1960 1:30 PM', '%m/%d/%Y %I:%M %p') #earliest_date we can use
    d2 = datetime.now() #current date
    delta = d2 - d1
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return d1 + timedelta(seconds=random_second)



def random_integer(min_value=0, max_value=100):
    return random.randint(min_value, max_value)

def random_double(min_value=0.0, max_value=100.0):
    return random.uniform(min_value, max_value)