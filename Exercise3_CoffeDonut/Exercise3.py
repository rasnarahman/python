import Util

print('Hello! This program was written by Rasna Rahman.')
print('Enter number of Coffee and donuts. ')


coffeeCount = input('Number of coffee:')
while Util.validateInt(coffeeCount) == False:
    print("Please enter a valid number.")
    coffeeCount = input('Number of coffee:')


donutCount = input('Number of donut:')
while Util.validateInt(donutCount) == False:
    print("Please enter a valid number.")
    coffeeCount = input('Number of donut:')

coffeeCount = int(coffeeCount)
donutCount = int(donutCount)

if(Util.isCombo(coffeeCount, donutCount)):
    print("It is a combo. Customer will get a discounted price.")
    price = Util.getComboPrice(coffeeCount, donutCount)
else:
    price = Util.getBasePrice(coffeeCount, donutCount)


print("Total price: " + str(price))
