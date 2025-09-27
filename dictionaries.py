#accesssing values in dict
alien_0={'color':'green'}
print(alien_0)

alien_0 = {'color': 'green', 'points': 5}
new_points=alien_0['points']
print(f'you have {new_points} points')

alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)

#starting dictionaries with an empty dict
info={}
info['size']=int(input('how big are ya in numbers?'))
info['height']=int(input('how tall are you?'))
print(info)


alien_0={'x_position':0,'y_position':25,'speed':'medium'}
print(f"original position:{alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    c_increment = 3