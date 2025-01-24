# Tea

tea_varieties = ['green', 'black', 'oolong', 'white', 'herbal']
# complete list
print(tea_varieties)

# Last variety
print(tea_varieties[-1])

# slice tea_varieties from 1 to 2
print(tea_varieties[1:3])

# slice starts from 0 index to 2  
print(tea_varieties[:3])

# change 4th tea variety to herbal
tea_varieties[3] = 'yellow'


print(tea_varieties)
# ['green', 'black', 'oolong', 'yellow', 'herbal']