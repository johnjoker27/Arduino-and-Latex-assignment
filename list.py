#python list
bikes=["trek","cannodale","redline","specialized"]
print(bikes)
#acessing individual items
print(bikes[0].title())#indexing
print(bikes[1].upper())
print(bikes[-1].lower())#neg indexing
message = f"My first bicycle was a {bikes[-2].title()}"
print(message)
#ex 3-1
names=['divine','vic','daadi','chris','kyei','spydee','kelvin']
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())
greeting=f"Ahoy there {names[4].title()}"
print(greeting)
#modifying strings
names[4]="sherrif"
print(names[4].lower())
#adding data to strings
names.append("salman")
print(names)
user=input("enter your friends name here:")
names.append(user)
print(names)
#self test
items=[]
item1=input('item here;')
item3=input('item here;')
item2=input('item here;')
items.extend(item2)#seperates the item's name into single alphabets
items.append(item1)
items.append(item3)
print(items)
#removing elements
del names[3]
print(names)
#usinf the pop() method-removes last item in the list if you don't use the index
popped_rides=bikes.pop(-1)
print(popped_rides)
#using remove deletes by value
bikes.remove('trek')
#ex-3
guest_list=['Adam','Eve','You']
invite_1=f'{guest_list[0].title() }? Dinner at 9?'
invite_2=f'{guest_list[1].title()}.Dinner at 9:30.'
invite_3=f'{guest_list[2].title()}Join me for Dinner at 9.'
print(invite_1)
print(invite_2)
print(invite_3)
guest_list[2]='Jane'
print(guest_list)
guest_list.insert(1,'Ria')
guest_list.insert(2,'Mia')
guest_list.append('White')
print(guest_list)
uninvite_1= guest_list.pop()
uninvite_2=guest_list.pop()
uninvite_3 =guest_list.pop()
uninvite_4 =guest_list.pop()
print(guest_list)
#list organization
names.sort()
print(names)
guest_list.sort(reverse=True)
print(guest_list)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print('here is the original list')
print(cars)
print('\n here is the sorted list')
print(sorted(cars))#sorts but temp
print(cars)
print(cars.reverse())#reverse() flips the list on its head
print(len(cars))#len() is used to determine the number of items in the list
print(len(guest_list))
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[0:2:3])
print('here are the first 3 players in my team:')
for player in players[:3]:
    print(player.title())
    #coyping lists
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print('My favourite foods are:')
print(my_foods)

print("\nMy friend's fav foods are:")
print(friend_foods)
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\n my fav foods are:")
print(my_foods)
print("\nmy friends like:")
print(friend_foods)

#ex-4-10
my_foods = ['pizza', 'falafel', 'carrot cake','cannoli','ice cream','waakye']
print("my first 3 favourite foods are:")
print(my_foods[0:3])
print("\n Threes items from the middle of the list are:")
print(my_foods[2:5])
print("\nThe last three items are :")
print(my_foods[-1:-4])
#ex-4-11
friend_pizzas=['pepperoni','cheese','allseasoned','spice']
my_drinks=friend_pizzas[:]
friend_pizzas.append('superspice')
my_drinks.append('apple')
print( f"funny enough my friends like {friend_foods}")
print(f"I like to drink {my_drinks}")

