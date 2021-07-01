#Imports needed to create this Calculator.
from statistics import variance, mean, median, median_high, median_low, mode, geometric_mean, harmonic_mean
import math

#A list to hold the numbers.
numbers_list = []

#A loop enabling a calculation after calculation.
while True:
    #A place to enter numbers. 
    numbers = input('Enter a numbers: ')

#If statements that have certain letters assigned to execute certain tasks in the calculator. Ex. pressing 'a' adds the numbers in the list.
    if numbers == 'a':
        ans = sum(numbers_list)
        print(ans)
        numbers_list = []
    
    elif numbers == 's':
        ans = numbers_list[0] - sum(numbers_list[1:])
        print(ans)
        numbers_list = []

    elif numbers == 'm':
        ans = math.prod(numbers_list)
        print(ans)
        numbers_list = []

    elif numbers == 'v':
        ans = variance(numbers_list)
        print(ans)
        numbers_list = []

    elif numbers == 'mn':
        ans = mean(numbers_list)
        print(ans)
        numbers_list = []

    elif numbers == 'med':
        ans = median(numbers_list)
        print(ans)
        numbers_list = []
    
    elif numbers == 'medl':
        ans = median_low(numbers_list)
        print(ans)
        numbers_list = []

    elif numbers == 'medh':
        ans = median_high(numbers_list)
        print(ans)
        numbers_list = []

    elif numbers == 'mode':
        ans = mode(numbers_list)
        print(ans)
        numbers_list = []

    elif numbers == 'gm':
        ans = geometric_mean(numbers_list)
        print(ans)
        numbers_list = []

    elif numbers == 'hm':
        ans = harmonic_mean(numbers_list)
        print(ans)
        numbers_list = []
    #If pressed then the calculator ends breaking the loop.
    elif numbers == 'quit':
        break
    #If it is a number it is sent to the list.
    else:   
        numbers_list.append(float(numbers))