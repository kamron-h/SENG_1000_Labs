# This is a sample Python script.

import math
import binascii

# hours = int(input())
# minutes = int(input())
# V Variable below needed for convert_time() below also..
# seconds = int(input())

# hours = 0
# minutes = 0

# print('Seconds:', ((hours * 3600) + (minutes * 60) + seconds))

# print('Hours:', ((3600 / hours) + (minutes * 60) + seconds))

# print('Seconds: ', seconds, 'convert to', hours, 'hours and', minutes, 'minutes.')


# Convert Seconds into Hours:Minutes:Seconds
# def convert_time(secs) :
#
#     hours = secs // 3600
#     minutes = (secs % 3600) // 60
#     seconds = ((secs % 3600) % 60)
#
#
#     print('Hours:', hours)
#     print('Minutes:', minutes)
#     print('Seconds:', seconds)
#
#
#
# convert_time(seconds)


# Pizza Party Lab
# cost per pizza = 14.95
# cost per slice = 1.24583333
# # slices per person = 2
# def calculate_cost(people):
#     pizzas = m.ceil((float(people) * 2) / 12)
#     # extra_slices = ((float(people) * 2) % 12)
#     cost = pizzas * 14.95
#
#     print('Pizzas:', (pizzas))
#     print('Cost: ${:.2f}'.format(cost))
#
# # calculate_cost(int(input('How many people will be eating? ')))
# calculate_cost(int(input()))


# # Hypotenuse
# length_a = float(input())
# length_b = float(input())
#
# def hypot(a, b):
#
#     c = (a * a) + (b * b)
#
#     # print('Hypotenuse:', (math.sqrt(c)))
#     print('Hypotenuse: {:.2f}'.format(math.sqrt(c)))
#
#
# hypot(length_a, length_b)


# # 17.5 LAB 5: Area of a triangle
# a = float(input())
# b = float(input())
# c = float(input())
#
# def tri_area(a1, b1, c1):
#     s = float(a + b + c) / 2
#     area = math.sqrt(s * (s - a) * (s - b) * (s - c))
#
#     return area
# # print(area)
# print('The area of the triangle is: {:.3f}'.format(tri_area(a, b, c)))

# def tri_area(a, b, c):

# print('The area of the triangle is: {:.3f}'.format(area))


# tri_area(a, side_b, side_c)


# # 5.17.1: LAB: Print string in reverse
# exitWords = ['Done', 'done', 'd']
# word_list = []
# word_list2 = []
# x = 0
#
# while x == 0:
#     usrInput = str(input())
#     if usrInput not in exitWords:
#         # print('word not in list')
#         word_list.append(usrInput)
#     else:
#         # print('word is in list !!!')
#         for word in reversed(word_list):
#             word_list2.append(f'{word}')
#             word_list = word_list2
#         x = 1
#
#     # print(word_list)
# if x == 1:
#     for word in reversed(word_list):
#         print(f'{word[::-1]}')
#         x = 2


# if (usrInput != 'Done') or (usrInput != 'done') or (usrInput != 'd'):
#     word_list.append(str(usrInput))
#     print(word_list)
# else:
#     x = 1
#     print(reversed(word_list))
# if (usrInput == 'Done') or (usrInput == 'done') or (usrInput == 'd'):
#     print(reversed(word_list))

# HackerRank
# if __name__ == '__main__':
#     n = int(input().strip())
#     odd_even = n % 2
#
#     if (n <= 1) and (n <= 100):
#         if odd_even != 0:
#             print('Weird')
#         elif (odd_even == 0) and n in range(2, 6):
#             print('Not Weird')
#         elif (odd_even == 0) and n in range(6, 21):
#             print('Weird')
#         elif (odd_even == 0) and (n > 20):
#             print('Not Weird')

# HR
# n = int(input())
# x = 0
# ls = []
#
# while x == 0:
#
#     # if n == '':
#     if (n > 1) and (n < 20):
#         for i in range(0, n):
#             ls.append(i ** 2)
#
#     for o in ls:
#         print(o)
#     x = 1


# def is_leap(year):
#     leap = False
#
#     # Write your logic here
#     if (year >= 1900) and (year <= (10 ** 5)):
#         if (year % 4) == 0:
#             leap = True
#         if (year % 100) == 0:
#             leap = False
#         if (year % 400) == 0:
#             leap = True
#
#     return leap
#
#
# year = int(input())
# print(is_leap(year))

# # # 5.19 LAB: Adjust values in a list by normalizing
# num_input = int(input('Initial Input :'))
# num_list = []
# result = []
# results = []
#
# for i in range(1, num_input + 1):
#     floater = float(input('Floater Value: '))
#
#     num_list.append(floater)
#
#     max_result = max.__call__(num_list)
#
# for m in num_list:
#         z = (m / max_result)
#         print(f'{z:.2f}')


# def min_to_hours():
#     minute = float(input())
#     hours = float(minute / 60)
#     remainder = float(minute % 60)
#     print(f'Hours: {hours}\nMin: {minute}')
#
# min_to_hours()


# def calc_total_inches(num_feet, num_inches):
#     result = 12 * num_feet
#     return result + num_inches
#
# feet = int(input())
# inches = int(input())
# print('Total inches:', calc_total_inches(feet, inches))

# help(round)
#
# def calc_pyramid_volume(base_length, base_width, pyramid_height):
#     a = base_length * base_width
#     volume = (0.33 * a * pyramid_height)
#     return round(volume, 2)


# # 20.1 Home LAB 1: Count input length without spaces, periods, exclamation points, or commas
# sentence = str(input())
# bad_char = [' ', '.', '!', ',']
# ls = []
#
# for letter in sentence:
#     if letter not in bad_char:
#         ls.append(letter)
#
# print(len(ls))
# q = '57'
#
# print(q[0::-1])
# print(q[1::])
#
# if q[0::-1] != q[1::]:
#     print('true')
# else:
#     print('false')


# # 20.2.1: Home LAB 2: Countdown until matching digits
# x = int(input())
# ls = []
# z = 0
# e = 0
#
# while z == 0:
#
#     if (x > 10) and (x < 101):
#         ls.append(x)
#         a = x
#         b = a - 1
#         for i in range(x, 9, -1):
#             i_string = str(i)
#             if (i_string[0::-1] != i_string[1::]) and (z == 0):
#                 # print(int(i) - 1)
#                 ls.append(int(i) - 1)
#             else:
#                 z = 1
#         for number in ls:
#             print(number)
#     else:
#         while e == 0:
#             print('Input must be 11-100')
#             z = 1
#             e = 1


# # 20.3 Home LAB 3: Smallest and largest numbers in a list
# """Write a program that reads a list of integers into a list as
# long as the integers are greater than zero, then outputs the smallest
# and largest integers in the list."""
#
# end = False
# ls = []
#
# while not end:
#     x = int(input())
#     if x > 0:
#         ls.append(x)
#         if len(ls) > 1:
#             minimum = min(ls)
#             maximum = max(ls)
#     else:
#         print(f'{minimum} and {maximum}')
#         end = True


# # 20.4 Home LAB 4: Output values in a list below a user defined amount
# end = False
# ls = []
#
# while not end:
#     usrInput = int(input())
#     for i in range(0, usrInput):
#         x = int(input())
#         ls.append(x)
#     # print(ls)
#     for digit in ls:
#         last = ls[-1]
#         if digit < last:
#             print(f'{digit},', end='')
#     break


# # 20.5 Home LAB 5: Count multiples
# low = int(input())
# high = int(input())
# x = int(input())
# ls = []

# for i in range(low, high, x):
#     ls.append(x)
#     # print(x)
#     x += x
# print(len(ls))

#
# def count_multiples(l, h, xx):
#     for ii in range(l, h, xx):
#         ls.append(xx)
#         # print(x)
#         xx += xx
#     return(len(ls))


# # 4.7.2: If-else statements.
# car_year = int(input())
# if car_year < 1968:
#     print('Probably has few safety features.')
# if car_year > 1971:
#     print('Probably has head rests.')
# if car_year > 1992:
#     print('Probably has anti-lock brakes.')
# if car_year > 2001:
#     print('Probably has tire-pressure monitor.')


# # Must be >= 1
# num_insects = int(input())
# while (num_insects >= 0) and (num_insects <= 100):
#     print(num_insects, end=' ')
#     num_insects += num_insects


# # 5.14.1: LAB: Convert to reverse binary
# x = int(input())
# ls = []
# output = format(x, 'b')
#
# for i in reversed(output):
#     ls.append(i)
#     print(i, end='')


# # 5.15 LAB: Password modifier
# word = input()
# password = ''
# ls = []
#
# for letter in word:
#     if letter == 'i':
#         letter = '1'
#         ls.append(letter)
#     elif letter == 'a':
#         letter = '@'
#         ls.append(letter)
#     elif letter == 'm':
#         letter = 'M'
#         ls.append(letter)
#     elif letter == 'B':
#         letter = '8'
#         ls.append(letter)
#     elif letter == 's':
#         letter = '$'
#         ls.append(letter)
#     else:
#         ls.append(letter)
# for element in ls:
#     password += element
# print(password, end='!\n')

# # 5.16.1: LAB: Output range with increment of 5
# x = int(input())
# y = int(input())
#
# for i in range(x, (y + 1), 5):
#     if not x > y:
#         print(i, end=' ')
# if x > y:
#     print("Second integer can't be less than the first.", end='')
# print()


# 5.19.1: LAB: Adjust values in a list by normalizing
"""
When analyzing data sets, such as data for human heights or for human weights, 
a common step is to adjust the data. This adjustment can be done by 
normalizing to values between 0 and 1, or throwing away outliers.
For this program, adjust the values by dividing all values by the largest value. 
The input begins with an integer indicating the number of floating-point values that follow.
Output each floating-point value with two digits after the decimal point

    Input :
    
        5
        30.0
        50.0
        10.0
        100.0
        65.0
        
    Output :
    
        0.30
        0.50
        0.10
        1.00
        0.65
"""

# num_input = int(input())
# num_list = []
# max_result = 0
#
# for i in range(1, num_input + 1):
#     floater = float(input())
#     num_list.append(floater)
#     max_result = max.__call__(num_list)
#
# for m in num_list:
#     z = (m / max_result)
#     print(f'{z:.2f}')

# # 6.2.2: Function call with parameter: Printing formatted measurement.
# def print_feet_inch_short(num_feet, num_inches):
#     print(f'{num_feet}\' {num_inches}\"')
#
#
# user_feet = int(input())
# user_inches = int(input())
#
# print_feet_inch_short(user_feet, user_inches)


# 6.4.1: Functions: Factoring out a unit-conversion calculation.
"""
Write a function so that the main program below can be replaced by the 
simpler code that calls function mph_and_minutes_to_miles(). 
Original main program: 
"""


# miles_per_hour = float(input())
# minutes_traveled = float(input())


def mph_and_minutes_to_miles(mph, min_traveled):
    hours_traveled = min_traveled / 60.0
    miles_traveled = hours_traveled * mph

    return miles_traveled


# mph_and_minutes_to_miles(miles_per_hour, minutes_traveled)

# # 6.6.1: Function stubs: Statistics.
def get_user_num():
    n = int(input())
    print('FIXME: Finish get_user_num()')
    return n


def compute_avg(x, y):
    print('FIXME: Finish compute_avg()')
    return (x + y) / 2


user_num1 = 0
user_num2 = 0
avg_result = 0

# user_num1 = get_user_num()
# user_num2 = get_user_num()
# avg_result = compute_avg(user_num1, user_num2)

# print('Avg:', avg_result)


# # 6.7.3: Function with loop: Shampoo.
# def print_shampoo_instructions(num_cycles):
#     if num_cycles < 1:
#         print('Too few.')
#     elif num_cycles > 4:
#         print('Too many.')
#     else:
#         for i in range(num_cycles):
#             print(f'{i + 1} : Lather and rinse.')
#         print('Done.')
#
#
# user_cycles = int(input())
# print_shampoo_instructions(user_cycles)


# # 6.7.2: Function with branch: Popcorn.
# def print_popcorn_time(bag_ounces):
#     if bag_ounces < 3:
#         print('Too small')
#     elif bag_ounces > 10:
#         print('Too large')
#     else:
#         print(f'{6 * bag_ounces} seconds')


# # 6.12.1: Change order of elements in function list argument.
# values_list = ['quatrillion', 'is', 'more', 'than', 'gazillion']
#
# def swap(ls):
#     # Grab first element
#     first = ls[0]
#     # Grab second element
#     last = ls[-1]
#     ls[0] = last
#     ls[-1] = first
#     return ls
#
#
# values_list = input().split(',')  # Program receives comma-separated values like 5,4,12,19
# swap(values_list)
#
# print(values_list)


# 6.17.1: Function to compute gas volume. (Challenge Activity)
"""Define a function compute_gas_volume that returns the volume of a gas given parameters pressure,
temperature, and moles. Use the gas equation PV = nRT, where P is pressure in Pascals,
V is volume in cubic meters, n is number of moles, R is the gas
constant 8.3144621 ( J / (mol*K)), and T is temperature in Kelvin.

Sample output with inputs: 100.0 1.0 273.0 :

Gas volume: 22.698481533 m^3
"""

gas_const = 8.3144621


def compute_gas_volume(pressure, temperature, moles):
    result = (moles * gas_const * temperature) / pressure
    return result


# gas_pressure = float(input())
# gas_moles = float(input())
# gas_temperature = float(input())
# gas_volume = 0.0
#
# gas_volume = compute_gas_volume(gas_pressure, gas_temperature, gas_moles)
# print('Gas volume:', gas_volume, 'm^3')


# 6.19 LAB: Driving costs - functions
"""Write a function driving_cost() with input parameters miles_per_gallon, dollars_per_gallon,
    and miles_driven, that returns the dollar cost to drive those miles. All items are of type float.
    The function called with arguments (20.0, 3.1599, 50.0) returns 7.89975.

    Define that function in a program whose inputs are the car's miles per gallon and the price of gas
    in dollars per gallon (both float). Output the gas cost for 10 miles, 50 miles, and 400 miles,
    by calling your driving_cost() function three times.

    Input :
        20.0 - miles per gallon
        3.1599 - $_per_gallon
        50.0 - miles driven
    Output :
        1.58 7.90 63.20
    """

ls = []


def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    # Calculate the cost for x miles
    cost = round(float(miles_driven / miles_per_gallon) * dollars_per_gallon, 2)
    # return a float rounded 2 decimal places
    return cost


def total_driving_cost(current_mpg, current_gas_price):
    ls.append(driving_cost(current_mpg, current_gas_price, 10))
    ls.append(driving_cost(current_mpg, current_gas_price, 50))
    ls.append(driving_cost(current_mpg, current_gas_price, 400))
    for i in ls:
        print(f'{i:.2f}')


# mpg = float(input())
# gas_price = float(input())
#
# total_driving_cost(mpg, gas_price)


# 6.20 LAB: Step counter
"""A pedometer treats walking 1 step as walking 2.5 feet. 
Define a function named feet_to_steps that takes a float as a 
parameter, representing the number of feet walked, and returns 
an integer that represents the number of steps walked. 
Then, write a main program that reads the number of feet walked 
as an input, calls function feet_to_steps() 
with the input as an argument, and outputs the number of steps.

Use floating-point arithmetic to perform the conversion.

Input: 
    150.5
    
Output:
    60
"""


def feet_to_steps(nof):
    one_step = 2.5
    return round(nof / 2.5)


# number_feet_walked = float(input())
# total_steps = feet_to_steps(number_feet_walked)
# print(f'{total_steps:.0f}')


# 6.21 LAB: Convert to binary - functions
def int_to_reverse_binary(number: int):
    """
        Write a program that takes in a positive integer
        as input, and outputs a string of 1's and 0's representing
        the integer in binary.

        The program must define and call the following two functions.
        Define a function named int_to_reverse_binary() that takes an integer
        as a parameter and returns a string of 1's and 0's representing the
        integer in binary (in reverse). Define a function named string_reverse()
        that takes an input string as a parameter and returns a string
        representing the input string in reverse.

        Input:
            6

        Output:
            110

        def int_to_reverse_binary(integer_value)
        def string_reverse(input_string)
        """
    binary = format(number, 'b')
    bin_number = ''
    # print(digit)
    for i in reversed(str(binary)):
        bin_number += i
    bin_value = bin_number
    return bin_value


# def string_reverse(digit: str):
#     #     takes an input string as a parameter and returns a string
#     #     in reverse
#     rev_digit = ''
#     # print(digit)
#     for i in reversed(digit):
#         rev_digit += i
#     str_value = str(rev_digit)
#     return str_value


# user_input = int(6)
# print(string_reverse(int_to_reverse_binary(user_input)))


# 6.22 LAB: Swapping variables
# def swap_values(a: int, b: int, c: int, d: int):
#     a_0 = b
#     b_0 = a
#     c_0 = 9
#     d_0 = c
#
#     print(a_0, end=' ')
#     print(b_0, end=' ')
#     print(c_0, end=' ')
#     print(d_0)
#
#
# def read_integers(e: int, f: int, g: int, h: int):
#     swap_values(e, f, g, h)


# first = int(input())
# second = int(input())
# third = int(input())
# fourth = int(input())
#
# read_integers(4, 3, 6, 5)


# 7.2.1: Field width.
# N = int(input())


# def f(digit):
#     if digit > 0:
#         ls.append(1)
#     elif digit > 1:
#         ls.insert(1, 3)
#     elif digit > 2:
#         ls.remove(1)
#     elif digit > 3:
#         ls.pop()
#     elif digit > 4:
#         ls.reverse()
#     elif digit > 5:
#         print(ls.sort)
#     elif digit > 6:
#         ls.sort()


# f(N)


# 7.2.2: Format temperature output.
"""
Print air_temperature with 1 decimal point followed by C.

Input:
    36.4158102 
Output:
    36.4c
    
"""

# air_temperature = float(input())
# print(f'{air_temperature:.1f}', end='C')
# print()


# 7.3.2: Replace abbreviation
"""
Assign decoded_tweet with user_tweet, replacing any occurrence of 'TTYL' with 'talk to you later'.

    Input:
    
        'Gotta go. I will TTYL.'
        
    Output:

        Gotta go. I will talk to you later.
"""


# TODO: REVIEW OVER THIS!!
# user_tweet = input()
# decoded_tweet = user_tweet.replace('TTYL', 'talk to you later')
# print(decoded_tweet)


# Personal Code : Calculates the interest and commission rates
def commission_revenue(total_amount):
    total_commission = (total_amount * 0.05)
    return total_commission


def interest_revenue(total_amount):
    total_interest = (total_amount * 0.0045)
    return total_interest
    # total_commission = (total_amount * 0.05)
    # total = (total_interest + total_commission)
    # print(f'Escrow interest: {total_interest}')
    # print(f'Commission: {total_commission}')
    # return total_interest + total_commission


def revenue(amount):
    total = interest_revenue(amount) + commission_revenue(amount)
    return total


# 7.5.1: LAB: Checker for integer string
"""
Forms often allow a user to enter an integer. 
Write a program that takes in a string representing 
an integer as input, and outputs yes if every character 
is a digit 0-9. 
"""
# user_string = input()
#
# if user_string.isdigit():
#     print('yes')
# else:
#     print('no')


# 7.6 LAB: Name format
"""
Many documents use a specific format for a 
person's name. Write a program whose input is:

    firstName middleName lastName

and whose output is:

    lastName, firstInitial.middleInitial. 
"""

# name_initials = str(input())
#
# if (name_initials is not None) and name_initials.isdigit() == False:
#     split_name = name_initials.split(' ')
#     # print(f'{last}, {middle[0]}.{first[0]}.')
#     if len(split_name) < 3:
#         first = split_name[0]
#         last = split_name[1]
#         print(f'{last}, {first[0]}.')
#     else:
#         first = split_name[0]
#         middle = split_name[1]
#         last = split_name[2]
#         print(f'{last}, {first[0]}.{middle[0]}.')


# 7.7 LAB: Count characters
"""
Write a program whose input is a string which contains a character 
and a phrase, and whose output indicates the number of times the 
character appears in the phrase. The output should include the input 
character and use the plural form, n's, if the number of times the 
characters appears is not exactly 1.

    Input :

        n Monday

    Output :

        1 n
"""
#
# u_input = input().strip()
# count = 0
# # Grab the first character in string
# char = u_input[0]
#
# # Check each char in user-input for char occurrence
# # For each occurrence, increment count var
# for i in u_input:
#     # If char == char, increment
#     if i == char:
#         count += 1
#
# if count - 1 == 1:
#     # Check if count is == 1, if SO print without " 's "
#     print(f"{count - 1} {char}")
# else:
#     # Check if count is == 1, if NOT print with " 's "
#     print(f"{count - 1} {char}'s")


# 7.8 LAB: Mad Lib - loops
"""
Mad Libs are activities that have a person provide various words, 
which are then used to complete a short story in unexpected 
(and hopefully funny) ways.

Write a program that takes a string and an integer as input, and outputs 
a sentence using the input values as shown in the example below. 
The program repeats until the input string is quit and disregards 
the integer input that follows.

    Input :

        apples 5
        shoes 2
        quit 0

    Output :

        Eating 5 apples a day keeps the doctor away.
        Eating 2 shoes a day keeps the doctor away.

"""
#
# # Get user input, remove potential white spaces, & split.
# user_input = input().strip().split()
# # While input doesnt contain 'quit', request more input
# while 'quit' not in user_input:
#     # Get the word from the split-list
#     word = user_input[0]
#     # Get the integer from the split-list
#     integer = user_input[1]
#     # Print results
#     print(f'Eating {integer} {word} a day keeps the doctor away.')
#     # Ask user for more input for while loop reset
#     user_input = input().strip().split()


# 7.9 LAB: Palindrome (Completed)
"""
A palindrome is a word or a phrase that is the same when read both 
forward and backward. 

Examples are: "bob," "sees," or "never odd or even" (ignoring spaces). 

Write a program whose input is a word or phrase, and that outputs 
whether the input is a palindrome.

    Input :

        bob

    Output :

        bob is a palindrome

"""
# Get user input
user_input = input().strip()
# Create variable to hold reversed name
name_backwards = ''
# Split name
name_b = user_input.split()
# Join name WITHOUT spaces
compare_name = ''.join(name_b)

# Print name No-Spaces
print(compare_name)   # <--- NOT NEEDED, COMMENT OUT BEFORE SUBMITTING

# Append name in reverse to name_backwards
for i in reversed(compare_name):
    name_backwards += i

# Print name reversed No-Spaces
print(name_backwards)   # <--- NOT NEEDED, COMMENT OUT BEFORE SUBMITTING

# Compare name w/ name.reversed
if compare_name == name_backwards:
    print(f'{user_input} is a palindrome')
else:
    print(f'{user_input} is not a palindrome')


# 7.10 LAB: Remove all non-alpha characters
"""
Write a program that removes all non-alpha characters from the given input. 

    Input :

        -Hello, 1 world$!

    Output :

        Helloworld
        
"""
#
# user_input = str(input()).strip()
# word = ''
#
# for letter in user_input:
#     if letter.isalpha():
#         word += letter
# print(word)


# 8.1.2: Modify a list.
"""
Modify short_names by deleting the first element and changing the last element to Joe.

Sample output with input: 'Gertrude Sam Ann Joseph'

    Input :

        'Gertrude Sam Ann Joseph'

    Output :

        ['Sam', 'Ann', 'Joe']

"""

# user_input = input()
# short_names = user_input.split()
#
# del short_names[0]
# short_names[len(short_names) - 1] = 'Joe'
#
# print(short_names)


# 8.2.1: Reverse sort of list.
"""
Sort short_names in reverse alphabetic order.

    Input :

        'Jan Sam Ann Joe Tod'

    Output :

        ['Tod', 'Sam', 'Joe', 'Jan', 'Ann']
        
"""

# user_input = input()
# short_names = user_input.split()
# short_names.sort(reverse=True)
#
# print(short_names)


# 21.1 LAB: Track laps to miles
"""
One lap around a standard high-school running track is exactly 0.25 miles. 
Define a function named laps_to_miles that takes a number of laps as a parameter, 
and returns the number of miles. Then, write a main program that takes a number 
of laps as an input, calls function laps_to_miles() to calculate the number of miles, 
and outputs the number of miles.

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print(f'{your_value:.2f}')

    Input :

        7.6

    Output :

        1.90
"""
#
#
# def laps_to_miles(laps):
#     lap_eql_mile = 0.25
#     return laps * 0.25
#
#
# user_input = float(input().strip())
# print(f'{laps_to_miles(user_input):.2f}')


# 21.2 LAB: Max magnitude (Completed)
"""
Write a function max_magnitude() with three integer parameters that returns the largest magnitude value. 
Use the function in the main program that takes three integer inputs and outputs the largest magnitude value.

    Input :

        5,7,9

    Output :

        9
"""

# help(abs)
# lss_1 = []
# lss_2 = []
#
# def max_magnitude(u1, u2, u3):
#     # count = 0
#
#     lss_2.append(abs(u1))
#     lss_2.append(abs(u2))
#     lss_2.append(abs(u3))
#
#     lss_1.append(u1)
#     lss_1.append(u2)
#     lss_1.append(u3)
#
#     max_char = max(lss_2)
#
#     for element in lss_1:
#         if (element * -1) == max_char:
#             max_char = element
#
#     print(max_char)
#     return max_char
#
#
# print(max_magnitude(5, 7, -8))


# zyDE 8.2.1: Amusement park ride reservation system. [Extra Credit Activity]
# riders_per_ride = 3  # Num riders per ride to dispatch
#
# line = []  # The line of riders
# num_vips = 0  # Track number of VIPs at front of line
# name = ''
#
# menu = ('(1) Reserve place in line.\n'  # Add rider to line
#         '(2) Reserve place in VIP line.\n'  # Add VIP
#         '(3) Dispatch riders.\n'  # Dispatch next ride car
#         '(4) Print riders.\n'
#         '(5) Exit.\n\n')
#
# user_input = input(menu).strip().lower()
#
# while user_input != '5':
#     if user_input == '1':  # Add rider
#         name = input('Enter name:').strip().lower()
#         print(name)
#         line.append(name)
#
#         print(line)
#
#     elif user_input == '2':  # Add VIP
#         # print('FIXME: Add new VIP')
#         # Add new rider behind last VIP in line
#         # Hint: Insert the VIP into the line at position num_vips.
#         line.insert(num_vips, name)
#         line.pop()
#         # Don't forget to increment num_vips.
#         num_vips += 1
#         print(line)
#
#     elif user_input == '3':  # Dispatch ride
#         # print('FIXME: Remove riders from the front of the line.')
#         # Remove last riders_per_ride from front of line.
#
#         rev_line = []
#         count = 0
#         while count != 3:
#             count += 1
#             # Don't forget to decrease num_vips, if necessary.
#             if num_vips > 0:
#                 num_vips -= 1
#
#             for person in reversed(line):
#                 rev_line.append(person)
#
#
#             for ii in range(3):
#                 rev_line.pop()
#
#             for iii in range(1):
#                 for person_ in reversed(rev_line):
#                     line.append(person_)
#
#         print(line)
#
#     elif user_input == '4':  # Print riders waiting in line
#         print('{} person(s) waiting:'.format(len(line)), line)
#
#     else:
#         print('Unknown menu option')
#
#     user_input = input('Enter command: ').strip().lower()
#     print(user_input)

# 21.3 LAB: A jiffy (Completed)
"""
A "jiffy" is the scientific name for 1/100th of a second. Define a function named jiffies_to_seconds
that takes the number of "jiffies" as a parameter, and returns the number of seconds. 
Then, write a main program that reads the number of jiffies (float) as an input, calls function jiffies_to_seconds() 
with the input as argument, and outputs the number of seconds.

Output each floating-point value with three digits after the decimal point, which can be achieved as follows:

    Input :

        15.25

    Output :

        0.152

"""
# user_jiffies = float(input().strip())
#
#
# def jiffies_to_seconds(jiffies):
#     new_val = jiffies / 100
#     return new_val
#
#
# jifs = jiffies_to_seconds(user_jiffies)
# print(f'{jifs:.3f}')

# 21.4 LAB: Leap year - functions (Incomplete)
"""
A common year in the modern Gregorian Calendar consists of 365 days. 
In reality, Earth takes longer to rotate around the sun. 
To account for the difference in time, every 4 years, a leap year takes place. 

A leap year is when a year has 366 days: 
An extra day, February 29th. The requirements for a given year to be a leap year are:

1) The year must be divisible by 4

2) If the year is a century year (1700, 1800, etc.), the year must be evenly divisible by 400

Some example leap years are 1600, 1712, and 2016.

Write a program that takes in a year and determines the number of days in February for that year.


    Input :

        1712

    Output :

        1712 has 29 days in February. 
        
        
Your program must define and call the following function. 
The function should return the number of days in February for the input year.

def days_in_feb(user_year)
"""

# def days_in_feb(user_year):
#     leap_outcome = user_year % 4
#     century = user_year % 100
#
#     if century == 0:
#         if user_year == 1900:
#             return 28
#         elif user_year == 1600:
#             return 29
#     else:
#         if leap_outcome == 0:
#             print(leap_outcome)
#             return 29
#         else:
#             print(leap_outcome)
#             return 28
#
#
# year = int(input().strip())
# x = days_in_feb(year)
# print(f'{year} has {x} days in February.')


# 21.5 LAB: Exact change - functions (Completed)
"""
Define a function called exact_change that takes the total change
amount in cents and calculates the change using the fewest coins.
The coin types are pennies, nickels, dimes, and quarters.
Then write a main program that reads the total change amount as an integer input,
calls exact_change(), and outputs the change, one coin type per line.
Use singular and plural coin names as appropriate, like 1 penny vs. 2 pennies.

Output "no change" if the input is 0 or less.

Your program must define and call the following function. 
The function exact_change() should return num_pennies, num_nickels, num_dimes, and num_quarters.

def exact_change(user_total)


    Input :

        0

    Output :

        no change

    Input :

        45

    Output :

        2 dimes 
        1 quarter

"""

# def exact_change(user_total):
#     # divide qtrs into dollars
#     quarters = user_total // 25
#     # remainder (user_total % 25)
#     dimes = (user_total % 25) // 10
#     nickles = ((user_total % 25) % 10) // 5
#
#     pennies = user_total - (quarters * 25) - (dimes * 10) - (nickles * 5)
#
#     num_pennies = pennies
#     num_nickels = nickles
#     num_dimes = dimes
#     num_quarters = quarters
#
#     if num_pennies > 1:
#         print(f'{num_pennies} pennies')
#     elif num_pennies == 1:
#         print(f'{num_pennies} penny')
#
#     if num_nickels > 1:
#         print(f'{num_nickels} nickels')
#     elif num_nickels == 1:
#         print(f'{num_nickels} nickel')
#
#     if num_dimes > 1:
#         print(f'{num_dimes} dimes')
#     elif num_dimes == 1:
#         print(f'{num_dimes} dime')
#
#     return num_pennies, num_nickels, num_dimes, num_quarters
#
#
# user_input = int(input().strip())
#
# exact_change(user_input)


# 8.3.1: Get user guesses. (Completed)
"""
Write a loop to populate the list user_guesses with a number of guesses. 
The variable num_guesses is the number of guesses the user will have, which is read first as an integer. 
Read each guess (an integer) one at a time using int(input()). 

    Input :

        3
        9
        5
        2
        

    Output :

       [9, 5, 2]

"""

# num_guesses = int(input())
# user_guesses = []
# count = 0
#
# while count < num_guesses:
#     guess_input = int(input().strip())
#     user_guesses.append(guess_input)
#     count += 1
#
# print('user_guesses:', user_guesses)


# 8.3.2: Sum extra credit.

"""
Assign sum_extra with the total extra credit received given list test_grades. 
Iterate through the list with for grade in test_grades:. 
The code uses the Python split() method to split a string at each space into a 
list of string values and the map() function to convert each string value to an integer.

Full credit is 100, so anything over 100 is extra credit. 


    Input :

       101 83 107 90
       
    Output :

       8

"""

# user_input = input()
# # test_grades is an integer list of test scores
# test_grades = list(map(int, user_input.split()))
#
# sum_extra = 0  # Initialize 0 before your loop
#
#
# for index, test_grades in enumerate():
#
#
# print('Sum extra:', sum_extra)


# help(str)
# ingz = '90 92 94 95'
# user_input = input().strip()

# hourly_temperature = ingz.split()
#
# joined_temp = " -> ".join(hourly_temperature).strip()
#
# print(joined_temp, end=' \n')

# print(joined_temp)


# 8.17 LAB: Filter and sort a list (Completed)

"""
Write a program that gets a list of integers from input, 
and outputs non-negative integers in ascending order (lowest to highest).

    Input :

       10 -7 4 39 -6 12 2
       
    Output :

       2 4 10 12 39

"""

# num_input = input().strip()
# num_ls = list(map(int, num_input.split()))
# result = []
#
# # print(num_ls)
#
# sorted_nums = sorted(num_ls)
#
# for i in sorted_nums:
#     if i > -1:
#         result.append(i)
# for ii in result:
#     print(ii, end=' ')


# 8.18 LAB: Elements in a range (Completed)
"""
Write a program that first gets a list of integers from input. 
That list is followed by two more integers representing lower and upper bounds of a range. 
Your program should output all integers from the list that are within that range (inclusive of the bounds). 

    Input :

        25 51 0 200 33
        0 50

       
    Output :

        25 0 33

"""

# input_of_ints = input().strip()
# ls_of_ints = list(map(int, input_of_ints.split()))
#
# low_upper = input().strip()
# ls_lower_upper = list(map(int, low_upper.split()))
#
# for i in ls_of_ints:
#     if (i > ls_lower_upper[0] -1) and (i <= ls_lower_upper[1]):
#         print(i, end=' ')


# 8.19 LAB: Contact list (Completed)
"""
A contact list is a place where you can store a specific contact with other associated information such as a phone number,
email address, birthday, etc. Write a program that first takes in word pairs that consist of a name and a phone number 
(both strings), separated by a comma. That list is followed by a name, and your program should output the phone number
associated with that name. Assume the search name is always in the list.

    Input :

        Joe,123-5432 Linda,983-4123 Frank,867-5309
        
        Frank

       
    Output :

        867-5309

"""

# phone_entry = input().strip()
# indi_person = phone_entry.split()
# name_search = input().strip()
# ls = {}
#
# # print(indi_person)
#
# for i in indi_person:
#     name_number = i.split(',')
#     ls.update({name_number[0]: name_number[1]})
#
# if name_search in ls:
#     print(ls[name_search])


# 8.20.1: LAB: Car wash (Completed)
"""
Write a program to calculate the total price for car wash services. 
A base car wash is $10. A dictionary with each additional service and the corresponding cost has been provided. 
Two additional services can be selected. 
A '-' signifies an additional service was not selected. 
Output all selected services along with the corresponding costs and then the total price for all car wash services.

    Input :

        Tire shine
        Wax

       
    Output :

        ZyCar Wash
        Base car wash -- $10
        Tire shine -- $2
        Wax -- $3
        ----
        Total price: $15
        
        
    Input :

        Rain repellent
        -

       
    Output :

        ZyCar Wash
        Base car wash -- $10
        Rain repellent -- $2
        ----
        Total price: $12
        
"""

# services = {'Air freshener': 1, 'Rain repellent': 2, 'Tire shine': 2, 'Wax': 3, 'Vacuum': 5}
# base_wash = 10
# total = 0
#
# service_choice1 = input()
# service_choice2 = input()
#
# print('ZyCar Wash')
# print('Base car wash -- $10')
# if service_choice1 in services:
#     total += services[service_choice1]
#     print(f'{service_choice1} -- ${services[service_choice1]}')
#
# if service_choice2 in services:
#     total += services[service_choice2]
#     print(f'{service_choice2} -- ${services[service_choice2]}')
#
#
# print('----')
# print(f'Total price: ${total + base_wash}')


# 8.5.1: Print multiplication table. (Completed)
"""
Print the two-dimensional list mult_table by row and column.
On each line, each character is separated by a space. 

Hint: Use nested loops.

    Input :

        1 2 3,2 4 6,3 6 9

    Output :

        1 | 2 | 3
        2 | 4 | 6
        3 | 6 | 9

"""

# user_input = input()
# lines = user_input.split(',')
#
# # This line uses a construct called a list comprehension, introduced elsewhere,
# # to convert the input string into a two-dimensional list.
# # Ex: 1 2, 2 4 is converted to [ [1, 2], [2, 4] ]
#
# mult_table = [[int(num) for num in line.split()] for line in lines]
#
# for row in mult_table:
#     count = 0
#     for cell in row:
#         count += 1
#         print(cell, end=' | ' if count < len(mult_table) else '')
#     print()