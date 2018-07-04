import math

def twoNorm(vector):
  '''
  twoNorm takes a vector as it's argument. It then computes the sum of  the squares of each element of the vector. It then returns the square root of this sum.
  '''
  # This variable will keep track of the validity of our input.
  inputStatus = True  
  # This for loop will check each element of the vector to see if it's a number. 
  for i in range(len(vector)):  
    if ((type(vector[i]) != int) and (type(vector[i]) != float) and (type(vector[i]) != complex)):
      inputStatus = False
      print("Invalid Input")
  # If the input is valid the function continues to compute the 2-norm
  if inputStatus == True:
    result = 0
# This for loop will compute the sum of the squares of the elements of the vector. 
    for i in range(len(vector)):
      result = result + (vector[i]**2)
    result = result**(1/2)
    return result


def normalize(vector07):
	'''
	This function takes a vector as its argument and returns the normalized vector with respect to 
	the infinity norm. First we create a variable where we call the function infNorm but with vector07
	as its respective input. Then we create an empty list. We check if the input is indeed a list and
	if it is we execute the respective multiplication and append the results into the empty list.

	'''
	sup = twoNorm(vector07)
	newVec = []
	if sup == 0 or sup == 1:
		return vector07
	elif type(vector07) != list: 
		print("invalid input")
	else:
		for i in range(len(vector07)):
			norm = (1.0/sup)*vector07[i]
			newVec.append(norm)
	return newVec



def dot(vector01,vector02):
	'''
	This function takes two vectors as it's arguments and returns the dot product of them. First
	we identify whether or not the vectors are of same size, if they are continue if not we print 
	invalid input. If we continue then we execute the algorithm to find the dot product.

	'''

	add = 0
	if len(vector01) != len(vector02):
		print("invalid input")

	else:
		for i in range(len(vector01)):
			add += (vector01[i] * vector02[i])
		return add



def scalarVecMulti(scalar01,vector05):
	'''
	This functions takes a scalar and a vector as arguments and returns a new vector with the respective
	multiplication executed. The if-else statement checks for the scalar and vector to bbe either integers
	or lists, if they are then we proceed to execute the multiplication by appending to an empty list the
	result of the executed multiplication between the scalar and each individual element in the vector.

	'''
	newVec = []
	if type(scalar01) != int and type(scalar01) != float and type(scalar01) != complex:
		print("invalid input")
	elif type(vector05) != list:
		print("invalid input")
	else:
		for i in range(len(vector05)):
			mult = vector05[i]*scalar01
			newVec.append(mult)

		return newVec




def vecSubtract(vector03,vector04):
	'''
	This functions takes two vectors as arguments and returns a new vector with the respective subraction. We
	first create an empty list, then check for dimensions of inputs and if they checkout, execute subraction 
	and append element's subraction onto empty list in order to create new list with subraction finished.

	'''
	newVec = []
	if len(vector03) != len(vector04):
		print("invalid input")

	else:
		for i in range(len(vector03)):
			sub = vector03[i] - vector04[i]
			newVec.append(sub)
	return newVec


def GS(A):
	'''
		This function takes the x-values hardcoded into matrix A and takes each column as a vector in order to compute the
		modified gram-schmidt appropriately. The R matrix is computed by initially creating a matrix with the appropriate 
		dimensions with only 0 as values and then changing the value of the distinct values into the appropriate values as
		the algorithm runs. The Q matrix is an empty list that will be appended by the appropriate values in order to be
		correctly filled with the right values. Finally, we return matrices Q and R as a list so that they are easily
		accessible. 

	'''
	if type(A[i]) != int and type(A[i]) != float and type(A[i]) != complex:
		print("invalid input")
	else:
		col = len(A)
		row = len(A[0])
		V = A
		R = [[0]*col for i in range(col)]
		Q = []

		for i in range(col):
			R[i][i] = twoNorm(V[i])
			number = 1/(R[i][i])
			Qi = scalarVecMulti(number,V[i])
			Q.append(normalize(V[i]))
			for j in range(i+1,col):
				R[j][i] = dot(Q[i],V[j])
				temp = scalarVecMulti(R[j][i],Q[i])
				V[j] = vecSubtract(V[j],temp)
		return [Q,R]


def transMatVec(mat,vec):

	'''
	This function takes a matrix and a vector as its arguments and computes the appropriate multiplication. After each 
	iteration of i, the empty list sup is appended until we have a new vector with the correct values.

	'''
	
	sup = []

	for i in range(len(mat)):
		sum = 0
		for j in range(len(vec)):
			sum += (mat[i][j] * vec[j])
		sup.append(sum)
	return sup


#Below we have matrix y and A. Matrix y is just a list of all the y-values, but matrix A is the vandermode matrix developed in columns.


y = [1.102,1.099,1.017,1.111,1.117,1.152,1.265,1.380,1.575,1.857]

A = [[1,1,1,1,1,1,1,1,1,1],[0.55,0.60,0.65,0.70,0.75,0.80,0.85,0.90,0.95,1],[0.3025,0.36,0.4225,0.49,0.5625,0.64,0.7225,0.81,0.9025,1],[0.166375,0.216,0.274625,0.343,0.421875,0.512,0.614125,0.729,0.857375,1]]

#The variable QR is used to easily access the Q matrix and the R matrix from the gram-schmidt function above. 

QR = GS(A)

#Variables Q and R are the already found matrices from the QR factorization that will be used in order to obtain the correct coefficients.

Q = QR[0]
R = QR[1]

#Variable b is the result of the multiplication of the transpose of Q and the appropriate y values.

b = transMatVec(Q,y)

def BackSub(R,b):

	'''

	This function takes matrix R and vector b and performs a back substitution with the intention of finding the values
	of the coefficients c. We use the function reversed because we are solving an upper triangle matrix, meaning that
	the easiest coefficient to find lies at the bottom of the matrix and thus we should begin iterating from the
	bottom up. After running the algorithm we return the desired list c that is the list of coefficients in order.

	'''
	k = len(b) - 1
	c = [0]*len(b)
	c[k] = b[k]/(R[k][k])
	for i in reversed(range(len(b))):
		c[i] = b[i]
		for j in range(i + 1,len(b)):
			c[i] = c[i] - c[j]*R[j][i]
		c[i] = c[i]/(R[i][i])
	return c

#A few print outputs that properly answer all the questions from the quiz, the uncommented one returns the list of coefficients.


#print(transMatVec(QR[0],y))
#print(GS(A))


print(BackSub(R,b))