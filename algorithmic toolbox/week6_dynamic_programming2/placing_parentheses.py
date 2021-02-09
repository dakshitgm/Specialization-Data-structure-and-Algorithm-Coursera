# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):
    #write your code here
	nos=dataset[0::2]
	exp=dataset[1::2]
	Min=[[float('inf') for _ in range(len(nos))] for _ in range(len(nos))]
	Max=[[-float('inf') for _ in range(len(nos))] for _ in range(len(nos))]
	for i in range(len(nos)):
		Min[i][i]=Max[i][i]=int(nos[i])
	for s in range(1, len(nos)):
		for i in range(0, len(nos)-s):
			j=i+s
			for k in range(i, j):
				o1=evalt(Max[i][k], Max[k+1][j], exp[k])
				o2=evalt(Max[i][k], Min[k+1][j], exp[k])
				o3=evalt(Min[i][k], Max[k+1][j], exp[k])
				o4=evalt(Min[i][k], Min[k+1][j], exp[k])
				Max[i][j], Min[i][j]=max(o1, o2, o3, o4, Max[i][j]), min(o1, o2, o3, o4, Min[i][j])
				
				
	return Max[0][len(nos)-1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
