**Two for loops** 

The first solution is to use two for loops.
You can traverse the array once, go through each of the numbers individually, and then add each number traverse the rest of the array and find the sum

**O(N^2) time| O(1) space**

```
def twoNumberSum(array, targetNum):
  for i in range(len(array)-1):
    firstNum = array[i]
    for j in range(i+1, len(array)):
      secondNum = array[j]
      if firstNum + secondNum == targetNum:
        return [i, j]
    return []
```

**Hashtable**

The second solution is to a Hashtable.
As we can see, the first solution is not very optimal from the time point of view. So perhaps the better way to solve this here is to use a hashtable.
This gonna cost extra space, but it might make the algorithm faster.

So what do I mean by using a hashtable.

Basically, you know the target num, as you traverse the array, you can get the current number. So the potential Number is target Number minus current number.And if the potential number is not in the hashtable, you can store the number and its index in the hashtable. If the potential number is in the hashtable, you can return its index and the index of current num.

**O(N) time| O(N) space**

```
def twoNumberSum(array, targetNum):
  nums={}
  for i in len(array):
    potentialNum = targetNum - array[i]
    if potentialNum in nums:
      return [nums[potentialNum], i]
    else:
      nums[array[i]]=i
  return []
```

**Two pointers**

The third way to solve this problem more optimal than the two for loops without using a Hashtable is to use two pointers. First we have to sort the array, which would take O(nlogN) time. And we don't use extra space.

Basically what we can do is. Once we sort the array, we put a left pointer under the first number of the array and right pointer under the very last of the array.
Then we sum up these two nums and compared with the target num. 

**O(nlogN) time| O(1) space**

```
def twoNumberSum(array, targetNum):
  array.sort()
  left=0
  right=len(array)-1
  while left < right:
    if array[left]+array[right]==targetNum:
      return [left, right]
    elif array[left]+array[right]>targetNum:
      right-=1
    else:
      left+=1
  return []
```    
