#Uses python3

import sys

def lcs2(a, b):
	#write your code here
	l1=len(a)
	l2=len(b)
	seq=[[0 for _ in range(l1+1)] for _ in range(l2+1)]
	for i in range(l1):
		for j in range(l2):
			if a[i]==b[j]:
				seq[j+1][i+1]=max(seq[j][i]+1, seq[j][i+1], seq[j+1][i])
			else:
				seq[j+1][i+1]=max(seq[j][i], seq[j][i+1], seq[j+1][i])
				
	return seq[l2][l1]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
