ins=int(input())
def get_sqared_sum(ins):
	pre=0
	cur=1
	repeat=60
	sum=1
	ins=ins%repeat
	if(not ins):
		return 0
	for i in range(2, ins+1):
		pre, cur = cur, (pre+cur)%10
		sum=(sum+cur**2)%10
	return sum
print(get_sqared_sum(ins))
