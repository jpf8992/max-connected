#!/usr/bin/python

from matrix import Matrix
from recursiveSearch import recursiveSearch
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
	# my_grouping[0] = [current_grouping, 0, 0, 0] # pick first element as initial group - arbitrary!
	my_grouping[0] = [0, 0, 0, 0] # pick first element as initial group - arbitrary!
	print(my_grouping)


	#Iterate through each group element that is zero - i.e. unassigned
	for row_count, elem in enumerate(my_grouping):
		
		for col_count, val in enumerate(elem):
			
			# print("\n**********************************")
			# print("Row Num: " + str(row_count) ,elem)
			# print("Col Num: " + str(col_count),val)

			if(val == 0):	# tile yet to be assigned

				# Assign new group to tile
				my_grouping[row_count][col_count] = current_grouping
				print("\n**********************************")

				# Find valid surrounding tiles
				valid_neighbour_tiles = my_mat.getValidNeighbours(row_count, col_count)
				# print("valid_neighbour_tiles: " , valid_neighbour_tiles)
				# Get value of element in my_mat
				curr_tile_value = my_mat[row_count][col_count]
				# print("Tile Value: " , curr_tile_value)
				
				recursiveSearch( my_mat, my_grouping, row_count, col_count, current_grouping)

				print("Current Grouping",current_grouping)
				current_grouping +=1 # increment to next grouping


			print("**********************************\n")


	print("Newly Generated Grouping Matrix: ")
	print(my_grouping)



	





if __name__ == "__main__":

    main()