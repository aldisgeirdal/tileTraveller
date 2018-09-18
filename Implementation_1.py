# Algorithm for Tile Traveller:
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

