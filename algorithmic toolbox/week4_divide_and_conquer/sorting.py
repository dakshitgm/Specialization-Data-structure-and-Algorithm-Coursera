# Uses python3
import sys
import random

def partition3(a, l, r):
	#write your code here
	x=a[l]
	j=l
	k=l
	for i in range(l+1, r+1):
		if a[i]==x:
			if k==j:
				j+=1
			k+=1
			a[i], a[k]=a[k], a[i]
		if a[i]<x:
			j+=1
			a[i], a[j]=a[j], a[i]
	jstart=j-k+l
	for i in range(0, k-l+1):
		a[l+i], a[j-i]=a[j-i], a[l+i]
	return [jstart, j]

def partition2(a, l, r):
	x = a[l]
	j = l
	for i in range(l + 1, r + 1):
		if a[i] <= x:
			j += 1
			a[i], a[j] = a[j], a[i]
	a[l], a[j] = a[j], a[l]
	return j


def randomized_quick_sort(a, l, r):
	if l >= r:
		return
	k = random.randint(l, r)
	a[l], a[k] = a[k], a[l]
	#use partition
	m = partition3(a, l, r)
	randomized_quick_sort(a, l, m[0] - 1);
	randomized_quick_sort(a, m[1] + 1, r);


if __name__ == '__main__':
	input = sys.stdin.read()
	n, *a = list(map(int, input.split()))
	randomized_quick_sort(a, 0, n - 1)
	for x in a:
		print(x, end=' ')
