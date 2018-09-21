# GIT hub https://github.com/aldisgeirdal/tileTraveller

# 1. Which implementation was easier and why?
# 2. Which implementation is more readable and why?
# 3. Which problems in the first implementations were you able to solve with the latter
# implementation?
      

def instructions (x, y):
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
        
    if direction in north:
        if ((x==1 and y ==1) or (x == 2 and y == 1) or (x == 3 and y == 2) or (x == 1 and y == 2)):
            y += 1   
            break
        else:
            print("Not a valid direction!")
            return (x,y)
    elif direction in east:
        if ((x == 1 and y == 2) or (x == 1 and y == 3) or (x == 2 and y == 3)):
            x += 1
            break
        else:
            print("Not a valid direction!")
            return (x,y)
    elif direction in south:
        if ((x == 1 and y == 2) or (2 == 1 and y == 2) or (x == 3 and y == 3) or (x == 3 and y == 2) or (x == 2 and y == 2)):
            y -= 1
            break
        else:
            print("Not a valid direction!")
            return (x,y)
    elif direction in west:
        if ((x == 2 and y == 3) or (x == 2 and y == 2) or (x == 3 and y == 3)):
            x -= 1 
            break
        else:
            print("Not a valid direction!")
            return (x,y)
    else: 
        print("Not a valid direction!")
        break
    return (x, y)

def victory(x, y):
    if (x == 3 and y == 1):
        return False
    else:
        return True

while True:
    x = 1
    y = 1
    instructions(x, y)

    if not victory(x, y):
        break
    while 1 <= x <= 3 and 1 <= y <= 3:
        direction = input("Direction: ")
        x, y = movements(direction, x, y)
        