from datetime import datetime


def print_time(task):
    print('Completed ' + str(task) + ' at ' + str(datetime.now()))


def get_initial(name, force_uppercase=True):
    initial = name[0:1]
    if force_uppercase:
        return initial.upper()
    else:
        return initial


first_name = input('Enter your first name : ')
last_name = input('Enter your last name : ')
print(f'Your initials are ' + get_initial(first_name) + get_initial(last_name)+'!')
print_time('forming initials')
print(f'Your email id is ' + get_initial(first_name, False) +
      get_initial(force_uppercase=False, name=last_name)+'@myemail.com')
print_time('forming emailID')
