#Importing a library that has the function to generate a number for the stock information
import random

#Initial prices dictionary that only contain the price information
prices = {    
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3,
}

#prices dictionary that contains an unspecified stock information using randint
prices = {    
    "banana": (4, random.randint(0,10)),
    "apple": (2, random.randint(0,10)),
    "orange": (1.5, random.randint(0,10)),
    "pear": (3, random.randint(0,10))
}

#a loop that is going to print fruit name, price information and stock information
for i in prices:
    temp = prices.get(i)
    print(i + "\nPrice: " + str(temp[0]) + "\nStock: " + str(temp[1]) + "\n")

#Creating a variable to store the total price of sold goods from the prices dictionary
total = 0

#a loop that is going to print the individual total price for each fruit and also going to sum
#all of those individual value and store it to the total variable
for i in prices:
    temp = prices.get(i)
    price = (temp[0] * temp[1])
    print("Price of", i + "=", price)
    total += price

#Prints the total variable
print("\n" + str(total))