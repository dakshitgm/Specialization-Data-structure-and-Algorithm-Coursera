# Uses python3
import sys
import itertools

def partition3(A):
	if len(A)<3:
		return 0
	total=sum(A)
	if total%3!=0:
		return 0
	value=[[0 for _ in range(total+1)] for _ in range(len(A)+1)]
	for i in range(1, len(A)+1):
		cubar=A[i-1]
		for weight in range(1, total+1):
			value[i][weight]=value[i-1][weight]
			if cubar<=weight:
				value[i][weight]=max(value[i-1][weight-cubar]+cubar, value[i][weight])
	v=total//3
	if value[len(A)][v]==v and value[len(A)][v*2]:
		return 1
	return 0
def sum(a):
	sum=0
	for i in a:
		sum+=i
	return sum
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

