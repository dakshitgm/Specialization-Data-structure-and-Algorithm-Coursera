
ins=int(input())
fib=[0, 1]
for i in range(2,ins+1):
	fib_no=fib[i-1]+fib[i-2]
	fib.append(fib_no)
print(fib[ins])
