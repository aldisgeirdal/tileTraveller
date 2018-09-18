# GIT hub https://github.com/aldisgeirdal/tileTraveller

# Algorithm for Tile Traveller:
# Player:
# 1. There are 9 tiles, three rows and three columns. 
#       Some of the walls of the tiles have openings, but not all.
#       The one marked 1,1 is at the left bottom.
#       The one above is marked 1,2.
#       The one marked 3,1 is at the right bottom. That is the vicctory location.
# 2. The player starts at tile 1,1.
# 3. Player is informed of possible travel options.
# 4. Player is asked to move.  
# 5. If player moves to a direction not available - let player know that direction is not valid. Go back to 4.
# 6. If player moves to a direction available, relocate player in program and go back to 3.
# 7. If player is located in tile 3,1, player is in victory location. Inform player he is in victory location.

# Program
# 1. Figure out on what tile player is located.
# 2. Inform player of possible moves, depending on where player is located.
# 3. Ask player for direction.
# 4. If direction is valid - change location of player (change x or y).
# 5. If direction is not valid - inform player. Go back to 3.
# 6. If player is on tile 3,3 - inform player he is in victory location.

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
        elif direction in south and ((x == 1 and y == 2) or (2 == 1 and y == 2) or (x == 3 and y == 3) or (x == 3 and y == 2) or (x == 2 and y == 2)):
            y -= 1
            break
        elif direction in west and ((x == 2 and y == 3) or (x == 2 and y == 2) or (x == 3 and y == 3)):
            x -= 1
            break
        else: 
            print("Not a valid direction!")
