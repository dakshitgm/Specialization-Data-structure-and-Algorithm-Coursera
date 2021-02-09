# Uses python3
import sys

def get_change(m):
	no_coin=0
	coins=[10, 5, 1]
	for coin in coins:
		while(m>=coin):
			m=m-coin
			no_coin=no_coin+1
	return no_coin


m = int(input())
print(get_change(m))
