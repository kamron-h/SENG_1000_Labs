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
#
# for i in range(low, high, x):
#     ls.append(x)
#     # print(x)
#     x += x
# print(len(ls))


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


# # 6.2.2: Function call with parameter: Printing formatted measurement.
# def print_feet_inch_short(num_feet, num_inches):
#     print(f'{num_feet}\' {num_inches}\"')
#
#
# user_feet = int(input())
# user_inches = int(input())
#
# print_feet_inch_short(user_feet, user_inches)


# # 6.6.1: Function stubs: Statistics.
# def get_user_num():
#     n = int(input())
#     print('FIXME: Finish get_user_num()')
#     return n
#
#
# def compute_avg(x, y):
#     print('FIXME: Finish compute_avg()')
#     return (x + y) / 2
#
#
# user_num1 = 0
# user_num2 = 0
# avg_result = 0
#
# user_num1 = get_user_num()
# user_num2 = get_user_num()
# avg_result = compute_avg(user_num1, user_num2)
#
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
    total_steps = nof / 2.5
    print(f'{total_steps:.0f}')


number_feet_walked = float(input())
# 6.21 LAB: Convert to binary - functions
# feet_to_steps(number_feet_walked)


# 6.21 LAB: Convert to binary - functions

# 7.2.1: Field width.
