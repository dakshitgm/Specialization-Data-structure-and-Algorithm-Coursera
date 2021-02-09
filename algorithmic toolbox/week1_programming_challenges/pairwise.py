no_input=int(input())
ins=input()
ins=ins.split(' ')
max1=0
max2=0
for no in ins:
	no=int(no)
	if(no>max1):
		max1=no
	elif(no>max2):
		max2=no
	if(max1>max2):
		tmp=max2
		max2=max1
		max1=tmp

print(max1*max2)
