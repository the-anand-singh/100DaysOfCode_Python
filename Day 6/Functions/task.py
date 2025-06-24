def greet_world():
    print('Hello, World!')

greet_world()

def get_user_name():
    return input('What is your name? ')

def greet_user():
    name = get_user_name()
    print(f'Hello, {name}')

greet_user()