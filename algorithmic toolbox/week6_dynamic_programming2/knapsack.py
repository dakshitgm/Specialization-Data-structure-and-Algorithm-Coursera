# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
	value=[[0 for _ in range(W+1)] for _ in range(len(w)+1)]
	for i in range(1, len(w)+1):
		cubar=w[i-1]
		for weight in range(1, W+1):
			value[i][weight]=value[i-1][weight]
			if cubar<=weight:
				value[i][weight]=max(value[i-1][weight-cubar]+cubar, value[i][weight])
	result = value[len(w)][W]
    
	return result

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
