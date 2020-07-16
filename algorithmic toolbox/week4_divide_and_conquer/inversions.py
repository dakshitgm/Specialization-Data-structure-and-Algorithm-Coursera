# Uses python3
import sys

def get_number_of_inversions(a, b, left, right):
	number_of_inversions = 0
	if right - left <= 1:
		return number_of_inversions
	ave = (left + right) // 2
	number_of_inversions += get_number_of_inversions(a, b, left, ave)
	number_of_inversions += get_number_of_inversions(a, b, ave, right)
	#write your code here
	f=left
	s=ave
	ind=left
	while f<ave and s<right:
		if a[f]<=a[s]:
			b[ind]=a[f]
			f+=1
			ind+=1
		else:
			b[ind]=a[s]
			number_of_inversions+=ave-f
			ind+=1
			s+=1
	while f<ave:
		b[ind]=a[f]
		#number_of_inversions+=1
		ind+=1
		f+=1
	while s<right:
		b[ind]=a[s]
		ind+=1
		s+=1
	a[left:right]=b[left:right]
	return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
