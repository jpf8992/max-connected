#!/usr/bin/python

from matrix import Matrix
import operator
import sys

def main():

	# Keep track of linked groups of connected tiles
	current_grouping = 1
	curr_tile_value = None

	# Create new matrix from file
	print("\nCreating Test Matrix:")
	my_mat = Matrix.readGrid("testMatrix.txt")
	print(my_mat)


	# Create another matrix (of same rank) to store connected group identifiers
	(y_height, x_width) = my_mat.getRank()
	print("Initializing Grouping Matrix:")
	my_grouping = Matrix.makeZero(y_height,x_width)
	# my_grouping[1] = [4, 4, 4, 4] # Test Set
	print(my_grouping)


	#Iterate through each group element that is zero - i.e. unassigned
	for row_count, elem in enumerate(my_grouping):
		
		for col_count, val in enumerate(elem):
			
			print("\n**********************************")
			print("Row Num: " + str(row_count) ,elem)
			print("Col Num: " + str(col_count),val)

			if(val == 0):	# tile yet to be assigned

				# Find valid surrounding tiles
				valid_neighbour_tiles = my_mat.getValidNeighbours(row_count, col_count)
				# print("valid_neighbour_tiles: " , valid_neighbour_tiles)
				# Get value of element in my_mat
				curr_tile_value = my_mat[row_count][col_count]
				# print("Tile Value: " , curr_tile_value)
				


				# Determine if neighbouring tiles are same value
				# - disregard tiles that have already been categoriesd,
				# i.e. my_grouping value other than zero

				for direction , valid in valid_neighbour_tiles.items():

					if(valid and direction == 'above'): # is a valid tile within bounds

						value_above = my_mat[row_count - 1][col_count]
						if(curr_tile_value == value_above):
							print("** Match Found Above **")
							print("Curr Tile: " + str(curr_tile_value) , "Above Tile: " + str(value_above))


					if(valid and direction == 'right'):

						value_right = my_mat[row_count][col_count + 1]
						if(curr_tile_value == value_right):
							print("** Match Found Right **")
							print("Curr Tile: " + str(curr_tile_value) , "Right Tile: " + str(value_right))


					if(valid and direction == 'below'):

						value_below = my_mat[row_count + 1][col_count]
						if(curr_tile_value == value_below):
							print("** Match Found Below **")
							print("Curr Tile: " + str(curr_tile_value) , "Below Tile: " + str(value_below))
					

					if(valid and direction == 'left'):

						value_left = my_mat[row_count][col_count - 1]
						if(curr_tile_value == value_left):
							print("** Match Found Left **")
							print("Curr Tile: " + str(curr_tile_value) , "Left Tile: " + str(value_left))
					
				print("**********************************\n")









if __name__ == "__main__":

    main()