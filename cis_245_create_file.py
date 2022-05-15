# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 14:33:25 2022

@author: llmechling
"""

import os
    
def create_filepath():
    active = True
    while active:
        filePath = str(input('Please enter the path for your file: '))
        if os.path.exists(filePath):
            print('Thank you, you can write a file to that path.')
            os.chdir(filePath)
            return filePath
            active = False
        else:
            print('This file path does not exist. Please enter a valid file path')                       
            
 
print('Welcome. Please enter the user information into a new file.')
print('You can enter as many users as you want.')

create_filepath()

active = True
while active:
    fileName = str(input('Please enter an alphanumeric file name: '))
    if fileName.isalnum() == True:
        print(f'Your file will be titled {fileName}.')
        active = False
    else:
        print("Please enter a valid alphanumeric filename.")

active = True
while active:
    x = input("Please enter 'user' to add a new user or 'quit' to close the file: ")
    
    if x == 'quit':
        print('You have entered all of your users.')
        break
    
    elif x == 'user':
        userID = input('Please enter the user ID: ')
        name = input('Please type your name: ')
        streetAddress = input('Please enter your street address: ')
        cityStateZip = input('Please enter your city, state, and zip code: ')
        phoneNumber = input('Please enter your phone number: ')
        
        with open(fileName, 'w') as f:
            f.write(userID + "\n")
            f.write("\t" + name + "\n")
            f.write("\t" + streetAddress + "\n")
            f.write("\t" + cityStateZip + "\n")
            f.write("\t" + phoneNumber + "\n")
            
        with open(fileName) as f:
            contents = f.read()
        
    else:
        print("Please enter 'user' or 'quit.'")
        
print('Please review your entries: ')
print(contents)