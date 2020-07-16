#Uses python3

import sys

def largest_number(a):
    #write your code here
	for i in range(len(a)-1):
		for j in range(i+1, len(a)):
			if(len(a[i])==len(a[j])): 
				if(int(a[i])<int(a[j])):
					a[i], a[j]=a[j], a[i]
			elif((int(a[i][0])<int(a[j][0])) or (int(a[i][0])==int(a[j][0]) and int(a[i][-1])<int(a[j][-1]))):
				a[i], a[j]=a[j], a[i]
	res=''
	for no in a:
		res=res+no
	return res

if __name__ == '__main__':
	input = sys.stdin.read()
	data = input.split()
	a = data[1:]
	print(largest_number(a))
    
