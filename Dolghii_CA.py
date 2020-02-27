#Alexander Dolghii, Mohammed Jan
#5/05/2019
#Dolghii_Jan_CA.py
#Program simulates a game of battleship

Flag = True          #Used to start the menu overlay loop
import random   #Imports random library so program can generate random coordinates on grid


####FUNCTIONS####


def printgrid():   #Creates function to output visual grid to user during each turn, outputting each item in list in each box
    print(topbar)
    print(row0letters)
    print('|___|____|____|____|____|____|____|____|____|____|____|')
    print('| 1 | ' + (row1[0]) + '  | ' + (row1[1]) + '  | ' + (row1[2]) + '  | ' + (row1[3]) + '  | ' + (row1[4]) + '  | ' + (row1[5]) + '  | ' + (row1[6]) + '  | ' + (row1[7]) + '  | ' + (row1[8]) + '  | ' + (row1[9]) + '  |')
    print('|___|____|____|____|____|____|____|____|____|____|____|')
    print('| 2 | ' + (row2[0]) + '  | ' + (row2[1]) + '  | ' + (row2[2]) + '  | ' + (row2[3]) + '  | ' + (row2[4]) + '  | ' + (row2[5]) + '  | ' + (row2[6]) + '  | ' + (row2[7]) + '  | ' + (row2[8]) + '  | ' + (row2[9]) + '  |')
    print('|___|____|____|____|____|____|____|____|____|____|____|')
    print('| 3 | ' + (row3[0]) + '  | ' + (row3[1]) + '  | ' + (row3[2]) + '  | ' + (row3[3]) + '  | ' + (row3[4]) + '  | ' + (row3[5]) + '  | ' + (row3[6]) + '  | ' + (row3[7]) + '  | ' + (row3[8]) + '  | ' + (row3[9]) + '  |')
    print('|___|____|____|____|____|____|____|____|____|____|____|')
    print('| 4 | ' + (row4[0]) + '  | ' + (row4[1]) + '  | ' + (row4[2]) + '  | ' + (row4[3]) + '  | ' + (row4[4]) + '  | ' + (row4[5]) + '  | ' + (row4[6]) + '  | ' + (row4[7]) + '  | ' + (row4[8]) + '  | ' + (row4[9]) + '  |')
    print('|___|____|____|____|____|____|____|____|____|____|____|')
    print('| 5 | ' + (row5[0]) + '  | ' + (row5[1]) + '  | ' + (row5[2]) + '  | ' + (row5[3]) + '  | ' + (row5[4]) + '  | ' + (row5[5]) + '  | ' + (row5[6]) + '  | ' + (row5[7]) + '  | ' + (row5[8]) + '  | ' + (row5[9]) + '  |')
    print('|___|____|____|____|____|____|____|____|____|____|____|')
    print('| 6 | ' + (row6[0]) + '  | ' + (row6[1]) + '  | ' + (row6[2]) + '  | ' + (row6[3]) + '  | ' + (row6[4]) + '  | ' + (row6[5]) + '  | ' + (row6[6]) + '  | ' + (row6[7]) + '  | ' + (row6[8]) + '  | ' + (row6[9]) + '  |')
    print('|___|____|____|____|____|____|____|____|____|____|____|')
    print('| 7 | ' + (row7[0]) + '  | ' + (row7[1]) + '  | ' + (row7[2]) + '  | ' + (row7[3]) + '  | ' + (row7[4]) + '  | ' + (row7[5]) + '  | ' + (row7[6]) + '  | ' + (row7[7]) + '  | ' + (row7[8]) + '  | ' + (row7[9]) + '  |')
    print('|___|____|____|____|____|____|____|____|____|____|____|')
    print('| 8 | ' + (row8[0]) + '  | ' + (row8[1]) + '  | ' + (row8[2]) + '  | ' + (row8[3]) + '  | ' + (row8[4]) + '  | ' + (row8[5]) + '  | ' + (row8[6]) + '  | ' + (row8[7]) + '  | ' + (row8[8]) + '  | ' + (row8[9]) + '  |')
    print('|___|____|____|____|____|____|____|____|____|____|____|')
    print('| 9 | ' + (row9[0]) + '  | ' + (row9[1]) + '  | ' + (row9[2]) + '  | ' + (row9[3]) + '  | ' + (row9[4]) + '  | ' + (row9[5]) + '  | ' + (row9[6]) + '  | ' + (row9[7]) + '  | ' + (row9[8]) + '  | ' + (row9[9]) + '  |')
    print('|___|____|____|____|____|____|____|____|____|____|____|')
    print('|10 | ' + (row10[0]) + '  | ' + (row10[1]) + '  | ' + (row10[2]) + '  | ' + (row10[3]) + '  | ' + (row10[4]) + '  | ' + (row10[5]) + '  | ' + (row10[6]) + '  | ' + (row10[7]) + '  | ' + (row10[8]) + '  | ' + (row10[9]) + '  |')
    print('|___|____|____|____|____|____|____|____|____|____|____|')

def printCpuGrid():   #Creates function to output program's grid with ship placements hidden behind another grid
    print(topbar)
    print(row0letters)
    print('|___|____|____|____|____|____|____|____|____|____|____|')
    print('| 1 | ' + (visual_row1[0]) + '  | ' + (visual_row1[1]) + '  | ' + (visual_row1[2]) + '  | ' + (visual_row1[3]) + '  | ' + (visual_row1[4]) + '  | ' + (visual_row1[5]) + '  | ' + (visual_row1[6]) + '  | ' + (visual_row1[7]) + '  | ' + (visual_row1[8]) + '  | ' + (visual_row1[9]) + '  |')
    print('|___|____|____|____|____|____|____|____|____|____|____|')
    print('| 2 | ' + (visual_row2[0]) + '  | ' + (visual_row2[1]) + '  | ' + (visual_row2[2]) + '  | ' + (visual_row2[3]) + '  | ' + (visual_row2[4]) + '  | ' + (visual_row2[5]) + '  | ' + (visual_row2[6]) + '  | ' + (visual_row2[7]) + '  | ' + (visual_row2[8]) + '  | ' + (visual_row2[9]) + '  |')
    print('|___|____|____|____|____|____|____|____|____|____|____|')
    print('| 3 | ' + (visual_row3[0]) + '  | ' + (visual_row3[1]) + '  | ' + (visual_row3[2]) + '  | ' + (visual_row3[3]) + '  | ' + (visual_row3[4]) + '  | ' + (visual_row3[5]) + '  | ' + (visual_row3[6]) + '  | ' + (visual_row3[7]) + '  | ' + (visual_row3[8]) + '  | ' + (visual_row3[9]) + '  |')
    print('|___|____|____|____|____|____|____|____|____|____|____|')
    print('| 4 | ' + (visual_row4[0]) + '  | ' + (visual_row4[1]) + '  | ' + (visual_row4[2]) + '  | ' + (visual_row4[3]) + '  | ' + (visual_row4[4]) + '  | ' + (visual_row4[5]) + '  | ' + (visual_row4[6]) + '  | ' + (visual_row4[7]) + '  | ' + (visual_row4[8]) + '  | ' + (visual_row4[9]) + '  |')
    print('|___|____|____|____|____|____|____|____|____|____|____|')
    print('| 5 | ' + (visual_row5[0]) + '  | ' + (visual_row5[1]) + '  | ' + (visual_row5[2]) + '  | ' + (visual_row5[3]) + '  | ' + (visual_row5[4]) + '  | ' + (visual_row5[5]) + '  | ' + (visual_row5[6]) + '  | ' + (visual_row5[7]) + '  | ' + (visual_row5[8]) + '  | ' + (visual_row5[9]) + '  |')
    print('|___|____|____|____|____|____|____|____|____|____|____|')
    print('| 6 | ' + (visual_row6[0]) + '  | ' + (visual_row6[1]) + '  | ' + (visual_row6[2]) + '  | ' + (visual_row6[3]) + '  | ' + (visual_row6[4]) + '  | ' + (visual_row6[5]) + '  | ' + (visual_row6[6]) + '  | ' + (visual_row6[7]) + '  | ' + (visual_row6[8]) + '  | ' + (visual_row6[9]) + '  |')
    print('|___|____|____|____|____|____|____|____|____|____|____|')
    print('| 7 | ' + (visual_row7[0]) + '  | ' + (visual_row7[1]) + '  | ' + (visual_row7[2]) + '  | ' + (visual_row7[3]) + '  | ' + (visual_row7[4]) + '  | ' + (visual_row7[5]) + '  | ' + (visual_row7[6]) + '  | ' + (visual_row7[7]) + '  | ' + (visual_row7[8]) + '  | ' + (visual_row7[9]) + '  |')
    print('|___|____|____|____|____|____|____|____|____|____|____|')
    print('| 8 | ' + (visual_row8[0]) + '  | ' + (visual_row8[1]) + '  | ' + (visual_row8[2]) + '  | ' + (visual_row8[3]) + '  | ' + (visual_row8[4]) + '  | ' + (visual_row8[5]) + '  | ' + (visual_row8[6]) + '  | ' + (visual_row8[7]) + '  | ' + (visual_row8[8]) + '  | ' + (visual_row8[9]) + '  |')
    print('|___|____|____|____|____|____|____|____|____|____|____|')
    print('| 9 | ' + (visual_row9[0]) + '  | ' + (visual_row9[1]) + '  | ' + (visual_row9[2]) + '  | ' + (visual_row9[3]) + '  | ' + (visual_row9[4]) + '  | ' + (visual_row9[5]) + '  | ' + (visual_row9[6]) + '  | ' + (visual_row9[7]) + '  | ' + (visual_row9[8]) + '  | ' + (visual_row9[9]) + '  |')
    print('|___|____|____|____|____|____|____|____|____|____|____|')
    print('|10 | ' + (visual_row10[0]) + '  | ' + (visual_row10[1]) + '  | ' + (visual_row10[2]) + '  | ' + (visual_row10[3]) + '  | ' + (visual_row10[4]) + '  | ' + (visual_row10[5]) + '  | ' + (visual_row10[6]) + '  | ' + (visual_row10[7]) + '  | ' + (visual_row10[8]) + '  | ' + (visual_row10[9]) + '  |')
    print('|___|____|____|____|____|____|____|____|____|____|____|')

def game_win(): # defines a functions called game_win which prints a sequence of ascii characters to spell out the words: you win. Ths will be displayed to the user when they sink all enemy ships
  blanks(5)
  print('██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗')
  print('╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║')
  print(' ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║')
  print('  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║')
  print('   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║')
  print('   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝')
  blanks(5) # calls the blanks function to create blanks spaces in between words. This makes things easier to read
  move_on = input('Enter - continue to main menu')


def userPointSelect():   #Creates function to select a point on the grid and verifies if it is a valid coordinate
    error_checker = True   #Variable set to true to check for errors in input
    while error_checker == True:  #Loop begins to get input and check for errors
        try:
            user_point = input('Enter the coordinate(e.g. "D2"): ')  #Asks user for coordinate value
            user_point = user_point.lower()   #Lowercases input for value check
            test_x = user_point[1:3]  #Slices input for x and y coordinate values
            test_y = user_point[0]
            test_x = int(test_x)

            if test_x < 1 or test_x > 10:   #If user enters a row value not on grid, this will display
                print('You have entered a row not in the grid, please try again.')
            else:
                if test_y == 'a' or test_y == 'b' or test_y == 'c' or test_y == 'd' or test_y == 'e' or test_y == 'f' or test_y == 'g' or test_y == 'h' or test_y == 'i' or test_y == 'j':    #If user enters a correct column value, this will display
                    return user_point  #Returns valid coordinate value
                else:   #If user enters an incorrect letter, this will display
                  print('You have entered a column not in the grid, please try again.')
        except ValueError:    #Allows program to continue if value error occurs
            print('You entered an invalid point. Try again!')
        except IndexError:   #Allows program to continue if index error occurs
            print('You entered an invalid point. Try again!')

def cpuPointSelect():   #Creates function to randomly select a point on the grid and return it
    cpu_x = random.randint(0,9)   #Selects random x value between 0 and 9
    cpu_y = random.randint(0,9)   #Selects random y value between 0 and 9
    cpu_x = str(cpu_x)
    cpu_y = str(cpu_y)
    cpu_point = (cpu_x + cpu_y)   #Combines both values into a str to be added for ship sink verification and ship placement
    return cpu_point  #Returns value to variable

def columnChecker(x_range):   #Creates function to change column letter inputted to a value that can used to select column on the grid
  if x_range == 'a':    #The next lines convert the letters to their corresponding numbers locating each column on the grid
    x_range = 0
  elif x_range == 'b':
    x_range = 1
  elif x_range == 'c':
    x_range = 2
  elif x_range == 'd':
    x_range = 3
  elif x_range == 'e':
    x_range = 4
  elif x_range == 'f':
    x_range = 5
  elif x_range == 'g':
    x_range = 6
  elif x_range == 'h':
    x_range = 7
  elif x_range == 'i':
    x_range = 8
  elif x_range == 'j':
    x_range = 9
  return x_range   #Returns converted value to variable

def shipPlacement(direction,grid,ship_row,ship_length,x_range):  #Creates function to place user's ships on their grid 
    if ((grid[ship_row])[x_range]) == 'S':   #If there is already a ship placed on the point, user will be notified to select a new point
        ship_length = 1   #Sets ship length value to one so it will not affect ship placement loop
        print('')
        print('You cannot place a ship there as it will overlap, please select a new coordinate.')  #Outputs error to user
        return ship_length   #Returns value to variable
    if direction == 'h':  #If user selects to place the ship horizontally, this will display
        if (x_range + ship_length) > 10:   #If user selects a point in which ship will go off the grid, this will display
            print('')
            print('You cannot place a ship there, it does not cover the grid completely.') #Outputs error to user
            user_ok = input('Press any key to continue')  #Asks user to continue when error has been read
            ship_length = 1  #Sets ship length value to one so it will not affect ship placement loop
            return ship_length  #Returns value to variable
        for ship_placement in range(ship_length):   #Loop begins to place ship on grid by replacing blanks in list with 'S'
            if ((grid[ship_row])[x_range]) == 'S':   #If the ship placement overlaps with another ship placed, this will display
                print('')
                print('You cannot place a ship there as it will overlap, please select a new coordinate.')  #Outputs error to user
                for ship_placement in range(ship_length):   #Loop begins to undo ship placement by replacing previous 'S' placements back to ' '
                   x_range = x_range - 1  #Subtracts row by one to go back to undo ship placement
                   ((grid[ship_row])[x_range]) = ' '   #Replaces ship placed ('S') back to a blank space (' ')
                   user_ok = input('Press any key to continue')   #Asks user to continue when error has been read
                   ship_length = 1  #Sets ship length value to one so it will not affect ship placement loop
                   return ship_length
            ((grid[ship_row])[x_range]) = 'S'  #Uses grid list to select row on grid then selects column and changes item in list to represent ship location
            x_range = x_range + 1   #Adds one to column so ship placement can move to next column to place ship
    elif direction == 'v':   #If user selects to place the ship vertically, this will display
        if (ship_row + ship_length) > 10:   #If user selects a point in which ship will go off the grid, this will display
            print('')
            print('You cannot place a ship there, it does not cover the grid completely.')   #Outputs error to user
            user_ok = input('Press any key to continue')
            ship_length = 1   #Sets ship length value to one so it will not affect ship placement loop
            return ship_length
        for ship_placement in range(ship_length):   #Loop begins to put ship on grid
            if ((grid[ship_row])[x_range]) == 'S':     #If the ship placement overlaps with another ship placed, this will display
                print('')
                print('You cannot place a ship there as it will overlap, please select a new coordinate.')   #Outputs error to user
                for ship_placement in range(ship_length):
                   ship_row = ship_row - 1    #Subtracts row by one to go back to undo ship placement
                   ((grid[ship_row])[x_range]) = ' '   #Replaces ship placed ('S') back to a blank space (' ')
                   user_ok = input('Press any key to continue')    
                   ship_length = 1   #Sets ship length value to one so it will not affect ship placement loop
                   return ship_length
            ((grid[ship_row])[x_range]) = 'S'   #Uses grid list to select column on grid then selects row and changes item in list to represent ship location
            ship_row = ship_row + 1   #Adds one to row so ship placement can move to next row to place ship
    return ship_length


def cpuShipPlacement(direction,cpu_grid,ship_row,ship_length,x_range,cpu_ships,cpu_point):   #Creates function to place program's ships on their grid 
    if ((cpu_grid[ship_row])[x_range]) == 'E':   #If program selects coordinate with a ship already placed, program does not place a ship and finds a new point
            return ship_length # returns the ship_length value
    if direction == 'h':  #If program selects to place the ship horizontally, this will display
        if (x_range + ship_length) > 10:   #If program selects a point in which ship will go off the grid, this will display
            return ship_length
        for ship_placement in range(ship_length):   #Loop begins to put ship on grid
            if ((cpu_grid[ship_row])[x_range]) == 'E':  #If the ship placement overlaps with another ship placed, this will display
                for ship_removal in range(ship_placement):   #Loop begins to undo ship placement by replacing previous 'E' placements back to ' '
                  x_range = x_range - 1  #Subtracts column by one to go back to undo ship placement
                  ((cpu_grid[ship_row])[x_range]) = ' '   #Replaces ship placed ('E') back to a blank space (' ')
                  if ship_length == 3:  #If second ship with length 3 is being removed, this will display
                        del((cpu_ships[ship_length])[3:6])   #Deletes points stored into list when ship was being placed
                  else:  #If any other ship is being placed, this will display
                        del((cpu_ships[ship_length])[0])  #Removes points that correspond with 'E's placed, resetting the list
                return ship_length
            ((cpu_grid[ship_row])[x_range]) = 'E'  #Uses grid list to select row on grid then selects column and changes item in list to represent ship location
            cpu_point = str(x_range) + str(ship_row)  #Concatenates current column and row values to act as a point for each 'E' placed
            cpu_ships[ship_length].append(cpu_point)  #Adds point to a list that corresponds with each ship placed
            x_range = x_range + 1   #Adds one to column so ship placement can move to next column to place ship
            
    elif direction == 'v':    #If program selects to place the ship vertically, this will display
        if (ship_row + ship_length) > 10:   #If program selects a point in which ship will go off the grid, this will display
            return ship_length
        for ship_placement in range(ship_length):   #Loop begins to put ship on grid
            if ((cpu_grid[ship_row])[x_range]) == 'E':   #If the ship placement overlaps with another ship placed, this will display
                for ship_removal in range(ship_placement):  #Loop begins to undo ship placement by replacing previous 'E' placements back to ' '
                  ship_row = ship_row - 1  #Subtracts row by one to go back to undo ship placement
                  ((cpu_grid[ship_row])[x_range]) = ' '  #Replaces ship placed ('E') back to a blank space (' ')
                  if ship_length == 3:  #If second ship with length 3 is being removed, this will display
                        del((cpu_ships[ship_length])[3:6])   #Deletes points stored into list when ship was being placed
                  else:  #If any other ship is being placed, this will display
                        del((cpu_ships[ship_length])[0])    #Removes points that correspond with 'E's placed, resetting the list
                return ship_length
            ((cpu_grid[ship_row])[x_range]) = 'E'   #Uses grid list to select column on grid then selects row and changes item in list to represent ship location
            cpu_point = str(x_range) + str(ship_row)  #Concatenates current column and row values to act as a point for each 'E' placed
            cpu_ships[ship_length].append(cpu_point)   #Adds point to a list that corresponds with each ship placed
            ship_row = ship_row + 1   #Adds one to row so ship placement can move to next row to place ship

    if ship_length == 3:      #If ship placement is successful, program will move onto next ship until each ship is placed successfully  
        ship_length = ship_length - 1
    elif ship_length == 2:
        ship_length = ship_length + 2
    else:
        ship_length = ship_length + 1
        
    return ship_length

def compShot():
  blanks(11) # calls blank spaces function to creates spaces between visual instances
  print('Enemy Turn') # tells the user that its the enemy turn 
  cpu_x = random.randint(0,9) # creates a var called cpu_x and puts a random number from 0 - 9 in it.
  cpu_y = random.randint(0,9) # does the same thing as above, except it puts a random value in a var called cpu_y
  ship_row = cpu_y # creates a variable called ship_row, and puts the value from cpu_y in it. This variable will be used to determine the y axis position on the grid
  x_range = cpu_x # creates a varaible called x_range, and puts the value from the cpu_x in it. This will be used as the computers x axis point selector on the grid
  if ((grid[ship_row])[x_range]) == 'S': # creates an if statement that will proceed if the item within the indexed list is 'S'
    ((grid[ship_row])[x_range]) = 'X' # if above is true, changes the 'S' to an 'X' to let the user know they've been shot there
    printgrid() # calls the printgrid() function after the cpu's turn
    compShotsHit() # calls the compShotHit() function becuase the computer hit the shot
  else: #else statement if the above is not true
     ((grid[ship_row])[x_range]) = 'O' # changes the item referenced in the list to 'O', indicating a missed shot.
     printgrid() # calls the printgrid() function after the cpu's turn
     compShotsMiss() # calls the compShotMiss() function because the computer missed
  blanks(11)
    

def userShot():  #Creates function to ask user to select a coordinate to place a shot on the program's grid
  print('Your turn!')
  printCpuGrid()  #Calls function to output enemy grid while hiding ship placements
  print(' ')
  point = userPointSelect()   #Calls function to get user point value
  x_range = point[0]   #Slices value into x and y values, x_range being the x value
  ship_row = point[1:3]
  ship_row = int(ship_row)
  ship_row = ship_row - 1  #Subtracts one from y value given to work in list selection
  x_range = columnChecker(x_range)   #Calls function to convert letter given to a number
  point = str(x_range) + str(ship_row)  #Concatenates x and y values together so it can be used to verify if user hit a ship and sunk it
  if ((cpu_grid[ship_row])[x_range]) == 'E':   #If user's point matches with an enemy ship, this will display
    ((visual_grid[ship_row])[x_range]) = 'X'  #Replaces point with an 'X', signifying a hit
    ((cpu_grid[ship_row])[x_range]) == 'X'  #Replaces point with an 'X', signifying a hit on invisible grid
    ship_check1 = cpu_ships[0].count(point)   #Variables made to count whether point matches with a specific ship
    ship_check2 = cpu_ships[1].count(point)
    ship_check3 = cpu_ships[2].count(point)
    ship_check4 = cpu_ships[3].count(point)
    ship_check5 = cpu_ships[4].count(point)
    ship_checks = [ship_check1,ship_check2,ship_check3,ship_check4,ship_check5]  #Creates list to select and verify which ship user hit
    counter = 0  #Sets counter to verify each ship in loop
    printCpuGrid()  #Calls function to output enemy grid while hiding ship placements
    user_shots_hit()  #Calls function to display to user that they have hit an enemy ship
    for test in ship_checks:  #Loop begins to verify which ship user hit 
        if test == 1:  #If user point matches a ship point, this will display
            boom = cpu_ships[counter].index(point)  #Finds index of the point of the ship that was hit  
            del((cpu_ships[counter])[boom])   #Removes point corresponding with user point, signifying a hit
            if cpu_ships[counter] == []:  #If all the points of the same ship has been hit, this will display
                print('\nYou sunk a ship!')  #Outputs to user that they have sunk a ship
                move_on = input('Nice!')
        counter = counter + 1  #Adds one to counter to check the next ship
  else:  #If user misses, this will display
    ((visual_grid[ship_row])[x_range]) = 'O'  #Replaces ' ' with an 'O', signifying a miss
    printCpuGrid()   #Calls function to output enemy grid while hiding ship placements
    user_shots_miss()  #Calls function to display to user that they have missed
  blanks(11)   #Calls function to output a certain amount of blanks
    

def user_shots_hit(): # defines a function which will be called if the user hit hit their shot
  print('\nYour shot has been fired. You landed a hit!') # lets the user know they've hit
  moveon = input('OK!') # moveon and move_on and user_ok variables are used through out as a way to ensure the user has read the message before the game proceeds

def user_shots_miss(): # defines a function which will be called if the user misses their shot
  print('\nYour shot has been fired. You missed.') # lets the user know they missed
  moveon = input('OK!')

def compShotsHit(): # defines a function which will be used to tell the user that the cpu hit its shot
  print('\nThe enemy fired. It hit your ship!') # tells the user that their ship has been hit
  moveon = input('OK!')  

def compShotsMiss(): # defines a function which will be used to tell
  print('\nThe enemy fired. It missed.')
  moveon = input('OK!')

def blanks(number):
    print('\n' * number)



####VARIABLE SETS####

row1 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']   #Creates list to set user's grid and adds ships and program shots during the game
row2 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
row3 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
row4 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
row5 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
row6 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
row7 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
row8 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
row9 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
row10= [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

cpu_row1 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']   #Creates list to set program's grid to set and hide ships from user
cpu_row2 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
cpu_row3 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
cpu_row4 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
cpu_row5 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
cpu_row6 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
cpu_row7 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
cpu_row8 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
cpu_row9 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
cpu_row10= [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

visual_row1 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']   #Creates list to set a visual grid of the program's ships and user shots during game
visual_row2 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
visual_row3 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
visual_row4 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
visual_row5 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
visual_row6 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
visual_row7 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
visual_row8 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
visual_row9 = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
visual_row10= [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

grid = [row1,row2,row3,row4,row5,row6,row7,row8,row9,row10]   #Creates list of user grid rows so ships can be added vertically
cpu_grid = [cpu_row1,cpu_row2,cpu_row3,cpu_row4,cpu_row5,cpu_row6,cpu_row7,cpu_row8,cpu_row9,cpu_row10]   #Creates list of program grid rows so ships can be added vertically
visual_grid = [visual_row1,visual_row2,visual_row3,visual_row4,visual_row5,visual_row6,visual_row7,visual_row8,visual_row9,visual_row10]

error_checker = True # create boolean to use in exception handling. Initial value set to True

topbar = (' _____________________________________________________') # creates a variable called 'topbar' and puts the top part of the visually displayed grid in it. Since there are no 
row0letters = ('|   | A  | B  | C  | D  | E  | F  | G  | H  | I  | J  |')

user_ship_placement = True  #Sets boolean to allow user to place ships
cpu_ship_placement = True  #Sets boolean to allow program to place ships
user_carrier = 1   #Sets user ship variables
user_battleship = 1
user_cruiser = 2
user_destroyer = 1
cpu_ship1 = []  #Sets program ship lists, storing every point ship is placed on
cpu_ship2 = []
cpu_ship3 = []
cpu_ship4 = []
cpu_ship5 = []
cpu_ships = [None,None,cpu_ship1,cpu_ship2,cpu_ship3,cpu_ship4,cpu_ship5]  #Creates list of ships to be accessed when shooting ships

game_loop = True 

####MAIN PROGRAM####


while Flag == True:
    print(' \n \n \n \n ')
    print('                                                  .  o ..')
    print('                                                  o . o o.o')
    print('                                                       ...oo')
    print('  ____        _   _   _           _     _       ' + '         __[]__   ')
    print(' | __ )  __ _| |_| |_| | ___  ___| |__ (_)_ __  ' + '      __|_o_o_o\__    ')
    print(" |  _ \ / _` | __| __| |/ _ \/ __| '_ \| | '_ \ " + '      \\""""""""""/     ')
    print(' | |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) |' + '       \. ..  . /     ')
    print(' |____/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/ ' + '   ^^^^^^^^^^^^^^^^^^^^    ')
    print('                                         |_|    ')
    print(' \n \n \n \n ')
    print('Welcome to the game of Battleship!')
    print(' ')
    print('S - Start the game')
    print('H - Help / Instructions')
    print('Q - Quit the game')
    print(' ')
    
    user_choice = input('Input a letter and press enter: ')      #Asks the user for a command
    print(' ')

    if user_choice == 'H' or user_choice == 'h':    #If user types h for help, program displays information about the program
        print("Objective \n \nThe objective of the game is to sink all of your opponent's ships before they sink yours. \n \nRules  \n \nYou cannot place a ship overlapping your own ship or going off the grid. \nYou have 5 ships: one carrier(5 spaces long), one battleship(4 spaces long), two cruisers(3 spaces long), and one destroyer(2 spaces long.') ")
        print('Remember: Placing your ships strategically can turn the game in your favour! \n\n')
        user_ok = input('Press any key to continue.')
        Flag_user = True    #Lets the program begin the main program
        Flag = False   #Ends the menu loop, allowing the program to start
    elif user_choice == 'S' or user_choice == 's':  #If user types s program will start
        Flag_user = True    #Lets the program begin the main program
        Flag = False  #Ends the menu loop, allowing the program to start
        print(' ')
    elif user_choice == 'Q' or user_choice == 'q':        #If user types q then loop and program will end
        Flag = False    #Ends the whole program
        Flag_user = False
    else:
        print('Invalid Command. Please restart the program and enter a letter again.')   #If user types a letter that isn't s, h, or q, this will display
        Flag_user = False  #Replays menu loop

    while Flag_user == True: #Main loop program begins

        printgrid()  #Calls function to output their grid to user

        while user_ship_placement == True:   #Begins loop to get user's input on ship placement
            blanks(2)
            error_checker = True  #Boolean set to true so errors can be checked and solved
            while error_checker == True:  #Loop begins to check error in ship length input
                try:
                    ship_length = input('Choose a ship length: ')   #Asks user for ship length value
                    ship_length = int(ship_length)
                    error_checker = False  #If correct ship length is inputted without error, program will move on
                except ValueError:  #If user runs into value error, program will output to user to enter a valid value
                    print('You entered an invalid length. Try again!')
            if ship_length < 2 or ship_length > 5:  #If user enters a ship length too high or low, program will output to user to enter a valid length
                print('You have entered an incorrect ship length, please try again. Remember, ship length can be 2,3,3,4,5.')
            elif ship_length == 5 and user_carrier == 0 or ship_length == 4 and user_battleship == 0 or ship_length == 3 and user_cruiser == 0 or ship_length == 2 and user_destroyer == 0:   #If user inputs a ship length that has already been used, this will display
                print('You have entered a ship that you have already placed, please enter a new ship.')  #Program will output to user to try again
            else:  #If user enters all the correct info, program will move on 
                
                print('What point does the head of your ship start?') 
                user_point = userPointSelect()  #Calls function to ask user for point value
                x_range = user_point[0]   #Slices input for x and y coordinate values
                ship_row = user_point[1:3]
                ship_row = int(ship_row)
                

                error_checker = True   #Boolean set to true so errors can be checked and solved
                while error_checker == True:  #Loop begins to check error in ship direction input
                    user_ship_direction = input('Would you like to place your ship horizontally (enter "H") or vertically (enter "V")?: ')  #Asks user for ship direction value
                    if user_ship_direction.lower() == 'h' or user_ship_direction.lower() == 'v':  #If user enters correct value, this will display
                        error_checker = False   #If correct ship direction is inputted without error, program will move on
                    else:  #If user enters an incorrect value, this will display
                        print('Please enter the correct letter for the direction.')  #Outputs to user to try again

                
                x_range = columnChecker(x_range)  #Calls function to convert letter value to a number to be used in ship placement

                ship_row = ship_row - 1  #Subtracts value by one so it can be used with lists
                ship_length = shipPlacement(user_ship_direction,grid,ship_row,ship_length,x_range)  #Calls function to place ship on grid

                if ship_length == 5:  #If ship was placed successfully, variables will be subtracted by one for each ship placed successfully until all ships have been placed
                    user_carrier = user_carrier - 1
                elif ship_length == 4:
                    user_battleship = user_battleship - 1
                elif ship_length == 3:
                    user_cruiser = user_cruiser - 1
                elif ship_length == 2:
                    user_destroyer = user_destroyer - 1
                else:
                    print('')
                    user_ok = input('(enter to continue)')
                    
                if user_carrier == 0 and user_battleship == 0 and user_cruiser == 0 and user_destroyer == 0:  #If all ships have been placed successfully, this will display
                    user_ship_placement = False   #Ends user ship loop 
                else:
                    blanks(5)  #Calls function to output a certain amount of blanks
                    printgrid()  #Calls function to output their grid to user

        blanks(11)  #Calls function to output a certain amount of blanks
        printgrid()  #Calls function to output their grid to user


        while cpu_ship_placement == True:  #Begins loop to add program's ships to their grid
            ship_length = 3  #Sets starting ship length value to 2, increasing by one with each successful placement
            while ship_length < 6:   #Begins loop to add program's ships until all ships have been successfully placed
              cpu_point = cpuPointSelect()   #Calls function to randomly select point and returns it
              x_range = cpu_point[0]
              ship_row = cpu_point[1]
              ship_row = int(ship_row)
              x_range = int(x_range)
                
              cpu_ship_direction = random.randint(1,2)
              if cpu_ship_direction == 1:
                cpu_ship_direction = 'h'
              elif cpu_ship_direction == 2:
                cpu_ship_direction = 'v'

              ship_length = cpuShipPlacement(cpu_ship_direction,cpu_grid,ship_row,ship_length,x_range,cpu_ships,cpu_point)

            ship_length = 3
            while ship_length == 3:
              cpu_point = cpuPointSelect()
              x_range = cpu_point[0]
              ship_row = cpu_point[1]
              ship_row = int(ship_row)
              x_range = int(x_range)

              cpu_ship_direction = random.randint(1,2)
              if cpu_ship_direction == 1:
                cpu_ship_direction = 'h'
              elif cpu_ship_direction == 2:
                cpu_ship_direction = 'v'

              ship_length = cpuShipPlacement(cpu_ship_direction,cpu_grid,ship_row,ship_length,x_range,cpu_ships,cpu_point)
                
            cpu_ship5.append(cpu_ship2[3])
            cpu_ship5.append(cpu_ship2[4])
            cpu_ship5.append(cpu_ship2[5])
            del(cpu_ship2[3:6])
            del(cpu_ships[0:2])
            cpu_ship_placement = False
                
            
        while game_loop == True:
          
            compShot()
            userShot()

            if cpu_ships[0] == [] and cpu_ships[1] == [] and cpu_ships[2] == [] and cpu_ships[3] == [] and cpu_ships[4] == []:
                print('Congratulations! You sunk all of the enemy ships!')
                game_win()
                game_loop = False
                Flag = True
                Flag_user = False
            elif row1.count('S') == 0 and row2.count('S') == 0 and row3.count('S') == 0 and row4.count('S') == 0 and row5.count('S') == 0 and row6.count('S') == 0 and row7.count('S') == 0 and row8.count('S') == 0 and row9.count('S') == 0 and row10.count('S') == 0:
                print('The enemy sunk all of your ships, you lost.')
                game_loop = False
                Flag = True
                Flag_user = False
