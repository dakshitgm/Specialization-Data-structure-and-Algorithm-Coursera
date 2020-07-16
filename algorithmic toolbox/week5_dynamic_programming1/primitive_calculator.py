# Uses python3
import sys

def optimal_sequence(n):
	sequence = [n]
	sq=[0]*(n+1)
	orn=[0]*(n+1)
	for i in range(2, n+1):
		no_operation=sq[i-1]+1
		orn[i]=i-1
		if i%2==0: 
			db2=sq[i//2]+1
			if db2<no_operation:
				no_operation=db2
				orn[i]=i//2
		if i%3==0:
			db2=sq[i//3]+1
			if db2<no_operation:
				no_operation=db2
				orn[i]=i//3
		sq[i]=no_operation
	while(n>1):
		n=orn[n]
		sequence.append(n)
	return sequence

input = sys.stdin.read()
n = int(input)
sequence=optimal_sequence(n)
print(len(sequence) - 1)
for x in reversed(sequence):
    print(x, end=' ')
