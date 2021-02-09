# Uses python3
import sys

def fast_count_segments(starts, ends, points):
	cnt = [0] * len(points)
    #write your code here
	arr=[]
	for i in starts:
		arr.append((i, 's'))
	for i in points:
		arr.append((i, 'p'))
	for i in ends:
		arr.append((i, 'e'))
	arr=sorted(arr)
	no_of_seg=0
	for seg in arr:
		if seg[1]=='p':
			index_p=points.index(seg[0])
			while(cnt[index_p]!=0):
				index_p=points.index(seg[0], index_p+1, len(points))
			cnt[index_p]=no_of_seg
		elif seg[1] == 's':
			no_of_seg+=1
		else:
			no_of_seg-=1
	return cnt
def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
