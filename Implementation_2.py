x = 1
y = 1

north = "nN"    # up     y += 1
east = "eE"     # right  x += 1
south = "sS"    # down   y -= 1
west = "wW"     # left   x -= 1

while True:
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
        break    

    while 1 <= x <= 3 and 1 <= y <= 3:
        direction = input("Direction: ")
        if direction in north and ((x==1 and y ==1) or (x == 2 and y == 1) or (x == 3 and y == 2) or (x == 1 and y == 2)):
            y += 1
            break
        elif direction in east and ((x == 1 and y == 2) or (x == 1 and y == 3) or (x == 2 and y == 3)):
            x += 1
            break
        elif direction in south and ((x == 1 and y == 2) or (2 == 1 and y == 2) or (x == 3 and y == 3) or (x == 3 and y == 2)):
            y -= 1
            break
        elif direction in west and ((x == 2 and y == 3) or (x == 2 and y == 2) or (x == 3 and y == 3)):
            x -= 1
            break
        else: 
            print("Not a valid direction!")