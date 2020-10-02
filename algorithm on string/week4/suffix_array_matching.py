# python3
import sys

def find_occurrences(text, patterns):
    occs = set()
    #write your code here
    text=text+'$'
    surfix_array=build_suffix_array(text)
    for pattern in patterns:
        s, e=find_of(text, pattern, surfix_array)
        if not (s>e):
            for i in range(s, e):
                occs.add(surfix_array[i])
    return occs

def find_of(text, pattern, surfix_array):
    l=0
    r=len(text)
    plen=len(pattern)
    while l<r:
        mid=(l+r)//2
        midend=surfix_array[mid]+plen
        if pattern>text[surfix_array[mid]:midend]:
            l=mid+1
        else:
            r=mid
    start=l
    r=len(text)
    while l<r:
        mid=(l+r)//2
        midend=surfix_array[mid]+plen
        if pattern<text[surfix_array[mid]:midend]:
            r=mid
        else:
            l=mid+1
    end=r
    return (start, end)     

def build_suffix_array(text):
  order = []
  # Implement this function yourself
  order=sortchar(text)
  clases=computeClass(text, order)
  l=1
  while l<=len(text):
    order=sortDoubled(text, l, order, clases)
    clases=updateClass(l, order, clases)
    l=2*l
  return order

def sortchar(text):
  ar=[[text[i], i] for i in range(len(text))]
  ar.sort()
  result=[ar[i][1] for i in range(len(text))]
  return result

def computeClass(text, order):
  class_ar=[0]*len(text)
  for i in range(1, len(order)):
    if text[order[i]]!=text[order[i-1]]:
      class_ar[order[i]]=class_ar[order[i-1]]+1
    else:
      class_ar[order[i]]=class_ar[order[i-1]]
  return class_ar

def sortDoubled(text, l, order, clases):
  count=[0]*len(text)
  newOrder=[0]*len(text)
  for i in range(len(text)):
    count[clases[i]]+=1
  for i in range(1, len(text)):
    count[i]=count[i]+count[i-1]
  for i in reversed(range(len(text))):
    prev=(order[i]-l+len(text))%len(text)
    cl=clases[prev]
    count[cl]-=1
    newOrder[count[cl]]=prev
  return newOrder

def updateClass(l, order, clases):
  n=len(order)
  newClass=[0]*n
  for i in range(1, n):
    cur, prev=order[i], order[i-1]
    mid, prevmid=(cur+l)%n, (prev+l)%n
    if clases[cur]!=clases[prev] or clases[mid]!=clases[prevmid]:
      newClass[cur]=newClass[prev]+1
    else:
      newClass[cur]=newClass[prev]
  return newClass

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    pattern_count = int(sys.stdin.readline().strip())
    patterns = sys.stdin.readline().strip().split()
    occs = find_occurrences(text, patterns)
    print(" ".join(map(str, occs)))