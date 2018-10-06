import Util

"""
Author:  Rasna Rahman.
Description:
In this programme the user can get the price of the coffee, donut and the combo price.
price for:
1 Coffee= $1,
1 Donut = $0.75,
and if the customer buy a donut with one coffee then they will get $0.25 as discount.
The Combo price will be $1.50 for each Coffee and Donut.
"""

print('Hello! This program was written by Rasna Rahman.')
print('Enter number of Coffee and donuts. ')

"""prompting the user to enter the number of coffee (Integer).
Validating whether the user input anything but Integer."""
coffeeCount = input('Number of coffee:')
while not Util.validateInt(coffeeCount):
    print("Please enter a valid number.")
    coffeeCount = input('Number of coffee:')

"""prompting the user to enter the number of Donut (Integer).
Validating whether the user input anything but Integer."""
donutCount = input('Number of donut:')
while not Util.validateInt(donutCount):
    print("Please enter a valid number.")
    coffeeCount = input('Number of donut:')

coffeeCount = int(coffeeCount)
donutCount = int(donutCount)
# checking the condition for getting the total price.
if Util.isCombo(coffeeCount, donutCount):
    print("It is a combo. Customer will get a discounted price.")
    price = Util.getComboPrice(coffeeCount, donutCount)
else:
    price = Util.getBasePrice(coffeeCount, donutCount)
#parsing the total price into string.
print("Total price: " + str(price))
