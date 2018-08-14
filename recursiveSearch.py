
from matrix import Matrix

def recursiveSearch( testMartrix, groupMatrix, row_cordinate, col_cordinate, current_grouping):

	print("\n\nCurrent Tile: " + str(row_cordinate) + ',' + str(col_cordinate))
	
	valid_neighbour_tiles = testMartrix.getValidNeighbours(row_cordinate, col_cordinate)
	print("Valid Tiles :" + str(valid_neighbour_tiles))
	curr_tile_value = testMartrix[row_cordinate][col_cordinate]

	for direction , valid in valid_neighbour_tiles.items():


			# Function for these if statements would look better???


			
			if(valid and direction == 'above'): # is a valid tile within bounds

				value_above = testMartrix[row_cordinate - 1][col_cordinate]
				group_val_above = groupMatrix[row_cordinate - 1][col_cordinate]

				if(curr_tile_value == value_above and group_val_above == 0):
					
					groupMatrix[row_cordinate - 1][col_cordinate] = current_grouping
					print("** Match Found Above  -- Grouping Unassigned **")
					print("Curr Tile: " + str(curr_tile_value) , "Above Tile: " + str(value_above))
					print("Starting Nested Search Above")
					recursiveSearch(testMartrix, groupMatrix, row_cordinate - 1, col_cordinate, current_grouping)


			if(valid and direction == 'right'):

				value_right = testMartrix[row_cordinate][col_cordinate + 1]
				group_val_right = groupMatrix[row_cordinate][col_cordinate + 1]

				if(curr_tile_value == value_right and group_val_right == 0):

					groupMatrix[row_cordinate][col_cordinate + 1] = current_grouping
					print("** Match Found Right -- Grouping Unassigned **")
					print("Curr Tile: " + str(curr_tile_value) , "Right Tile: " + str(value_right))
					print("Starting Nested Search Right")
					recursiveSearch(testMartrix, groupMatrix, row_cordinate, col_cordinate + 1, current_grouping)


			if(valid and direction == 'below'):

				value_below = testMartrix[row_cordinate + 1][col_cordinate]
				group_val_below = groupMatrix[row_cordinate + 1][col_cordinate]

				if(curr_tile_value == value_below and group_val_below == 0):

					groupMatrix[row_cordinate + 1][col_cordinate] = current_grouping
					print("** Match Found Below -- Grouping Unassigned **")
					print("Curr Tile: " + str(curr_tile_value) , "Below Tile: " + str(value_below))
					print("Starting Nested Search Below")
					recursiveSearch(testMartrix, groupMatrix, row_cordinate + 1, col_cordinate, current_grouping)
			

			if(valid and direction == 'left'):

				value_left = testMartrix[row_cordinate][col_cordinate - 1]
				group_val_left = groupMatrix[row_cordinate][col_cordinate - 1]

				if(curr_tile_value == value_left and group_val_left == 0):

					groupMatrix[row_cordinate][col_cordinate - 1] = current_grouping
					print("** Match Found Left -- Grouping Unassigned **")
					print("Curr Tile: " + str(curr_tile_value) , "Left Tile: " + str(value_left))
					print("Starting Nested Search Left")
					recursiveSearch(testMartrix, groupMatrix, row_cordinate, col_cordinate -1, current_grouping)




			print("Finished Recursive Search! ")
