#Uses python3
import sys
import math
from collections import namedtuple
point=namedtuple('point', 'x y')

def minimum_distance(points):
    #write your code here
	n=len(points)
	if n==1:
		return float('inf')
	if n==2:
		return distance(points[0], points[1])
	mid=n//2
	d1=minimum_distance(points[0:mid])
	d2=minimum_distance(points[mid:n])
	d=min(d1, d2)
	sline=(points[mid].x+points[mid-1].x)/2
	low=sline-d
	high=sline+d
	st_points=[]
	for i in points:
		if low<=i.x<=high:
			st_points.append(i)
	st_points.sort(key=lambda point:point.y)
	diff=d
	size=len(st_points)
	for i in range(size):
		j=i+1
		while j<size and st_points[j].y-st_points[i].y<diff:
			diff=distance(st_points[i+1], st_points[i])
			j+=1
	
	return min(d, diff)
def distance(p1, p2):
	x_dif=abs(p1.x-p2.x)**2
	y_dif=abs(p1.y-p2.y)**2
	return (x_dif+y_dif)**0.5
	
if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int, input.split()))
	n = data[0]
	x = data[1::2]
	y = data[2::2]
	points=[point(x[i], y[i]) for i in range(n)]
	points.sort()
	print("{0:.9f}".format(minimum_distance(points)))
