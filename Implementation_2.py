# GIT hub https://github.com/aldisgeirdal/tileTraveller

# 1. Which implementation was easier and why?
#   It was easier breaking down each assignment in the algorithm down to smaller pieces. However I 
#   had a hard time deciding which functions to make and how to make them. I started with a while loop
#   in the main program, but moved some of them to the functions. I learned a lot, but it took 
#   a long time to get my mind around it all.
# 2. Which implementation is more readable and why?
#   The main program is more readable, as it calls the functions rather than itering through each tile everytime.
#   it is more readable to have the iteration through each tile within a function.
# 3. Which problems in the first implementations were you able to solve with the latter
# implementation?
#   First I thought it would be impossible to make the program, i.e. a readable program, without using 
#   functions, however, it became a struggle when I started to make the functions afterwards, as 
#   I had a hard time turning the program around, after having written it once. 

def victory(x, y):
    if (x == 3 and y == 1):
        return False
    else:
        return True

def instructions (x, y):
    """Fallið gefur notanda upplýsingar um hvert hann má fara á þeim reit sem hann er staddur á."""
    if (x == 1 and y == 1) or (x == 2 and y == 1):   #tiles 1,1 and 2,1 are the same.
        print("You can travel: (N)orth.")
    elif x == 1 and y == 2:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
    elif x == 1 and y == 3:
        print("You can travel: (E)ast or (S)outh.")
    elif x == 2 and y == 3:
        print("You can travel: (E)ast or (W)est.")
    elif (x == 2 and y == 2) or (x == 3 and y == 3): # tiles 2,2 and 3,3 are the same.
        print("You can travel: (S)outh or (W)est.")
    elif x == 3 and y == 2:
        print("You can travel: (N)orth or (S)outh.")
    else:
        print("Victory!")
        return False
    return True

def movements (direction, x, y):
    north = "nN"    # up     y += 1
    east = "eE"     # right  x += 1
    south = "sS"    # down   y -= 1
    west = "wW"     # left   x -= 1
    while x <= 3 and y <= 3:
        if direction in north:
            if ((x==1 and y ==1) or (x == 2 and y == 1) or (x == 3 and y == 2) or (x == 1 and y == 2)):
                y += 1
                break   
            else:
                print("Not a valid direction!")
                return (x, y)
        elif direction in east:
            if ((x == 1 and y == 2) or (x == 1 and y == 3) or (x == 2 and y == 3)):
                x += 1
                break
            else:
                print("Not a valid direction!")
                return (x, y)
        elif direction in south:
            if ((x == 1 and y == 2) or (2 == 1 and y == 2) or (x == 3 and y == 3) or (x == 3 and y == 2) or (x == 2 and y == 2)):
                y -= 1  
                break  
            else:
                print("Not a valid direction!")
                return (x, y)
        elif direction in west:
            if (x == 2 and y == 3) or (x == 2 and y == 2) or (x == 3 and y == 3):    
                x -= 1 
                break
            else: 
                print("Not a valid direction!")   
                return (x, y)
        else:
            print("Not a valid direction!")   
            return (x, y)
    return (x, y)

x = 1
y = 1
x_1 = 1
y_1 = 1

while True:
    instructions(x, y)
    if not victory(x, y):
        break
    while victory(x, y):
        direction = input("Direction: ")
        x, y = movements(direction, x, y)
        if x_1 == x and y_1 == y:
            pass
        else:
            x_1, y_1 = x, y
            break

