from datetime import datetime, timedelta

nem = input('What is your name:')
print('hello '+nem)
# testing double quotes
print("Testing's boring!!")

sentence = 'testing String operations'
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.center(30,'*'))

first_name = input('First Name: ').capitalize()
last_name = input('Last Name: ').capitalize()
days_in_feb =28
print(f'Hello {first_name} {last_name} {days_in_feb}')

first_num = input('Enter first number:')
second_num = input('Enter second number:')
print(int(first_num) + int(second_num))
print(float(first_num) + float(second_num))

current_date = datetime.now()
print('Today is :: '+str(current_date))

one_day = timedelta(days=1)
yesterday = current_date-one_day

print('Yesterday day was :: '+str(yesterday.day))
print('Yesterday month was :: '+str(yesterday.month))
print('Yesterday year was :: '+str(yesterday.year))

birthday = input('Enter birthdate (dd/mm/yyyy) : ')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print('Birthday is '+str(birthday_date))

x=32
y=32

if (x==y & x*y==2):
    print('Success')
else:
    print('Lolled!')

#-------------------------------Exception handling
a =42
b =0

try:
    print(a/b)
except ZeroDivisionError as e:
    print('Divide by 0 not allowed!')
else:
    print('Something else went wrong!')
finally:
    print('Clean up code ran!')


#-----------------------------------Conditional
price = float(input('Enter the price: '))

if price<=5.00 or price in (15.00,24.00):
    tax= 0.07
else:
    tax =0.00
print(tax)

country = input('Enter your country : ').lower()

if country == "canada":
    province = input('Enter your province : ').lower()
    if province in ('alberta', 'nunavut', 'yukon'):
        tax = 0.005
    elif province == 'ontario':
        tax = 0.13
    else:
        tax = 0.15
else:
    tax= 0.0

print(tax)

#-------------------------------Dictionaries, Lists and Arrays
jobin = {}  # Dictionary i.e Map
jobin['first'] = 'Jobin'
jobin['second'] = 'Thomas'

jack = {'first': 'Jack', 'second': 'Frost'}
print(jobin)
print(jack)

people = [jobin, jack]  # List
people.append({'first': 'Bill', 'second': 'gates'})
print(people)

presenters = people[0:2]
print('No of presenters : ' + str(len(presenters)))
print('Presenters are : ' + str(presenters))

#----------------------------------------for loop
print('Printing each person using for loop:')
for person in people:
    print(person)

print('Printing each person using for range:')
for index in range(0, 3):
    print(people[index])

#------------------------------------------while loop
print('Printing using while loop:')
index = 0
while index < len(people):
    print(people[index])
    index = index + 1

key = int(input('Press 1 to add a new person or 2 to exit: '))
people = []

while(key == 1):
    person = input('Enter a new person: ')
    people.append(person)
    key = int(input('Press 1 to add a new person or 2 to exit: '))

print('All the people in the world: ')
for person in people:
    print(person)
    
