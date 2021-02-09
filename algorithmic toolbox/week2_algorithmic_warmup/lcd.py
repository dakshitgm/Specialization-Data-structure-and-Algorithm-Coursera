def gcd(a,b):
	if(b==0):
		return a
	else:
		return(gcd(b, a%b))
a, b=[int(n) for n in input().split(' ')]
gcd=gcd(a,b)
print(int((a*b)/gcd))