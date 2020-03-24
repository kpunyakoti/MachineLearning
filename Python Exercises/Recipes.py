#Blank#

def ColdCoffee():
     print('===============''\n''Cold Coffee Recipe:''\n''\n''List of Ingredients:''\n''Milk - 1/3rd cup or 100ml''\n'
           'Coffee mix - 2teaspoons''\n''Vanilla - 2scoops''\n''Sugar - 1 teaspoon''\n''Ice - 2cubes''\n'
              'Chocolate syrup - for garnish''\n''Cocoa powder - for garnish''\n')
     print('Preparation Method:''\n'
              'Pour Milk  |  add Coffee mix  |  add Sugar''\n'
              'Blend''\n'
              'add Ice  |  add Vanilla''\n'
              'Blend''\n'
            'Prepare glass:''\n'
              'Garnish with chocolate syrup  |  Pour the mix |  Add froth with Spoon  |  Sprinkle Cocoa powder on top''\n'
            'Serve the Drink''\n')
     return  print('Enjoy your Cold Coffee')
def BanCar():
    print('===============''\n''Banana Caramel Recipe:''\n''\n''List of Ingredients:''\n''Milk - 1/3rd cup''\n'
              'Frozen ripe Banana - 1''\n''Vanilla - 2scoops''\n'
              'Caramel sauce - ???''\n''Caramel syrup - for garnish''\n')
    print('Preparation Method:''\n'
              'Pour Milk  |  add cut Banana |  add caramel sauce''\n'
              'Blend''\n'
              'add Vanilla scoops''\n'
              'Blend''\n'
            'Prepare glass:''\n'
              'Garnish with caramel syrup  |  Pour the mix  |  add caramel sauce on top''\n'
            'Serve the Drink''\n')
    return  print('Enjoy your Banana Caramel Shake')
def Mchip():
    print('===============''\n''Mint Chocochips Recipe:''\n''\n''List of Ingredients:''\n''Milk - 1/3rd cup''\n'
              'Mint Leaves - 5''\n''Vanilla - 2scoops''\n''Green color - 2 drops''\n''Ice - 2cubes''\n'
              'Chocochips - 1/8th cup ''\n''Chocolate syrup - for garnish''\n')
    print('Preparation Method:''\n'
              'Pour Milk  |  add 3 mint leaves |  add Vanilla scoops   |   add color''\n'
              'Blend''\n'
              'add Chocochips   | add Ice''\n'
              'Blend''\n'
            'Prepare glass:''\n'
              'Pour the mix  |  add chocolate syrup on top''\n'
            'Serve the Drink''\n')
    return  print('Enjoy your Mint Chocochips Shake')
def Orshake():
    print('===============''\n''Oreo Shake Recipe:''\n''\n''List of Ingredients:''\n''Milk - 1/3rd cup''\n'
              'Oreo Biscuits - 4''\n''Vanilla - 2scoops''\n''Chocolate syrup - 5 drops''\n''Ice - 2cubes''\n'
              'Chocolate syrup - for garnish''\n')
    print('Preparation Method:''\n'
              'Pour Milk  |  add 3 Oreo Biscuits |  add Vanilla scoops  |   add chocolate sauce  | add Ice''\n'
              'Blend''\n'
            'Prepare glass:''\n'
              'Pour the mix  |  add oreo Biscuit on top''\n'
            'Serve the Drink''\n')
    return  print('Enjoy your Oreo Shake')
def Brbn():
    print('===============''\n''Bourbon Shake Recipe:''\n''\n''List of Ingredients:''\n''Milk - 1/3rd cup''\n'
              'Bourbon Biscuits - 4''\n''Vanilla - 2scoops''\n''Chocolate syrup - 5 drops''\n''Ice - 2cubes''\n'
              'Chocolate syrup - for garnish''\n')
    print('Preparation Method:''\n'
              'Pour Milk  |  add 3 Bourbon Biscuits |  add Vanilla scoops  |   add chocolate sauce  | add Ice''\n'
              'Blend''\n'
            'Prepare glass:''\n'
              'Pour the mix  |  add Bourbon Biscuit on top''\n'
            'Serve the Drink''\n')
    return  print('Enjoy your Bourbon Shake')
def IcecreamShake():
    print('===============''\n''Ice Cream Shake Recipe:''\n''\n''List of Ingredients:''\n''Milk - 1/3rd cup''\n'
              'Ice Cream - 2scoops''\n''Ice - 2cubes''\n'
              'Jam/Chocolate Sauce/Strawberry syrup/Caramel Sauce - for garnish''\n')
    print('Preparation Method:''\n'
              'Pour Milk |  add Icecream scoops | add Ice''\n'
              'Blend''\n'
            'Prepare glass:''\n'
              'Pour the mix  |  add sauce on top''\n'
            'Serve the Drink''\n')
    return  print('Enjoy your Ice Cream Shake')
def Ultchoc():
    print('===============''\n''Ultimate Chocolate Shake Recipe:''\n''\n''List of Ingredients:''\n''Milk - 1/3rd cup''\n'
              'Chocolate Ice Cream - 2scoops''\n''Ice - 2cubes''\n''Munch/Kitkat - 1''\n'
              'Chocolate Sauce Sauce - 30ml plus for garnish''\n')
    print('Preparation Method:''\n'
              'Pour Milk |  add Chocolate scoops | add Ice''\n'
              'Blend''\n'
            'Prepare glass:''\n'
              'Pour the mix  |  add chocolate sauce on top  |   add wmuch/kitkat on the side''\n'
            'Serve the Drink''\n')
    return  print('Enjoy your Chocolate Shake')
def Shakes():
    a = str(input('Enter your Milkshake Selction from below:''\n''Cold Coffee''\n''Banana Caramel''\n''Mint Chocochip''\n'
            'Ice Cream Shake''\n''Ultimate chocholate shake''\n''Oreo Shake''\n''Bourbon Shake:''\n'))
    if (a=='Cold Coffee'):
        ColdCoffee()
    elif(a=='Banana Caramel'):
        BanCar()
    elif(a=='Mint Chocochip'):
        Mchip()
    elif(a=='Oreo Shake'):
        Orshake()
    elif(a=='Bourbon Shake'):
        Brbn()
    elif(a=='Ice Cream Shake'):
        IcecreamShake()
    elif(a=='Ultimate Chocolate Shake'):
        Ultchoc()
    else:
        print('fuckoff')
        
