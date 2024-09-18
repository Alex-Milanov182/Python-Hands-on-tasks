
def split_decorator(func):
    def wrapper():
        data = func()
        return data.split()
    return wrapper


def uppercase_decorator(func):
    def wrapper():
        data = func()
        return [x.upper() for x in data]
    return wrapper


def words_decorator(func):
    def wrapper():
        data = func()
        return [i for i in data if len(i) >= 4]
    return wrapper 

def get_data():
    return 'This is An exAmPlE StRinG'

@words_decorator
@uppercase_decorator
@split_decorator
def decorators():
    return get_data()


result = decorators()
print(result)




