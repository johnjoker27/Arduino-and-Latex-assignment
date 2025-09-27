magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title())
    print(f'{magician} you are to perform a magic trick.') 
    print(f'{magician} that was good.')


       
for value in range(1,8):
    print(value)

#loops into variables
numbers=list(range(1,6))
print(numbers)
multiple_numbers=list(range(3,15,4)) 
print(multiple_numbers)

#making a loop that produces sqaure numbers
squares=[]
for value in range(1,21):
    square=value**2
    squares.append(square)

print(squares) 

#stats functions
a=min(squares)
b=max(squares)
c=sum(squares)
d=len(squares)
print(a)
print(b)
print(c)
print(d)

#animal list
animal_list=['Horse','Rabbit','Cat']
for animal in animal_list:
    print(animal.upper())
#ex-4
numbers=list(range(1,21))
for number in numbers:
    print(number)

'''count=list(range(1,1_000_001))
for counts in count:
    print(counts)

q=min(count)
w=max(count)
e=sum(count)
print(e)
print(q)
print(w)'''
#printing odd numbers
for odd_number in range(1,20,2):
    print(odd_number)

#multiples of 3
multiples_of_3=[]
for value in range(3,31):
    multiples_of_3=value**value
    print(value)
    print(multiples_of_3)

store=list(range(1,41))
for items in store:
    print(items)
print(store)
