ins, mod=[int(n) for n in input().split(' ')] 
fib=[0, 1]
repeat=ins+1
for i in range(2, ins+1):
	fib_no=(fib[i-1]+fib[i-2])%mod
	if(fib_no==1 and fib[i-1]==0):
		repeat=i-1
		break;
	fib.append(fib_no)
print(fib[ins%repeat])