# Uses python3
def edit_distance(s, t):
    #write your code here
	s=' '+s
	t=' '+t
	l1=len(s)
	l2=len(t)
	distances=[[(i+j) for i in range(l1)] for j in range(l2)]
		
	for i in range(1, l2):
		for j in range(1, l1):
			if(s[j]==t[i]):
				distances[i][j]=min(distances[i-1][j-1], distances[i-1][j]+1, distances[i][j-1]+1)
			else:
				distances[i][j]=min(distances[i-1][j-1]+1, distances[i-1][j]+1, distances[i][j-1]+1)
	return distances[l2-1][l1-1]
if __name__ == "__main__":
    print(edit_distance(input(), input()))
