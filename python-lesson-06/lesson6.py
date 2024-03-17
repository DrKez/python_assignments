 #Lesson 6 Dictionary of Ethan (and his family)
from datetime import date
DOB = date(2023, 11, 29)
print(f'Ethan DOB: {DOB}')

ethan = {
    'name':'Ethan',
    'age': '1 day', 
    'hobby': 'crying', 
    'diet': 'Colostrum'}
for x, y in ethan.items():
  print("\033[1;32m"+ f'  My {x} is {y}.'+"\033[0m")

#Update dictionary 
today = date.today()
time_difference = today - DOB
D = time_difference.days
W = int(D/7)
print("Today's date:", today)
print(f'Ethan at {W} weeks:')  
ethan_new = {'age':"3.5 months",'hobby':"smiling", 'diet':'milk'}
ethan.update(ethan_new)
for x, y in ethan.items():
  print("\033[1;33m"+ f'  My {x} is {y}.'+"\033[0m")

#delete data
ethan.pop('diet')

#add and update
relationship =input('Please enter your relationship to Ethan (e.g. Mum, Dad, Aunty, Friend): ')
ethan['name']=input('Please enter your name: ')
ethan['age']=input('Please enter your age: ')
ethan['occupation']=input('Please enter your occupation: ')
ethan['hobby']=input('Please enter your hobby: ')
for x, y in ethan.items():
  print ("\033[1;35m"+ f"  {relationship}'s {x} is {y}."+"\033[0m")

ethan.clear()
print (f'Dictionary is cleared for security reasons. Dictionary now contains: {ethan}')