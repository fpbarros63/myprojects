"""
Author: Francisco de Paula Barros kjhlkjh

Purpose: Practice formatting strings.
"""
print('Please enter the following information:')
print('')
first_name = input('First name: ')
last_name = input('Last name: ')
email_address = input('email_address: ')
phone_number = input('Phone number: ')
job_title = input('Job title: ') 
id_number = input('ID Number: ')
hair = input('Hair color: ')
eyes = input('Eye color: ')
month = input('Starting Month:  ')
training = input('Completed additional training? ')

print('\nThe ID Card is:')
print('----------------------------------------')
print(f'{last_name.upper()}, {first_name.capitalize()}')
print(f'{job_title.title()}')
print(f'ID: {id_number.capitalize()}')
print ('')
print(f'{email_address.lower()}')
print(f'{phone_number.capitalize()}')
print('----------------------------------------/n')

width = 30#the width of string

hairN = f"Hair: {hair.capitalize()}"
print(f"{hairN: <{width}} Eyes: {eyes.capitalize()}")
monthN = f"Month: {month.capitalize()}"
print(f"{monthN: <{width}} Training: {training.capitalize()}")
