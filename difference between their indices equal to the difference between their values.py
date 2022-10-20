# Python3 program for the above approach

# Function to find the maximum sum of
# a subsequence having difference between
# indices equal to difference in their values
def maximumSubsequenceSum(A, N):
	
	# Stores the maximum sum
	ans = 0

	# Stores the value for each A[i] - i
	mp = {}

	# Traverse the array
	for i in range(N):
		if (A[i] - i in mp):
			
			# Update the value in map
			mp[A[i] - i] += A[i]
		else:
			mp[A[i] - i] = A[i]
			
		# Update the answer
		ans = max(ans, mp[A[i] - i])

	# Finally, print the answer
	print(ans)

# Driver Code
if __name__ == '__main__':
	
	# Given Input
	A = [ 10, 7, 1, 9, 10, 1 ]
	N = len(A)

	# Function Call
	maximumSubsequenceSum(A, N)


