# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 19:39:23 2022

@author: llmechling
"""

#opening message to users
welcome = "Welcome to the investment calculator.\n"
welcome += "\nHere we will tell you how long it takes for your investment to double.\n"
welcome += "\nEnter the rate of return on your investment, or interest rate,\n"
welcome += "and using the rule of 72 you will learn the number of years it \n"
welcome += "it will take to double your investment!\n"
welcome += "\n(Enter '0' to end the program).\n"

#while loop using flag to end program
active = True
while active:
    rate = input(welcome)
    rate = float(rate)
    
    if rate == 0:
        active = False
        
    else:
        #return output as years and months
        #https://stackoverflow.com/questions/43351185/python-converting-decimals-into-months
        def singular_or_plural(count, word):
            if count == 1:
                return "1 %s" % word
            elif count > 1:
                return "%d %ss" % (count, word)
        
        def years_and_months(float_year):
            year = int(float_year)
            month = int((float_year % 1) * 12)
            words = [(year, 'year'), (month, 'month')]
            return ' and '.join(singular_or_plural(count, word) 
                                for (count, word) in words if count > 0)
        
        #rule of 72 to calculate years to double investment
        years = 72 / rate
        years = round(years, 2)
        
        #printed output of program
        print("\nTo double your investment it will take approximately:\n")
        print(years_and_months(years))
        
#I wanted to put in a try loop to check for correct input, like there 
#was no % sign included in the user input, but I couldnt figure out how to 
#make it work with the other while loop. Is this something you could help
#with in an office hour time?

#Is it OK to use an online resource to find code to help with part of 
#projects as long as we cite the code? Here i included the URL of the code
#I used to help with the months and years output.