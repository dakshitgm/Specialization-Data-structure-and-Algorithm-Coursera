ins=int(input())
pre=0
cur=1
sum=1
ins=ins%60
if(ins):
	for i in range(2, ins+1):
		pre, cur=cur, (pre+cur)%10
		sum=(sum+cur)%10
	print(sum)
else:
	print(0)
