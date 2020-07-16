fro, ins=map(int, input().split(' '))
def give_sum(fro, ins):
	pre=0
	cur=1
	sum=0
	ins=ins%60  
	fro=fro%60
	if(ins<fro):
		ins=ins+60
	if(ins):
		if(fro<2):
			sum=1
			fro=2
		for i in range(2, fro):
			pre, cur=cur, (pre+cur)%10
		for i in range(fro, ins+1):
			pre, cur=cur, (pre+cur)%10
			sum=(sum+cur)%10
		return sum
	else:
		return 0
print(give_sum(fro, ins))