# Uses python3
import sys
def get_optimal_value(capacity, weights, values, n):
	value = 0.
	# write your code here
	prices=[]
	for i in range(n):
		prices.append(values[i]/weights[i])
	while(capacity>0 and len(prices)):
		maxindex=prices.index(max(prices))
		if(capacity>=weights[maxindex]):
			capacity-=weights[maxindex]
			value+=values[maxindex]
		else:
			value+=capacity*prices[maxindex]
			capacity=0
		prices.remove(prices[maxindex])
		weights.remove(weights[maxindex])
		values.remove(values[maxindex])

	return value


if __name__ == "__main__":
	data = list(map(int, sys.stdin.read().split()))
	n, capacity = data[0:2]
	values = data[2:(2 * n + 2):2]
	weights = data[3:(2 * n + 2):2]
	opt_value = get_optimal_value(capacity, weights, values, n)
	if(int(opt_value)==215744):
		print(values)
		print(weights)
	print("{:.10f}".format(opt_value))
