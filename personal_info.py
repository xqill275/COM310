info = {'first_name': 'John', 'last_name': 'Doe', 'gender': 'male', 'username': 'user1234', 'password' : 'password1234'}

first_name = input("What is your first name?: ")
last_name = input("What is your last name?: ")
gender = input("what is your gender?: ")
username = input("What is your username?: ")
password = input("What is your password?: ")

info['first_name'] = first_name
info['last_name'] = last_name
info['gender'] = gender
info['username'] = username
info['password'] = password

for x in info:
    print(x, ":", info[x])
    