
R = 6
C = 5


def printMaxSubSquare(M):

	global R, C
	Max = 0

	
	S = [[0 for col in range(C)]for row in range(2)]


	for i in range(R):
		for j in range(C):

			
			Entrie = M[i][j]
			if(Entrie):
				if(j):
					Entrie = 1 + min(S[1][j - 1], min(S[0][j - 1], S[1][j]))

			# Save the last entrie and add the new one
			S[0][j] = S[1][j]
			S[1][j] = Entrie

			# Keep track of the max square length
			Max = max(Max, Entrie)

	# Print the square
	print("Maximum size sub-matrix is: ")
	for i in range(Max):
		for j in range(Max):
			print("1", end=" ")
		print()
