# Vishleshan Company Ask me questions

# Q.1
li1 = [1,2,3,4]
li2 = [5,6,7,8]

# Write code for this output = [6,8,10,12]

output = []

for i in range(len(li1)):
    output.append(li1[i] + li2[i])

print(output)

# Q.2
li1 = [1,2,3,4]
li2 = [5,6,7,8]

# Write code for this output = [5,12,21,32]

output = []

for i in range(len(li1)):
    output.append(li1[i]*li2[i])

print(output)

# Q.3
li1 = [1,2,3,4]
li2 = [5,6,7,8]

# Write code for this output = [5,8,21,12]

output = []

for i in range(len(li1)):
    if i % 2 == 0:
        output.append(li1[i]*li2[i])
    else:
        output.append(li1[i]+li2[i])

print(output)
    

# Q.4 
li1 = [1,2,3,4]
li2 = [5,6,7,8]

# Write code for this output [1,2,3,4,[5,6,7,8]]

li1.append(li2)
print(li1)

# Q.5  
li1 = [1,2,3,4]
li2 = [5,6,7,8]

# Write code for this output [1,2,3,4,5,6,7,8]

li1.extend(li2)
print(li1)

# Q.6 Create decorator 

# The wrapper is simply: A new function that wraps around your original function.

# What is *args? *args = all positional arguments ✔ *args accepts ANY type of positional arguments (numbers, strings, lists, objects… anything)

# What is **kwargs? **kwargs = all keyword arguments **kwargs accepts ANY type of keyword arguments (values can also be anything — numbers, strings, lists, functions) 

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function runs")
        
        result = func(*args, **kwargs)
        
        print("After function runs")
        return result
    
    return wrapper
@my_decorator
def greet():
    print("Hello!")

greet()

def safety_decorator(func):
    def wrapper(*args, **kwargs):
        # Safety check
        for value in args:
            if value < 0: 
                return "Error: Negative numbers are not allowed!"
            
        return func(*args, **kwargs)
    
    return wrapper

@safety_decorator
def add(a, b):
    return a + b

print(add(10, 5))   # OK
print(add(-1, 5))   # ERROR


def require_login(func):
    def wrapper(user, *args, **kwargs):
        if not user.get("is_logged_in"):
            return "Access Denied! Please login."
        
        return func(user, *args, **kwargs)
    
    return wrapper

@require_login
def view_profile(user):
    return f"Welcome {user['name']}!"

user1 = {"name": "Nikhil", "is_logged_in": True}
user2 = {"name": "Guest", "is_logged_in": False}

print(view_profile(user1))  # allowed
print(view_profile(user2))  # denied


# Q.7 How you can retrieve name from database using ORM use filter but name first latter start from A

# Q.8 How you can retrieve name from database using ORM use filter but name first latter start from S


# Metaphi company ask me questions

# Q.1 write query to get the name of the employee who has the highest salary

# Q.2 write code for to get highest number from unorder list

# Q.3 what is diffrenece between blank=True and null=True

# Q.4 how you can create model for like there is many post and many likes also for one post many likes create schema for model 

# Q.5 List() vs Set()

# Q.6 what is Decorator work , create an Decorator 

# Q.7 Which python framework you use 

# Q.8  what is restframewok 

# Q.9 what is generic in djnago 