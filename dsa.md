<style>
    body{
         font-family:Ubuntu;
    }
</style>

# Data Structure & Algo

## Reverse Array/String

Tag: Array, String.</br>
_Time Complexity: O(n). Space Complexity: O(1)_

    for i in range(0, n/2):
        swap(arr[0], arr[n-i-1]);

## Find Max and min elemnts in an array

Tag: Array</br>
_Time Complexity: O(n). Space Complexity: O(1)_

    Max = -Infinity, Min = Infinity
    for i in arr:
        Max = max(Max, i)
        Min = min(Min, i)

## Find Kth Max Element

Tag: Array, Heap.</br>
_Time Complexity: O(n log k). Space Complexity: O(K)_

    minHeap(k) //heap with k capacity
    for i in range(0, k):
        minHeap.add(arr[i])
    heapify()
    for i in range(k, n):
        heap[0]=arr[i]
        heapify()

    return heap[0]

## Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo

Tag: Array</br>
_Time Complexity: O(n). Space Complexity: O(1)_

    Create two indexes(start=0, last=n) if start curElemnt from 0 if curElement is 0 swap with first if swap with last if 1 just iterate

## Move Negative Element to one side of Array.

Tag: Array</br>
_Time Complexity: O(n). Space Complexity: O(1)_

    create index. iterate through array and swap negative element with index

## Union & Intersection Sorted array

Tag: Array</br>
_Time Complexity: O(n). Space Complexity: O(1)_

    int i, j
    union<- arr1[i]<arr2[j]?arr[i++]:arr2[j];
    if(arr1[i]==arr2[j])
        union<- arr1[i];
        inter<- arr[i]; i++; j++;

## Program to cylicaly rotate array by one

Tag: Array</br>
_Time Complexity: O(n). Space Complexity: O(1)_

    temp = arr[0]
    for i in range(1, n):
        arr[i-1] = arr[i]

    arr[n-1]=temp

## Largest of Contiguous subArray

Tag: Array</br>
_Time Complexity: O(n). Space Complexity: O(1)_

    max = -Infinity, sum=0

    for i in arr:
        sum += i
        max = Max(max, sum)
    return max

## Minimize & Maximize Diff between Hights after adding or subtracting k

Tag: Array</br>
_Time Complexity: O(n). Space Complexity: O(1)_

    sort(arr)
    for i in arr:
        i += k


    big= arr[n-1], small = arr[0], diff = big - small,

    afterbig = big-2*k

    for i in reversed(arr):
        i -= 2*k
        if i< 0:
            afterBig = max(afterbig, i)
            big = max(big, afterbig)
            small = min(small, i)
            diff = min(diff, big-small)

    return diff

## Min no of Jumps reach end of Array
Tag: Array</br>
_Time Complexity: O(n). Space Complexity: O(1)_

    start = end = jump = 0

    while end < arr.length-1:
        jump++
        s=start, e=end
        for i s to <=e:
            end = max(end arr[i]+i)

           if end>=arr.length-1 return jump 
        if e= end return -1
        start = e+1

    return jump

## Find duplicate in N+1 size array where a[i]<N+1

ag: Array, Hash</br>
_Time Complexity: O(n). Space Complexity: O(N)_

    use hashtable whenever encounter count two return



