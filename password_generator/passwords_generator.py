#!/usr/bin/env python3
"""Program that takes two numbers and returns all possible combinations."""
# Given two digits for a four digit combination, output all combinaions from
# the two digits
# Prints out 14 combinations (minus the two (1111, 2222))


def display(password, reverse_password):
    print(f'normal: {password}, reverse: {reverse_password}')


def passwords_generator():
    inputs = ['1', '2']
    reverse_inputs = ['2', '1']
    length = 4
    combination_pairs = 7
    password = ''
    reverse_password = ''
    passwords = []
    checker = [1, 2, 3]
    count = 0
    while count < combination_pairs:
        if count == 0:
            i = 0
            while i < length:
                if i < checker[2]:
                    password += inputs[0]
                    reverse_password += reverse_inputs[0]
                if i == checker[2]:
                    password += inputs[1]
                    reverse_password += reverse_inputs[1]
                i += 1
            passwords.append(password)
            passwords.append(reverse_password)
            display(password, reverse_password)
            password = ''
            reverse_password = ''
            count += 1
        elif count == 1:
            i = 0
            while i < length:
                if i < checker[1]:
                    password += inputs[0]
                    reverse_password += reverse_inputs[0]
                if i in (checker[1], checker[2]):
                    password += inputs[1]
                    reverse_password += reverse_inputs[1]
                i += 1
            passwords.append(password)
            passwords.append(reverse_password)
            display(password, reverse_password)
            password = ''
            reverse_password = ''
            count += 1
        elif count == 2:
            i = 0
            while i < length:
                if i < checker[0]:
                    password += inputs[0]
                    reverse_password += reverse_inputs[0]
                if i < checker[2]:
                    password += inputs[1]
                    reverse_password += reverse_inputs[1]
                i += 1
            passwords.append(password)
            passwords.append(reverse_password)
            display(password, reverse_password)
            password = ''
            reverse_password = ''
            count += 1
        elif count == 3:
            i = 0
            while i < length:
                if i < checker[0] or i == checker[1]:
                    password += inputs[0]
                    reverse_password += reverse_inputs[0]
                if i in (checker[0], checker[2]):
                    password += inputs[1]
                    reverse_password += reverse_inputs[1]
                i += 1
            passwords.append(password)
            passwords.append(reverse_password)
            display(password, reverse_password)
            password = ''
            reverse_password = ''
            count += 1
        elif count == 4:
            i = 0
            while i < length:
                if i < checker[1] or i == checker[2]:
                    password += inputs[0]
                    reverse_password += reverse_inputs[0]
                if i == checker[1]:
                    password += inputs[1]
                    reverse_password += reverse_inputs[1]
                i += 1
            passwords.append(password)
            passwords.append(reverse_password)
            display(password, reverse_password)
            password = ''
            reverse_password = ''
            count += 1
        elif count == 5:
            i = 0
            while i < length:
                if i < checker[0] or i > checker[0]:
                    password += inputs[0]
                    reverse_password += reverse_inputs[0]
                if i == checker[0]:
                    password += inputs[1]
                    reverse_password += reverse_inputs[1]
                i += 1
            passwords.append(password)
            passwords.append(reverse_password)
            display(password, reverse_password)
            password = ''
            reverse_password = ''
            count += 1
        else:
            i = 0
            while i < length:
                if i < checker[0] or i > checker[1]:
                    password += inputs[0]
                    reverse_password += reverse_inputs[0]
                if i in (checker[0], checker[1]):
                    password += inputs[1]
                    reverse_password += reverse_inputs[1]
                i += 1
            passwords.append(password)
            passwords.append(reverse_password)
            display(password, reverse_password)
            password = ''
            reverse_password = ''
            count += 1
    print(f'{passwords}')


if __name__ == '__main__':
    passwords_generator()
