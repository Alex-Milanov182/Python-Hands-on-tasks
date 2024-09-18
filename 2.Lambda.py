string = 'This is a lAmBdA FuNction task'
string_split = string.split()
a = [1, 11, 23, 44, 16]
b = [2, 3, 5, 6, 7, 8, 44, 16]




################ 1

lambda_func = lambda n: [n, n.upper(), n.lower(), len(n)]

final_result = [lambda_func(i) for i in string_split]

print(final_result)




################ 2

def string_uppercase(n):
    return n.upper()

def string_lowercase(n):
    return n.lower()

def length_string(n):
    return len(n)

functions = [string_uppercase, string_lowercase, len]

results = [list(map(lambda func: func(i), functions)) for i in string_split]

print(results)



############## 3

numbers = list(filter(lambda x: x in a,b))
print(numbers)


############# 4 
string = 'This is a lAmBdA FuNction task'
split_string = string.split()

last_letter=sorted(split_string,key = lambda x:x[-1])
print(last_letter)

