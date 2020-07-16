# Uses python3
import sys

def optimal_summands(n):
	summands = []
    #write your code here
	cut=1
	while(n):
		if(n-cut<=cut):
			summands.append(n)
			n=0
		else:
			summands.append(cut)
			n=n-cut
			cut=cut+1
	return summands

if __name__ == '__main__':
	input = sys.stdin.read()
	n = int(input)
	summands = optimal_summands(n)
	print(len(summands))
	for x in summands:
		print(x, end=' ')
