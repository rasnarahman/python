# Method to validate Integer created by Rasna Rahman
def validateInt(input):
    valid = True
    try:
        int(input)
    except ValueError:
        valid = False
    return valid


# Method to Get price if not combo. Arithmetic and logic operators are used in the function.
def getBasePrice(coffeeCount, donutCount):
    return 1 * coffeeCount + 0.75 * donutCount


# Method to Get combo price. Arithmetic and logic operators are used in the function.
def getComboPrice(coffeeCount, donutCount):
    if donutCount > coffeeCount:
        price = (coffeeCount + donutCount) * 0.75
    else:
        price = (coffeeCount + (donutCount * 0.50))
    return price


# Method to check if the order is combo and logic operators are used in the function.
def isCombo(coffeeCount, donutCount):
    isCombo = False
    if donutCount > 0 and coffeeCount > 0:
        isCombo = True
    return isCombo