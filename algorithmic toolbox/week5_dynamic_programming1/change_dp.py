# Uses python3
import sys

def get_change(m):
    #write your code here
	denoms=[1, 3, 4]
	j=0
	no_of_coin=[0]
	coin_used=[0]
	for i in range(1, m+1):
		if(j<2 and i==denoms[j+1]):
			no_of_coin.append(1)
			j+=1
			continue
		no_coin=no_of_coin[i-1]+1
		for k in range(1, j+1):
			no_coin=min(no_coin, no_of_coin[i-denoms[k]]+1)
		no_of_coin.append(no_coin)
	return no_of_coin[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
