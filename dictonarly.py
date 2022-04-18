fruits_colors={'apple': 'red','lemon': 'yellow','geapes': 'purple'}
print(fruits_colors['apple'])
fruits_colors['peach'] = 'pink'
print(fruits_colors)

#.keys()　values()
for fruit in fruits_colors.values():
#for fruit in fruits_colors.keys():
    print(fruit)

#.items()
for fruit, color in fruits_colors.items():
    print(f"{fruit} is {color}")