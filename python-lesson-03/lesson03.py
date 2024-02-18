#Assignment 3
#Initialise three variables: money_start, saving_years, interest_rate
#Assign the values to the three variables using the input() function. Pass an instructional message (string) as an argument to the input function.
#Convert each input to a float or integer, depending on the type of input you are requesting.
#Create a variable money_result
#Assign the formula money_start * interest_rate * saving_years to money_result
#Print money_result to the console in a formatted string.
#Is the result more than 10000? If yes, include in your code to print True to the console, otherwise print False.

money_start = input('Enter inital savings: $')
saving_years = input('Enter whole years of savings: ')
interest_rate = input('Enter interest rate %: ')
money_result = float(money_start)*(float(interest_rate)/100)*int(saving_years)
print (f"Savings simple interest: ${money_result}")
print (f"Savings simple interest greater than 10000: {money_result > 10000}")
principle_interest = float(money_start)+float(money_result)
print (f"Principle and Interest is: ${principle_interest}")
print (f"Principle and interest greater than 10000: {principle_interest > 10000}")