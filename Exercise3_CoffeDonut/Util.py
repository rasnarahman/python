# Method to valudate Integer
def validateInt(input):
    valid = True
    try:
        int(input)
    except ValueError:
        valid = False
    return valid


# Get price if not combo
def getBasePrice(coffeeCount, donutCount):
    return 1 * coffeeCount + 0.75 * donutCount


# Get combo price
def getComboPrice(coffeeCount, donutCount):
    if donutCount > coffeeCount:
        price = (coffeeCount + donutCount) * 0.75
    else:
        price = (coffeeCount + (donutCount * 0.50))
    return price


# Check if the order is combo
def isCombo(coffeeCount, donutCount):
    isCombo = False
    if donutCount > 0 and coffeeCount > 0:
        isCombo = True
    return isCombo