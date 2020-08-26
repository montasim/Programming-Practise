Grocery = ["Harpic", "Vim Bar", "Soap", "Powder",
           "Tooth Pest", "Water Bottle", "100", "200", "Cloth", "1", "300", "10", "4", "2", "340", "999"]

for number in Grocery:
    listElements = str(number)
    if listElements.isnumeric():
        if int(listElements) > 6:
            print(listElements)
