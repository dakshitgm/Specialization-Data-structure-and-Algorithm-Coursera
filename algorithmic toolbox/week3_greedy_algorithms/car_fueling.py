# python3
import sys


def compute_min_refills(distance, tank, stops, l):
    # write your code here
	refils=0
	cur=-1
	last=cur
	cov=0
	while((distance-cov)>tank):
		while(cur<(l-1) and tank>=(stops[cur+1]-cov)):
			cur=cur+1
		if(last==cur):
			return -1
		cov=stops[cur]
		last=cur
		refils=refils+1
		
	return refils

if __name__ == '__main__':
	d, m, l, *stops = map(int, sys.stdin.read().split())
	print(compute_min_refills(d, m, stops, l))
