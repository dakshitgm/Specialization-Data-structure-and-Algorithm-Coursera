#Uses python3

import sys

def lcs3(a, b, c):
    #write your code here
	l1=len(a)
	l2=len(b)
	l3=len(c)
	seq=[[[0 for _ in range(l1+1)] for _ in range(l2+1)] for _ in range(l3+1)]
	for i in range(l1):
		for j in range(l2):
			for k in range(l3):
				if a[i]==b[j]==c[k]:
					seq[k+1][j+1][i+1]=max(seq[k][j][i]+1, seq[k][j][i+1], seq[k][j+1][i], seq[k][j+1][i+1], seq[k+1][j][i], seq[k+1][j][i+1], seq[k+1][j+1][i])
				else:
					seq[k+1][j+1][i+1]=max(seq[k][j][i], seq[k][j][i+1], seq[k][j+1][i], seq[k][j+1][i+1], seq[k+1][j][i], seq[k+1][j][i+1], seq[k+1][j+1][i])
	return seq[l3][l2][l1]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
