import matplotlib.pyplot as plt
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
from sys import exit

global status
status = True

def getroutenumber():
    routenumber = input("Enter the next route instructions file, or enter STOP to finish: ")
    return routenumber


def main():
    global status
    status = True

    #Points List is initialised this will hold the x and y axis example: (9,10)
    points = []

    # Gets user input for filename
    number = getroutenumber()

    if number == "STOP":
        status = False
        return

    if number == "001":
        pass
    elif number == "002":
        pass
    elif number == "003":
        pass
    else:
        print("Wrong route file number, please input as 3 numerical numbers #000 ")
        main()
        return


    with open("Route"+str(number)+".txt", "r") as f: 
        coor = f.read().splitlines() 



    #Defines starting x and y coordinates
    initial_value_x = (coor[0]) # X Axis
    initial_value_y = (coor[1]) # Y Axis
    del coor[0:2] # Deletes staring axis

    points = [(int(initial_value_x),int(initial_value_y))]

    # Works out how many values are in the Route file
    counter = 0
    for i in coor:
        counter = counter + 1

    # Initial Values to compare with
    value1 = (initial_value_x) # X Axis
    value2 = (initial_value_y) # Y Axis
    a = 0
    for i in coor:
        # Setting key variables for what direction to move if South is initiated
        if i == "S":
            value1 = int(value1) - 0
            value2 = int(value2) - 1
            points.append((value1,value2))
            if value1 < 0 or value1 > 12 or value2 < 0 or value2 > 12: # Checking for coordinates outside the 12x12 grid
                print ('Error: The route is outside of the grid (Error Code:MS)')
                return
            a = a + 1

        # Setting key variables for what direction to move if South is initiated
        elif i == "N":
            value1 = int(value1) - 0
            value2 = int(value2) + 1
            points.append((value1,value2))
            if value1 < 0 or value1 > 12 or value2 < 0 or value2 > 12: # Checking for coordinates outside the 12x12 grid
                print ('Error: The route is outside of the grid (Error Code:MN)')
                return
            a = a + 1

        # Setting key variables for what direction to move if South is initiated
        elif i == "E":
            value1 = int(value1) + 1
            value2 = int(value2) - 0
            points.append((value1,value2))
            if value1 < 0 or value1 > 12 or value2 < 0 or value2 > 12: # Checking for coordinates outside the 12x12 grid
                print ('Error: The route is outside of the grid (Error Code:ME)')
                return
            a = a + 1
        
        # Setting key variables for what direction to move if South is initiated
        elif i == "W":
            value1 = int(value1) - 1
            value2 = int(value2) - 0
            points.append((value1,value2))
            if value1 < 0 or value1 > 12 or value2 < 0 or value2 > 12:# Checking for coordinates outside the 12x12 grid
                print ('Error: The route is outside of the grid (Error Code:MW)')
                return
            a = a + 1
        else:
            return
        
    makeplot(points=points)

def makeplot(points):
    plt.rcParams['toolbar'] = 'None'
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    # Set axis ranges; by default this will put major ticks every 25.
    ax.set_xlim(0, 12 )
    ax.set_ylim(0, 12)

    # Change major ticks to show every 20.
    ax.xaxis.set_major_locator(MultipleLocator(2))
    ax.yaxis.set_major_locator(MultipleLocator(2))

    # Change minor ticks to show every 5. (20/4 = 5)
    ax.xaxis.set_minor_locator(AutoMinorLocator(1))
    ax.yaxis.set_minor_locator(AutoMinorLocator(1))

    # Turn grid on for both major and minor ticks and style minor slightly
    # differently.
    ax.grid(which='major', color='#CCCCCC', linestyle='--')
    ax.grid(which='minor', color='#CCCCCC', linestyle=':')

    # Makes and plots values onto a graph
    x = list(map(lambda x: x[0], points))
    y = list(map(lambda x: x[1], points))
    plt.plot(x, y)
    plt.grid(True)
    plt.show()

while status == True:
    main()