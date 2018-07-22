#!/usr/bin/python3

from matrix import Matrix


def main():


	# Create new board
	y_length = 4
	x_width = 3
	my_mat = Matrix.readGrid("testMatrix.txt")
	print(my_mat)




if __name__ == "__main__":

    main()