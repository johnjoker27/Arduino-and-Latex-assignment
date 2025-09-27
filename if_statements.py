cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car=='bmw':
       print(car.upper())
    else:
        print(car.title()) 

requested_toppings='mushrooms'


if requested_toppings!='anchioves':
    print('Hold the anchioves!')


#checking whether  a value is available or not
requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms'in requested_toppings:
    print('Helll Yeaaahh')
else:
    print('Aww damn')

#banned-users
banned_users=['john','giveon','justin','peaches','marie']
user='marie'
if user not in banned_users:
    print(f'{user}you may post whatever you wish')
else:
    print(f'Hello {user}.You have been banned from commenting on any posts on this platform.')



#TRY-5-1
car = 'subaru'
guess_1=input('Guess what car?')

if guess_1.lower()==car:
    print('true')
else:
    print('false')



car_2='audi'
guess_2=input("Think it is a bmw?Guess...:")
print("\nIs car == 'audi'? I predict False.")
if guess_2==car_2:
    print('Arrrgh, You lucky bugger!')
else:
    print('Haha, You loose!')


items=['Money','Brush','Jute Bag','Clothes','Passports'] 
forgotten_item=input('Enter the name of the of the item you may or may not have forgotten:')
if forgotten_item.title() in items:
    print('Nope.Already packed and loaded for travel')
else:
    print(f'You should probably go get some{forgotten_item} before you forget it again.')

age=int(input("How old are you sir?"))

if age < 4:
    print("Your admission costs are 0")
elif age < 18:
    print("Your admission costs are 25")
else:
    print("your admission costs are 40.")

age=int(input('AGe?'))

if age <4:
    price=0
elif age <18:
    price=25
elif age>18:
    price=30    
elif age>=60:
    price=10
print(f"Your bill will be {price} dollars. ")


wanted_additions=['cheese','pepperoni']
if 'cheese' in wanted_additions:
    print('Adding cheese')
if 'pepperoni' in wanted_additions:
    print('Adding pepperoni')
if 'mint' in wanted_additions:
  print("Mint being added.")

alien_colour=['red','blue','green']
for alien in alien_colour:
 if alien=='red':
    print("you have earned 5 points")
 else:
    print("you have earned 8 points")        


#greetings using for loops and if statements together
user=['admin','jenkins','rihamma','grit']
for users in user:
    if users=='admin':
        print(f"Hello {users.title()}!Would you like to see the performance reports?")
    else:
        print(f"Hello {users.title()}! Thank you for logging in again.")


#comparing usernames
current_users=['john','petra','kofi','james','fuhad']
new_users=['frenkie','pedri','john','kofi','bum']
for user in new_users:
    if user.lower() in current_users:
        print('Sorry but this username has been taken,please enter another one.')
    else:
        print(f'Feel free to use this username.\nWelcome {user}!')


#ordinal number with suffixes
numbers=[1,2,3,4,5,6,7,8,9]
for number in numbers:
    if number == 1:
         print(f'{number}st')
    elif number == 2:
        print(f'{number}nd')
    elif number == 3:    
        print(f'{number}rd')
    else:
        print(f'{number}th')
             