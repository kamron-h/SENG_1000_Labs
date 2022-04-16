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
# # Get user input
# user_input = input().strip()
# # Create variable to hold reversed name
# name_backwards = ''
# # Split name
# name_b = user_input.split()
# # Join name WITHOUT spaces
# compare_name = ''.join(name_b)
#
# # Print name No-Spaces
# print(compare_name)  # <--- NOT NEEDED, COMMENT OUT BEFORE SUBMITTING
#
# # Append name in reverse to name_backwards
# for i in reversed(compare_name):
#     name_backwards += i
#
# # Print name reversed No-Spaces
# print(name_backwards)  # <--- NOT NEEDED, COMMENT OUT BEFORE SUBMITTING
#
# # Compare name w/ name.reversed
# if compare_name == name_backwards:
#     print(f'{user_input} is a palindrome')
# else:
#     print(f'{user_input} is not a palindrome')

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


# 8.16 LAB: Varied amount of input data
"""
Statistics are often calculated with varying amounts of input data. 
Write a program that takes any number of integers as input, and outputs the average and max. 

    Input :

       15 20 0 5
       
    Output :

       10 20
"""

# user_input = input().strip()
# ls_numbers = user_input.split()
# average = sum([int(i) for i in ls_numbers]) / len(ls_numbers)
# max = max([int(ii) for ii in ls_numbers])
#
# print(f'{average:.0f} {max:.0f}')


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


# 8.14.1: Report country population. (Completed)
"""
 Write a loop that prints each country's population in country_pop. 

    Input :

        China:1365830000,India:1247220000,United States:318463000,Indonesia:252164800

    Output :

        United States has 318463000 people.
        India has 1247220000 people.
        Indonesia has 252164800 people.
        China has 1365830000 people.

"""

# user_input = input()
# entries = user_input.split(',')
# country_pop = {}
#
# for pair in entries:
#     split_pair = pair.split(':')
#     country_pop[split_pair[0]] = split_pair[1]
#     # country_pop is a dictionary, Ex: { 'Germany':'82790000', 'France':'67190000' }
#     for country, pop in country_pop.items():
#     # country = split_pair[0]
#     # pop = split_pair[1]
#
#     print(country, 'has', pop, 'people.')


# 9.11.1: LAB: Car value (classes) (Completed)
"""
Complete the Car class by creating an attribute purchase_price (type int) 
and the method print_info() that outputs the car's information.

    Input :

        2011
        18000
        2018

    Output :

        Car's information:
           Model year: 2011
           Purchase price: 18000
           Current value: 5770
"""
# class Car:
#     def __init__(self):
#         self.model_year = 0
#         # TODO: Declare purchase_price attribute
#
#         self.current_value = 0
#
#     def calc_current_value(self, current_year):
#         depreciation_rate = 0.15
#         # Car depreciation formula
#         car_age = current_year - self.model_year
#         self.current_value = round(self.purchase_price * (1 - depreciation_rate) ** car_age)
#
#     # TODO: Define print_info() method to output model_year, purchase_price, and current_value
#      def print_info(self):
#            print(f"Car's information:\n   Model year: {self.model_year}")
#            print(f"   Purchase price: {self.purchase_price}\n   Current value: {self.current_value}")
#
#
# if __name__ == "__main__":
#     year = int(input())
#     price = int(input())
#     current_year = int(input())
#
#     my_car = Car()
#     my_car.model_year = year
#     my_car.purchase_price = price
#     my_car.calc_current_value(current_year)
#     my_car.print_info()


# 9.12.1: LAB: Nutritional information (classes/constructors) (Completed)
"""
Complete the FoodItem class by adding a constructor to initialize a food item. 
The constructor should initialize the name (a string) to "None" and all other instance attributes to 0.0 by default. 
If the constructor is called with a food name, grams of fat, grams of carbohydrates, 
and grams of protein, the constructor should assign each instance attribute with the appropriate parameter value.

The given program accepts as input a food item name, fat, carbs, and protein and the number of servings. 
The program creates a food item using the constructor parameters' default values and a food item using the input values. 
The program outputs the nutritional information and calories per serving for both food items.

    Input :

        M&M's
        10.0
        34.0
        2.0
        1.0

    Output :

        Nutritional information per serving of None:
           Fat: 0.00 g
           Carbohydrates: 0.00 g
           Protein: 0.00 g
        Number of calories for 1.00 serving(s): 0.00
        
        Nutritional information per serving of M&M's:
           Fat: 10.00 g
           Carbohydrates: 34.00 g
           Protein: 2.00 g
        Number of calories for 1.00 serving(s): 234.00
"""

# class FoodItem:
#     # TODO: Define constructor with parameters to initialize instance
#     #       attributes (name, fat, carbs, protein)
#     def __init__(self, name='None', fat=0, carbs=0, protein=0):
#         self.name = name
#         self.fat = fat
#         self.carbs = carbs
#         self.protein = protein
#
#     def get_calories(self, num_servings):
#         # Calorie formula
#         calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
#         return calories
#
#     def print_info(self):
#         print(f'Nutritional information per serving of {self.name}:')
#         print(f'   Fat: {self.fat:.2f} g')
#         print(f'   Carbohydrates: {self.carbs:.2f} g')
#         print(f'   Protein: {self.protein:.2f} g')
#
#
# if __name__ == "__main__":
#     food_item1 = FoodItem()
#
#     item_name = input()
#     amount_fat = float(input())
#     amount_carbs = float(input())
#     amount_protein = float(input())
#
#     food_item2 = FoodItem(item_name, amount_fat, amount_carbs, amount_protein)
#
#     num_servings = float(input())
#
#     food_item1.print_info()
#     print(f'Number of calories for {num_servings:.2f} serving(s): {food_item1.get_calories(num_servings):.2f}')
#
#     print()
#
#     food_item2.print_info()
#     print(f'Number of calories for {num_servings:.2f} serving(s): {food_item2.get_calories(num_servings):.2f}')


# 9.13 LAB: Artwork label (classes/constructors) (Completed)
"""
Define the Artist class with a constructor to initialize an artist's information and a print_info() method.
The constructor should by default initialize the artist's name to "None" and the years of birth and death to 0.
print_info() should display Artist Name, born XXXX if the year of death is -1 or Artist Name (XXXX-YYYY) otherwise.

Define the Artwork class with a constructor to initialize an artwork's information and a print_info() method.
The constructor should by default initialize the title to "None", the year created to 0,
and the artist to use the Artist default constructor parameter values.

    Input :

        Pablo Picasso
        1881
        1973
        Three Musicians
        1921

    Output :
        Artist: Pablo Picasso (1881-1973)
        Title: Three Musicians, 1921
        
        
    Input :

        Brice Marden
        1938
        -1
        Distant Muses 
        2000

    Output :
        Artist: Brice Marden, born 1938
        Title: Distant Muses, 2000
"""
# class Artist:
#
#     # TODO: Define constructor with parameters to initialize instance attributes
#     #       (name, birth_year, death_year)
#     def __init__(self, name='None', birth_year=0, death_year=0):
#         self.name = name
#         self.birth_year = birth_year
#         self.death_year = death_year
#
#     # TODO: Define print_info() method. If death_year is -1, only print birth_year
#     def print_info(self):
#         if self.death_year == -1:
#             print(f'Artist: {self.name}, born {self.birth_year}')
#         else:
#             print(f'Artist: {self.name} ({self.birth_year}-{self.death_year})')
#
#
# class Artwork:
#

#
#
# if __name__ == "__main__":
#     user_artist_name = input()
#     user_birth_year = int(input())  # TODO: Define constructor with parameters to initialize instance attributes
#     #       (title, year_created, artist)
#     def __init__(self, title='None', year_created=0, artist=Artist()):
#         self.title = title
#         self.year_created = year_created
#         self.artist = artist

    # TODO: Define print_info() method
    def print_info(self):
        self.artist.print_info()
        print(f'Title: {self.title}, {self.year_created}')
    user_death_year = int(input())
    user_title = input()
    user_year_created = int(input())
#
#     user_artist = Artist(user_artist_name, user_birth_year, user_death_year)
#
#     new_artwork = Artwork(user_title, user_year_created, user_artist)
#
#     new_artwork.print_info()


# 9.14 LAB: Triangle area comparison (classes) (Completed)
"""
Given class Triangle, complete the program to read and set the base and height
of triangle1 and triangle2, determine which triangle's area is larger, and 
output the larger triangle's info, making use of Triangle's relevant methods.

    Input :

        3.0
        4.0
        4.0
        5.0

Where 3.0 is triangle1's base, 4.0 is triangle1's height,
4.0 is triangle2's base, and 5.0 is triangle2's height, 
the OUTPUT :
    
        Triangle with larger area:
        Base: 4.00
        Height: 5.00
        Area: 10.00
"""
# class Triangle:
#     def __init__(self):
#         self.base = 0
#         self.height = 0
#
#     def set_base(self, user_base):
#         self.base = user_base
#
#     def set_height(self, user_height):
#         self.height = user_height
#
#     def get_area(self):
#         area = 0.5 * self.base * self.height
#         return area
#
#     def print_info(self):
#         print(f'Base: {self.base:.2f}')
#         print(f'Height: {self.height:.2f}')
#         print(f'Area: {self.get_area():.2f}')
#
#
# if __name__ == "__main__":
#     triangle1 = Triangle()
#     triangle2 = Triangle()
#
#     larger_triangle = Triangle()
#
#     # TODO: Read and set base and height for triangle1 (use set_base() and set_height())
#     triangle1.set_base(float(input()))
#     triangle1.set_height(float(input()))
#
#     # TODO: Read and set base and height for triangle2 (use set_base() and set_height())
#     triangle2.set_base(float(input()))
#     triangle2.set_height(float(input()))
#
#     # TODO: Determine larger triangle (use get_area())
#     if triangle1.get_area() < triangle2.get_area():
#         larger_triangle = triangle2
#     else:
#         larger_triangle = triangle1
#
#     print('Triangle with larger area:')
#     # TODO: Output larger triangle's info (use print_info())
#     larger_triangle.print_info()


# 9.15 LAB: Winning team (classes) (Completed)
"""
Complete the Team class implementation. For the instance method get_win_percentage(), 
the formula is:

    team_wins / (team_wins + team_losses)

    Input :

        Ravens
        13
        3 

    Output :
    
        Congratulations, Team Ravens has a winning average!
        
        
    Input :

        Angels
        80
        82 

    Output :
    
        Team Angels has a losing average.
"""
# class Team:
#     def __init__(self):
#         self.team_name = 'none'
#         self.team_wins = 0
#         self.team_losses = 0
#
#     # TODO: Define get_win_percentage()
#     def get_win_percentage(self):
#         percent = self.team_wins / (self.team_wins + self.team_losses)
#         return percent
#
#
# if __name__ == "__main__":
#
#     team = Team()
#
#     team_name = input()
#     team_wins = float(input())
#     team_losses = float(input())
#
#     team.team_name = team_name
#     team.team_wins = team_wins
#     team.team_losses = team_losses
#
#     if team.get_win_percentage() >= 0.5:
#         print('Congratulations, Team', team.team_name, 'has a winning average!')
#     else:
#         print('Team', team.team_name, 'has a losing average.')


# 9.16 LAB: Vending machine (Completed)
"""
Given two integers as user inputs that represent the number of drinks to buy and the number of bottles to restock, create a VendingMachine object that performs the following operations:

    Purchases input number of drinks
    Restocks input number of bottles
    Reports inventory

A VendingMachine's initial inventory is 20 drinks.

    Input :

        5
        2

    Output :
    
        Inventory: 17 bottles
"""
# class VendingMachine:
#     def __init__(self):
#         self.bottles = 20
#
#     def purchase(self, amount):
#         self.bottles = self.bottles - amount
#
#     def restock(self, amount):
#         self.bottles = self.bottles + amount
#
#     def get_inventory(self):
#         return self.bottles
#
#     def report(self):
#         print(f'Inventory: {self.bottles} bottles')
#
#
# if __name__ == "__main__":
#     # TODO: Create VendingMachine object
#     vm = VendingMachine()
#     # TODO: Purchase input number of drinks
#     vm.purchase(int(input()))
#     # TODO: Restock input number of bottles
#     vm.restock(int(input()))
#     # TODO: Report inventory
#     vm.report()


# 24.1 LAB: Simple car (Completed)
"""
Given two integers that represent the miles to drive forward and the miles to drive
in reverse as user inputs, create a SimpleCar object that performs the following operations:

    Drives input number of miles forward
    Drives input number of miles in reverse
    Honks the horn
    Reports car status


    Input :

        100
        4

    Output :
    
        beep beep
        Car has driven: 96 miles
"""
# class SimpleCar:
#     def __init__(self):
#         self.miles = 0
#
#     def drive(self, dist):
#         self.miles = self.miles + dist
#
#     def reverse(self, dist):
#         self.miles = self.miles - dist
#
#     def get_odometer(self):
#         return self.miles
#
#     def honk_horn(self):
#         print('beep beep')
#
#     def report(self):
#         print(f'Car has driven: {self.miles} miles')
#
#
# if __name__ == "__main__":
# # TODO: Create SimpleCar object
# car = SimpleCar()
# # TODO: Drive input number of miles forward
# car.drive(int(input()))
# # TODO: Drive input number of miles in reverse
# car.reverse(int(input()))
# # TODO: Honk the horn
# car.honk_horn()
# # TODO: Report car status
# car.report()


# 24.2 LAB: Calculator class (Completed
"""
In the file main.py write a class called Calculator that emulates basic functions of a calculator:

        add, subtract, multiply, divide, and clear.
        
The class has one attribute called value for the calculator's current value.

Implement the following methods as listed below:

    Default constructor method to set the attribute to 0.0
    add(self, val) - add the parameter to the attribute
    subtract(self, val)- subtract the parameter from the attribute
    multiply(self, val) - multiply the attribute by the parameter
    divide(self, val)- divide the attribute by the parameter
    clear(self) - set the attribute to 0.0
    get_value(self) - return the attribute

Given two float input values num1 and num2, the program outputs the following values:

    The initial value of the instance attribute, value
    The value after adding num1
    The value after multiplying by 3
    The value after subtracting num2
    The value after dividing by 2
    The value after calling the clear() method


    Input :

        10.0 
        5.0

    Output :
    
        0.0
        10.0
        30.0
        25.0
        12.5
        0.0
"""
# class Calculator:
#
#     # Type your code here.
#     def __init__(self):
#         self.num_1 = 0.0
#         self.num_2 = 0.0
#         self.val = 0.0
#
#     def add(self, value):
#         self.val += value
#         return self.val
#
#     def multiply(self, value):
#         self.val *= value
#         return self.val
#
#     def subtract(self, value):
#         self.val -= value
#         return self.val
#
#     def divide(self, value):
#         self.val /= value
#         return self.val
#
#     def clear(self):
#         self.val = 0.0
#
#     def get_value(self):
#         return self.val
#
# if __name__ == "__main__":
#
#     calc = Calculator()
#     num1 = float(input())
#     num2 = float(input())
#
#     # 1. The initial value
#     print(f'{calc.get_value():.1f}')
#
#     # 2. The The value after adding num1
#     calc.add(num1)
#     print(f'{calc.get_value():.1f}')
#
#     # 3. The value after multiplying by 3
#     calc.multiply(3)
#     print(f'{calc.get_value():.1f}')
#
#     # 4. The value after subtracting num2
#     calc.subtract(num2)
#     print(f'{calc.get_value():.1f}')
#
#     # 5. The value after dividing by 2
#     calc.divide(2)
#     print(f'{calc.get_value():.1f}')
#
#     # 6. The value after calling the clear() method
#     calc.clear()
#     print(f'{calc.get_value():.1f}')


# 24.3 LAB: Product class (Bonus Completed)
"""
In main.py define the Product class that will manage product inventory.
Product class has three attributes: a product code, the product's price, and the number count of product in inventory.

Implement the following methods:

    A constructor with 3 parameters that sets all 3 attributes to the value in the 3 parameters
    set_code(self, code) - set the product code (i.e. SKU234) to parameter code
    get_code(self) - return the product code
    set_price(self, price) - set the price to parameter price
    get_price(self) - return the price
    set_count(self, count) - set the number of items in inventory to parameter count
    get_count(self) - return the count
    add_inventory(self, amt) - increase inventory by parameter amt
    sell_inventory(self, amt) - decrease inventory by parameter amt

    Ex. If a new Product object is created with code set to "Apple",
    price set to 0.40, and the count set to 3, 
    the output is:

    Input :

        Name: Apple
        Price: 0.40
        Count: 3

    Output :
    
        0.0
"""
# class Product:
#     # Type your code here
#     def __init__(self, name_='', price_=0, num_=0):
#         self.name = name_
#         self.price = price_
#         self.num = num_
#         self.product_amt = 3
#
#     def set_code(self, code):
#         # set the product code (i.e. SKU234) to parameter code
#         self.name = code
#
#     def get_code(self):
#         return self.name
#
#     def set_price(self, price_amt):
#         # set the price to parameter price
#         self.price = price_amt
#
#     def get_price(self):
#         return self.price
#
#     def set_count(self, count):
#         # set the number of items in inventory to parameter count
#         self.num = count
#
#     def get_count(self):
#         return self.num
#
#     def add_inventory(self, amt):
#         self.num += amt
#
#     def sell_inventory(self, amt):
#         self.num -= amt
#

# if __name__ == "__main__":
#     name = 'Apple'
#     price = 0.40
#     num = 3
#     p = Product(name, price, num)
#
#     # Test 1 - Are instance attributes set/returned properly?
#     print('Name:', p.get_code())
#     print(f'Price: {p.get_price():.2f}')
#     print('Count:', p.get_count())
#
#     # Test 2 - Are attributes set/returned properly after adding and selling?
#     num = 10
#     p.add_inventory(num)
#     num = 5
#     p.sell_inventory(num)
#     print('Name:', p.get_code())
#     print(f'Price: {p.get_price():.2f}')
#     print('Count:', p.get_count())
#
#     # Test 3 - Do setters work properly?
#     name = 'Golden Delicious'
#     p.set_code(name)
#     price = 0.55
#     p.set_price(price)
#     num = 4
#     p.set_count(num)
#     print('Name:', p.get_code())
#     print(f'Price: {p.get_price():.2f}')
#     print('Count:', p.get_count())


# 24.4 LAB: Student class (Bonus Completed)
"""
In main.py define the Student class that has two attributes: name and gpa

Implement the following instance methods:

    A constructor that sets name to "Louie" and gpa to 1.0
    set_name(self, name) - set student's name to parameter name
    get_name(self) - return student's name
    set_gpa(self, gpa) - set student's gpa to parameter gpa
    get_gpa(self) - return student's gpa


    Ex. If a new Student object is created, the default output is:
    
        Louie/1.0
    
    Ex. If the student's name is set to "Felix" and the gpa is set to 3.7, the output becomes:
    
        Felix/3.7
"""
# class Student:
#     # Type your code here
#     def __init__(self):
#         self.name = 'Louie'
#         self.gpa = 1.0
#
#     def set_name(self, name):
#         # set student's name to parameter name
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#     def set_gpa(self, gpa):
#         # set student's gpa to parameter gpa
#         self.gpa = gpa
#
#     def get_gpa(self):
#         return self.gpa
#
# if __name__ == "__main__":
#     initial_student = Student()
#     print(initial_student.get_name(),'/', initial_student.get_gpa())
#
#     initial_student.set_name('Felix')
#     initial_student.set_gpa(3.7)
#     print(initial_student.get_name(), '/', initial_student.get_gpa())


# 24.5 LAB: Random values (Bonus Completed)
"""
In main.py define the RandomNumbers class, which has three integer attributes: var1, var2, and var3.
Write getter method for each attribute: get_var1(), get_var2() and get_var3().
Then write the following 2 instance methods:

    - set_random_values( ) - accepts a low and high integer values as parameters, and sets var1, var2, and var3 to
    random numbers within the range of the low and high input values (inclusive).
        
    - get_random_values( ) - prints out the 3 random numbers in the format: "Random values: var1 var2 var3"



    Input :
        
        15
        20

    Possible Output :
    
        Random values: 17 15 19
        
        
    where 17, 15, 19 can be any random numbers within 15 and 20 (inclusive).

Note: When submitted, your program will be tested against different input range to verify
if the three randomly generated values are within range.
"""
# from random import randint
#
# class RandomNumbers:
#     # Type your code here.
#     def __init__(self):
#         self.n1 = 0
#         self.n2 = 0
#         self.n3 = 0
#
#     def set_random_values(self, lw, hi):
#         self.n1 = randint(lw, hi)
#         self.n2 = randint(lw, hi)
#         self.n3 = randint(lw, hi)
#
#     def get_var1(self):
#         return self.n1
#
#     def get_var2(self):
#         return self.n2
#
#     def get_var3(self):
#         return self.n3
#
#     def get_random_values(self):
#         print(f'Random values: {self.n1} {self.n2} {self.n3}')
#
# if __name__ == "__main__":
#
#     low = int(input())
#     high = int(input())
#
#     numbers = RandomNumbers()
#     numbers.set_random_values(low, high)
#     numbers.get_random_values()