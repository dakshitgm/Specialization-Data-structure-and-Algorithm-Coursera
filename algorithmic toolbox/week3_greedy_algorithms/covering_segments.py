
# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
	points = []
	toremove=[]
	while(len(segments)):
		match=segments[0]
		segments.remove(segments[0])
		for seg in segments:
			nwmatch=getmatch(seg, match)
			if(len(nwmatch)):
				match=nwmatch
				toremove.append(seg)
		points.append(match.start)
		while(len(toremove)):
			segments.remove(toremove[0])
			toremove.remove(toremove[0])
		
	return points
	
def getmatch(seg1, seg2):
	a=max(seg1.start, seg2.start)
	b=min(seg1.end, seg2.end)
	if(a>b):
		return []
	return Segment(a, b)

if __name__ == '__main__':
	input = sys.stdin.read()
	n, *data = map(int, input.split())
	segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
	points = optimal_points(segments)
	print(len(points))
	print(*points)
