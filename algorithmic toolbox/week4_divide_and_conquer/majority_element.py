# Uses python3
import sys

def get_majority_element(a, left, right):
	if left == right:
		return -1
	if left + 1 == right:
		return a[left]
	#write your code here
	ave=(left+right)//2
	fh=get_majority_element(a, left, ave)
	sh=get_majority_element(a, ave, right)
	if fh==sh:
		return fh
	else:
		cnt2=cnt1=0
		for i in range(left, right):
			if a[i]==fh:
				cnt1+=1
			elif a[i]==sh:
				cnt2+=1
		if(cnt1>(right-left)/2):
			return fh
		elif(cnt2>(right-left)/2):
			return sh
	return -1

if __name__ == '__main__':
	input = sys.stdin.read()
	n, *a = list(map(int, input.split()))
	if get_majority_element(a, 0, n) != -1:
	   print(1)
	else:
	   print(0)
