#!/usr/bin/python

from matrix import Matrix


def main():


	# Create new matrix from file
	y_height = 4
	x_width = 3
	print("Creating Test Matrix")
	my_mat = Matrix.readGrid("testMatrix.txt")
	print(my_mat)

	# Create another matrix (of same rank) to store connected group identifiers
	(y_height, x_width) = my_mat.getRank()
	print("Creating Grouping Matrix")
	my_grouping = Matrix.makeZero(y_height,x_width)
	print(my_grouping)


	my_mat(1,9)

	print(my_mat)






if __name__ == "__main__":

    main()