#List contaning the food/groceries that we intend to buy
groceries = ["banana","orange","apple"]

#dictionary containing the stock of the foods
stock = {
    "banana": 0,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

#dictionary containing the prices of the food
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

#Initial Unmodified function that adds the total of groceries price
def compute_bill_early_version(food = groceries):
    total = 0
    for i in food:
        total += prices.get(i)
    return total

#The modified function that is able to compare wether the food is available or not and then updating the initial dictionary 
def compute_bill(food = groceries):
    '''This function will take an array as the parameter. It will then compare if the food(s)
    inside the array is available/in stock.
    If it is in stock it will then add the price to the total variable and then updating the stock dictionary by reducing the item stock by 1.
    If the item is not available, it will print a message stating which food is not available.'''
    total = 0
    unavailableFood = []
    for i in food:
        if stock.get(i) > 0:
            total += prices.get(i)
            stock[i] = stock.get(i) - 1
        else:
            unavailableFood.append(i)
    string = ", ".join(map(str, unavailableFood))
    print("There aren't any", string, "in this market. Please go to your nearest Giant Supermarket thx.")
    return total

#calls the function and prints a message that contains the total value of the grocery list and also tells the user wether if an item is available or not
print("Your total price is " + str(compute_bill()))