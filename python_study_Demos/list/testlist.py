'''
Description: 
Version: 2.0
Author: xuchaoxin
Date: 2021-04-08 22:55:30
LastEditors: xuchaoxin
LastEditTime: 2021-04-13 09:29:16
'''

# test git


numbers = [30, 42, 28, 50, 15]  
for i, num in enumerate(numbers):  
    if num % 3 == 0 and num % 5 == 0:  
        numbers[i] = 'fizzbuzz'  
    elif num % 3 == 0:  
        numbers[i] = 'fizz'  
    elif num % 5 == 0:  
        numbers[i] = 'buzz'  
print(numbers) # ['fizzbuzz', 'fizz', 28, 'buzz', 'fizzbuzz'] 
    
    

countries = ['France', 'Germany', 'Canada']  
capitals = ['Paris', 'Berlin', 'Ottawa']  
for country, capital in zip(countries,capitals): 
    print(country, capital) # France Paris  
