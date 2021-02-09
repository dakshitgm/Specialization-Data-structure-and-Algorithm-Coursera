# python3
import sys


def find_pattern(pattern, text):
  """
  Find all the occurrences of the pattern in the text
  and return a list of all positions in the text
  where the pattern starts in the text.
  """
  result = []
  # Implement this function yourself
  conc=pattern+'$'+text
  values=[0]*len(conc)
  last=0
  for i in range(1, len(conc)):
  	while last>=0:
  	  if conc[i]==conc[last]:
  	  	last+=1
  	  	values[i]=last
  	  	break
  	  else:
  	  	if last!=0:
  	  	  last=values[last-1]
  	  	else:
  	  		break
 
  pl=len(pattern)
  for i in range(pl, len(conc)):
  	if values[i]==pl:
  		result.append(i-pl-pl)
  return result


if __name__ == '__main__':
  pattern = sys.stdin.readline().strip()
  text = sys.stdin.readline().strip()
  result = find_pattern(pattern, text)
  print(" ".join(map(str, result)))

