#Initial dictionary
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

#Method to add pocket as the key and an empty string as the value of the key to the inventory dictionary.
inventory.update({'pocket' : ''})

#Updates the value of the pocket key inside the inventory dictionary
inventory['pocket'] = ['seashell', 'strange berry', 'lint']

#Updates the values stored in the backpack key to be the sorted values of the backpack key
inventory['backpack'] = sorted(inventory.get('backpack'))

#Defining a function to remove a value of a key from a dictionary
def removeValue(dict, key, val):
    '''This function is going to take three parameters :
    (Dictionary name, the key containing the element, and the element that we want to remove)
    Its going to assign all of the elements inside the key to variable called temp.
    Then its going to remove the value that we specify.
    Then its going to assign the temp values to the dictionary key.'''
    temp = dict.get(key)
    temp.remove(val)
    dict[key] = temp

#Calls the function that removes the value of dagger inside the key backpack from the inventory dictionary
removeValue(inventory, 'backpack', 'dagger')

#adds 50 the value of the gold inside the dictionary.
inventory['gold'] = (inventory.get('gold') + 50)

#prints the final dictionary.
print(inventory)