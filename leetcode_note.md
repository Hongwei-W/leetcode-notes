# Array



## Binary Search 



General idea:

#### [E 704. Binary Search](https://leetcode.com/problems/binary-search/)

2 ways: 1) [left, right], 2) [left, right)

### Sol. 1 [left, right]



```python
 def search(self, nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
		if nums[mid] == target:
        	return mid
      
      	if nums[mid] < target:
        	left = mid + 1
      	else:
        	right = mid - 1
    
    return -1
```



### Sol. 2 [left, right) mostly used



```python
def search(self, nums: List[int], target: int) -> int:
	left,right = 0, len(nums)
  
 	while left < right:
    	mid = (left + right) // 2
    	if nums[mid] == target:
        	return mid
      
    	if nums[mid] < target:
        	left = mid + 1
    	else:
        	right = mid
    
   return -1
```

or

```python
def search(self, nums: List[int], target: int) -> int:
	left,right = 0, len(nums)
  
    while left <= right:
    	mid = (left + right) // 2
    	if nums[mid] == target:
        	return mid
      
    	if nums[mid] < target:
        	left = mid + 1
    	else:
        	right = mid - 1
    
   	return -1
```



#### [E 35. Search Insert Position](https://leetcode.com/problems/search-insert-position/)



#### [M 34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

Use two modified binary search to search for two bounds



#### [E 69. Sqrt(x)](https://leetcode.com/problems/sqrtx/)

Store sub-solution and use it later (the "left" calculate last time maybe the answer)



####  [E 367. Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/)





## Two Pointers



Use two pointers, one slow pointer and one fast pointer. 



### Ptrs' Value Compared/Exchanged



#### [E 27. Remove Element](https://leetcode.com/problems/remove-element/)

Use two pointers, one slow pointer and one fast pointer. Fast pointer increment everytime while slow pointer stops everytime it encounters a target value and continues immediately after the value exchanged with the fast pointer. 

To do that, we let the value in fast pointer exchange with the value in slow pointer in **all iteration as long as the value in fast pointer is not the target value**, only after the exchange takes place, there is an increment of slow pointer. And this is the **only** condition in the iteration.

```python
def removeElement(self, nums: List[int], val: int) -> int:
  slow = 0
  for fast in range (0, len(nums)):
    if nums[fast] != val:
      nums[slow] = nums[fast]
      slow += 1
      return slow
```



#### [E 26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

**Enlightenment**: fast pointer could start from the second place in the array, if you don't need it in the fast place 



#### [E 283. Move Zeroes](https://leetcode.com/problems/move-zeroes/)

The same process as remove element (question 27), but fill the rest of the array with `0`

Can also use "right" and "left" pointers that loop the array in just one iteration, but the question ask to keep the origianl order, this approach cannot be used 



#### [E 844. Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/)

**Enlightenment**:  Pay sepcial attention to the "and" "or" usage. "and" could ignore some of the edge cases

One pointer for each string



#### [E 977. Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)

Two pointers from each side of the array

**Enlightenment**: the crossing of two pointers needs to be througthly considered



### Sliding Window (Fast & Slow Pointers)

 Find a right time to update slow pointer's postion while iterate the array with fast pointer



#### [M 209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)

**Enlightenment**: right introduces the new elements into the sub-array, left controls the deletion of the sub-array 



#### [M 904. Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/)



#### [H 76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)

**Enlightenment**: there are just a lot of to consider: when to update the slow pointer? When to count if the current answer is valid?



### Left and Right Pointers



#### [M 15. 3Sum](https://leetcode.com/problems/3sum/)

**Enlightenment**: Should not use hash map, there are too many edge case to consider

**Enlightenment**: one iterator, one left pointer, one right pointer. Iterator iterate thought the list, left increment while the result is less than 0, right decrement while result is greater than 0



#### [M 18. 4Sum](https://leetcode.com/problems/4sum/)

**Enlightenment**: one more layer of iterator. So, two layer of for loop but still two pointers as sliding window





## 2*2 Matrix



Python list comprehension: ` [<element> for _ in range(lower, upper)]`



#### [M 59. Spiral Matrix II](https://leetcode.com/problems/spiral-matrix-ii/)

**Enlightenment**: find the pattern. There might be two outcome depends on the odd/even number given 



#### [M 54. Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)

**Enlightenment**: don't change the general rule, considering it as the special case first 

In #59, the only special case is when the matrix width is an odd number, so the center is the special case. While here, the special case is when there is only `1*col` or  `row*1` left to be calculated, due to that it cannot be treated as a ring as before. 



# Sort



## Sorting Algorithm



Bubble Sort $\textrm{O}(n^2)$

```python
def bubbleSort(data):
    for last in range(len(data)-1, 0, -1):
        for current in range(last):
            if (data[current] > data[current+1]):
                data[current], data[current+1] = data[current+1], data[current]
```



Selection Sort $\textrm{O}(n^2)$

From left to right, in each iteration, select the smallest value and swap into the first place

```python
def selectionSort(data):
    for index in range(len(data)):
        smallIndex = index
        for i in range(index, len(data)):
            if (data[i] < data[smallIndex]):
                smallIndex = i
        data[index], data[smallIndex] = data[smallIndex], data[index]
```



Insertion Sort $\textrm{O}(n^2)$

The lower part of the collection is sorted, while the higher part is unsorted. In each iteration, take the last value in each iteration and go to the lower part, find a place to insert the value. 

```python
def insertionSort(data):
    for index in range(len(data)):
        temp = data[index]
        position = index
        while position > 0 and data[position-1] > temp:
            data[position] = data[position-1]
            data -= 1
        data[position] = temp
```



Merge Sort $\textrm{O}(n logn)$ *spcae*: $2n$
First separate the data as half, as the half's half, and so on till there is only one value left. And recompose the value from the bottom to top. By comparing elements in two lists and composing into one list. 

```python
def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j +=1 1
  	result += left[i:]
    result += right[j:]
    return result

def mergeSort(data):
    if len(data) <= 1:
        return data
   	
    middle = len(data) // 2
    
    left = mergeSort(data[:middle])
    right = mergeSort(data[middle:])
    
    return merge(left, right)
```



Quick Sort $\textrm{O}(nlogn)$

First separate data by a pivot into half, then separate those two data by their pivot into half's half. Then till there are only one value left in each list. At this time, the data has been sorted. 

```python
def quickSort(data):
    quickSort_helper(data, 0, len(data)-1)

def quickSort_helper(data, first, last):
    if first < last:
        pivot = partition(data, first, last)
        quickSort_helper(data, first, pivot-1)
        quickSort_helper(data, pivot+1, last)
        
def partition(data, first, last):
    pivot = data[first]
    left = first+1
    right = last
    done = False
    
    while not done:
        while left <= right and data[left] <= pivot:
            left += 1
        while left <= right and data[right] >= pivot:
            right -= 1
        if left > right:
            done = True
       	else:
            data[left], data[right] = data[right], data[left]
    data[first], data[right] = data[right], data[first]
    
    return right
```



Heap Sort $\textrm{O}(nlogn)$

```python
def heapify(arr, n, i): # O(lg n)
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[i] < arr[r]:
        largest = r
   	if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    
    # build a max heap O(n)
    for i in range(n//2, -1, -1):
        # heapify one element 
        heapify(arry, n, i)
    
    for i in range(n-1, 0, -1): # O(nlgn)
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
```



# Fibonacci Numbers



```python
def Fib(n):
    if n == 0:
        return 0
    elif n ==1 and n ==2:
        return 1
    else:
        return Fib(n-1) + Fib(n-2)
```





# Linked List



## Linked List General 



#### [E 707. Design Linked List](https://leetcode.com/problems/design-linked-list/)



The use of:

- Dummy head, to generalize the head's speciality 
- Two pointers, fast and slow. Can be:
  - Fast pointer go a certain amount of step first, then start the iteration with slow pointer 
  - Fast pointer followed by slow pointer, dealing with adjacent nodes 



## Dummy Head



#### [E 203. Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/)

**Enlightenment**: the only special case is the removal of the first element. To generalize this special case, we add a `dummy_head` before the acutal head. When we return the head, we return `dummy_head.next`. When find that `cur.next.val` is the target, we only update the `cur.next` but don't incrment the `cur`. By not incrementing `	cur`, we re-evaluate the updated `cur.next.val`.



#### [M 24. Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)

**Enlightenment**: dummy head generalize the spcial behaviour of head. This question is just a simple swap between three nodes, then move **two** nodes forward (instead of one node). Note, when moving two modes forward, pay attention to how you use the variable. 



## Two Pointers



#### [E 206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

**Enlightenment**: use two pointers. Increment the fast pointer to the tail and in each step change the direction of the `next`. Return the slow pointer in the end. 



#### [M 142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)

Try tackle the question by reading this explanation and **draw** a diagram by yourself

We use two set of fast and slow pointers. The first set is used to located if there is a cycle in the linked list, the second set is used to located the start of the cycle. The first set, the fast pointer run two times faster than the slow pointer. If they ever meet, there is a cycle. If we supposed that the length of linked list before the cycle start is x, the length that after the start and before (and including) the slow pointer stop is y, and the length left in the cycle is z. We could deduce that the slow pointer walked (x+y) while fast pointer walked (x+n(y+z)+y). We want to see where is the cycle start, so we want to calculate the x. And 2 times of the slow pointer walked is the same length as the fast pointer, so we could deduce that x = (n-1)*(y+z)+z. That is, the length of the linked list start to the cycle start, is equal to the remaining length of the cycle that the slow pointer has. We just need to start the second set of the pointer, that let one pointer start from the slow pointer, and the other start from the start of the linked list. When they meet, we find the start of the cycle. 

https://programmercarl.com/0142.%E7%8E%AF%E5%BD%A2%E9%93%BE%E8%A1%A8II.html#%E6%80%9D%E8%B7%AF



## Dummy Head + Two Pointers



#### [M 19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

Dummy head + two pointers. 

**Enlightenment**: fast pointer go a few step first, then start the iteration with slow pointer till fast pointer reach the end





# Hash Map



## Hash Map General 



#### [E 350. Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/)

Solution 1: use hash map

Solution 2: use sorting & two pointers. First sort the two arrays, then use two pointers point to their heads. If the numbers pointer points to are equal, both increment and add the number to the answer, if not equal, the small number pointer increment



### Update Hash Map While Iterating List



#### [E 1. Two Sum](https://leetcode.com/problems/two-sum/)



#### [M 454. 4Sum II](https://leetcode.com/problems/4sum-ii/)

**Enlightenment**: treate it the same as the *E 1.Two Sum*, except that this time is adding the additon result of two list into the hash map, instead of the element in one list.



### Home Made Key



#### [M 49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)

Two method: 1) reorder the character in the string, so that the string with same characters will be the same reordered string; 2) create a key that using the characters a string has, so that the string with same characters will have the same key

**Enlightenment:** A `defaultdict`'s value could be list. This means that I could append values to a `mp = defaultdict(list)` value. And when I want all values of the `mp` as a list, I could just call `list(mp.values())`

**Enlightenment**: A `defaultdict`'s can not be list, but could be a `tuple`. So, to store a list as a key, we could use `tuple(list_item)`.



#### [E 202. Happy Number](https://leetcode.com/problems/happy-number/)

**Enlightenment**: from question description: "loops endlessly in a cycle", we could find that: there will be a loop that "loop the same thing". So, a hash map is introduce



## List (As a Hash Map)

It is better to use a list instead of a hash map sometimes becasue when the list is short, it is faster than the hash map due to how the hash map was perform fundamentally 



#### [E 242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)

**Enlightenment**: It is better to use a list instead of a hash map because of the small size of the hash map key 

**Enlightenment**: `defaultdict` in python used by `from collections import defaultdict`. `defaultdict` provide default value for `int`, `set`, `str`, and `list` as `0`, `set()`, `''`, `[]`. More explanation by https://www.jianshu.com/p/bbd258f99fd3



#### [E 383. Ransom Note](https://leetcode.com/problems/ransom-note/)



## Set (Each Element Appears Once)



#### [E 349. Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/)

**Enlightenment**: use **set** (each element can only appear once)



## Sliding (Fixed Length) Window 



#### [438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)

This time, python built in sorted string won't work. Re-build a dictionary in every iteration is way too complicated, so we use a sliding windowm to add/delete counts from dictionary everytime we move forward in each iteration. 



# String



## Reverse String



#### [E 344. Reverse String](https://leetcode.com/problems/reverse-string/)

**Enlightenment**: create space for the "need to fill" things by the end of the string first, then fill them up from the back to the front. 



#### [E 541. Reverse String II](https://leetcode.com/problems/reverse-string-ii/)

**Enlightenment**: write general solution! It seems like there are a lot of edge cases in the question but there are actually not. Note how `step` in python for loop iterating the list by adding not-1-step. 



#### [M 151. Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/)



#### [E 剑指 Offer 58 - II. 左旋转字符串](https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/)

**Enlightenment**: reverse parts of string first, then reverse the whole string to reach the required result 

**Notice**: python reversed() and .reverse() returns an iterator, not a sequence. So, use `lst = list(reversed(lst))` or `lst = list(lst.reverse()` to make it back to list. 



## Replace String Element



#### [E 剑指 Offer 05. 替换空格](https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/)

**Enlightenment**: enlarge the string space first, then use two pointers to move the place of element from the left's place to the right 



# KPM Algorithm



#### [28. Implement strStr()](https://leetcode.com/problems/implement-strstr/)



```python
def strStr(self, haystack: str, needle: str) -> int:
    # implement KMP algorithm 

	def get_next_table():
      # initialize the next table
      next_table = [0] * len(needle)
      j = 0

      for i in range(1, len(needle)):
        # if not match
        while j > 0 and needle[i] != needle[j]:
          j = next_table[j-1]
          # if match
        if needle[i] == needle[j]:
          j += 1
          # update the current next table value
        next_table[i] = j
       return next_table

	if len(needle) == 0:
    return 0

  next_table = get_next_table()
  needle_pos = 0

  for haystack_pos in range(len(haystack)):
    # when not match
    while needle_pos > 0 and haystack[haystack_pos] != needle[needle_pos]:
      needle_pos = next_table[needle_pos-1]
		# when match
	if haystack[haystack_pos] == needle[needle_pos]:
	  needle_pos += 1
      #haystack_pos += 1 is the for loop 

    # return condition
    if needle_pos == len(needle):
      return haystack_pos - needle_pos + 1

  return -1
```



#### [E 459. Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/)

**Enlightenment**: observe the next_table's value and the length of the string, discover the relationship between them.

The next_table means the max length of the prefix and postfix sub-strings. So, at the last character, the max length is the max length of the sub-string, the first n-1 duplicates and the last n-1 duplicates.



# Stack and Queue



## Stack and Queue General



Stack: LIFO

Queue: FIFO



#### [E 232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)

**Enlightenment**: use python `collections.deque` to implement stack 



#### [E 225. Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/)

**Improvement**: use only one queue to implement a stack, by dequeuing then enqueuing all the element EXCEPT the last element agian to the same queue



#### [E 20.Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)



#### [E 1047. Remove All Adjacent Duplicates In String](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/)



#### [M 150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)



## Queue, But Not That Queue



### Monotonically Increasing/Decreasing Queue



#### [H 239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)

**Enlightenment**: use doubely opened, monotonically decreasing queue

`enqueue(val)` only when the `val` is smaller than the last element of the queue. So, pop the last element until the queue is empty or the last element is greater than `val`

`dequeue(val)` can only happen when the `val` is at the front of the queue, if not at front, it means that the element has already been discard

`front()` returns the first element of the queue, which is the greatest value in the window



### Heap/Priority Queue



#### [M 347. Top K Frequent Elements](https://leetcode-cn.com/problems/top-k-frequent-elements/submissions/)

**Enlightenment**: use min heap, `heapq` that python provides. 

First iterate through the list and create a dictionary. Then create a heap and `heappush` item one by one. If the number of item in heap is greater than the requested amount, `heappop` the last element. 



# Binary Tree



## Tree Basics



```
				  10					height = 4, depth = 0
                /    \
             55      25					height = 3, depth = 1
            / \      / \
           21  17   13  90				height = 2, depth = 2
              / \ 
             15  99 					height = 1, depth = 3
            / \
           11  88						height = 0, depth = 4
```



### Terms

**Node** and **edge** (the connection of two nodes).

**Path**: a path from one node to another is the sequence of edges and nodes connecting them.

**Length of a path**: is the number of edges in it.

**Depth of a node**: is the length of the path from one root to a node, depth of root is 0. *For example, the depeth of node 17 is the length of the path from node 10 to node 17 which is 2*.

**Height of a node**: is the length of a path from one node to the heighest leaf. *For example, the height of 55 is 3*.

**Height of a tree**: is the height of the root. *For example, here, the height of the tree is the height of the root 10, which is 4*.

**Degree of a node**: is the number of children it has. *For example, the degree of node 55 is 2*.

**Degree of a tree**: is the maximum degree of any node in the tree, in binary tree, the degree of a tree is always 2.

*Less common ones:*

The **ancestors** of node 21 are nodes 55 and 10.

The **descendants** of node 55 are 21, 17, 15, 99, 11, 18



### Binary Tree Terms

<u>A **full** binary tree of height h</u> has leaves only on level h and each of its interior nodes is full

<u>A **complete** binary tree of height h</u> is a full binary tree of height h with 0 or more of the rightmost leaves of level h removed

*Examples*:

				complete                 
				  10
	            /    \
	         55      25
	        /
	       21 
	       
	       		complete                 
				  10
	            /    \
	         55      25
	        / \    
	       21  17


​	       
​		        not	complete                 
​				 10
​		       /    \
​	         55      25
​	      		    / \
​	   			  13  90

<u>A **AVL** tree</u> is a binary search tree where for any node we have $\abs{h_s - h_r} \leq 1$ 

*Examples:*

	   			 AVL                 
			  10
	        /    \
	     55      25
	    /
	   21  
	   
	   			not AVL                 
			 10
	        /  
	     55     
	    / 
	   21 



### Store Binary Tree

1) Linked list

*Eample:*

```python
class TreeNode:
  def __init(self, value):
    self.value = value
    self.left = None
    self.right = None
```

2. Array

*Example*:

```
			 10
            /    \
         55      25
        / \     /  \
       21  17  7   8

array = [10, 55, 25, 21, 17, 7, 8]
```



### Traverse a BST

1. BFS 广度优先 -- **queue**
   1. Level-order *example: 10 55 25 21 17 7 8*
2. DFS 深度优先 -- **stack** (recursion)
   1. Pre-order *example: 10 55 21 17 25 7 8*
   2. In-order *example: 21 55 17 10 7 25 8*
   3. Post-order *example: 21 17 55 7 8 25 10*

​		**Note: these orders are for the mid-node*



## Pre/In/Post Order Traversal



#### [E 144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)



#### [E 145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)



#### [E 94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)



### With Recursion



```python
def preorderTraversal(root):
  result = []
  
  def traversal(root):
    if root == None:
      return
    result.append(root.val) #mid-node, if put it first: preorder, in the middle: inorder, by the end: postorder
    traversal(root.left)
    traversal(root.right)
    
  traversal(root)
  return result
```



### With Stack



**Preorder**: Push the root first. Use `while` to gradually pop node, **push right child then left child**. So, left child will come out from the stack first.

```
If PREORDER
			  10
            /    \
          55      25
      	  / \     /  \
      	 21  17  7    8
      	 
		 -----------------------
stack:    10                    |
       	 -----------------------
   
		 -----------------------
stack:    55 25                 |  list: [10] note, push 25 first, then 55
       	 -----------------------
   
		 -----------------------
stack:    21 17 25              |  list: [10, 55]
       	 -----------------------
      
		-----------------------
stack:    17 25                 |  list: [10, 55] note, left/right child of 17 == None, so 			-----------------------			push nothing in
       	 

```



```python
def preorderTraversal(root):
  if root == None:
    return []
  
  stack = collections.deque()
  stack.appendleft(root)
  ans = []
  
  when len(stack):
    node = stack.popleft()
    ans.append(node.val)
    if node.right != None: # very improtant: to verify it is not None
      stack.appendleft(node.right) 
    if node.left != None:
      stack.appendleft(node.left)
  
  return ans
```



**Inorder**: user a pointer to go to the very left buttom, by looping giving the pointer to the left child. Add the current node, and give the pointer to the right child. If right is not None, then push it into stack, then give the pointer to the left child.

```python
def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
  if root == None:
    return []

  stack = collections.deque()
  cur = root
  ans = []

  while cur or len(stack):
    if cur: # goes to very buttom
      stack.appendleft(cur)
      cur = cur.left
    else: # pop, add value, then give the pointer cur.right
      cur = stack.popleft()
      ans.append(cur.val)
      cur = cur.right

  return ans
```



**Postorder**: the return list will go backwards, so `.appendleft()` or `reversed()`. So, the root will be at the end of the return list. If think in this reversed manner, then its right child would be the second last element. So this time, push the left child first, then right child. Because in this case, right child will come out first.

```python
def postorderTraversal(root):
  if root == None:
    return []
  
  stack = collections.deque()
  stack.appendleft(root)
  ans = collections.deque()
  
  when len(stack):
    node = stack.popleft()
    ans.appendleft(node.val)
    if node.left != None: # push LEFT first
      stack.appendleft(node.left)
    if node.right != None: 
      stack.appendleft(node.right) 

  return ans
```



### With Stack (Unified Method)



Preorder, inorder, postorder are **same code** except that sequnce of lines are change, just like recursion. 

To do this, we add a signal before the node we want to append to the answer list, that signal is a `None`. We check for the node is a None when we pop node from the stack, if yes, it indicates the next node is something we want to append to the answer list. 



Preorder

```python
def preorderTraversal(root):
  
  stack = collections.deque()
  if root:
    stack.appendleft(root)
  ans = []
  
  when len(stack):
    node = stack.popleft()
    if node:																  __
      if node.right: stack.appendleft(node.right) # right pop last 				|			
      if node.left: stack.appendleft(node.left) # left pop second				|
      stack.appendleft(node) # parent pop first									|
      stack.appendleft(None) # signal -> indicate add its value to ans		 ---
    else: # see the signal, append to the list
      node = stack.popleft() # discard the previous None, pop the parent 
      ans.append(node.val) 
  
  return ans
```



To write code for postorder and inorder, just change the sequence of those four lines



## Level Order Traversal 



### With Queue



```python
def levelOrder(root):
  queue = collections.deque()
  if root:
    queue.append(root)
   ans = []
  
  while queue:
    size = len(queue)
    res = []
    for _ in range(size):
      node = queue.popleft()
      res.append(node.val)
      if node.left:
        queue.append(node.left)
       if node.right:
        queue.append(node.right)
    ans.append(res)
  
  return ans
```



`for` loop iterate through the node in one level. If `for` loop ends, the `while` loop again becauser there are nodes in queue. And the nodes left is exactly the nodes in next level. 



#### [M 102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)



#### [M 107. Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)

Just simple reverse the order. 

**Note**: reverse a list in python, use `reversed(lst)` 



#### [M 199. Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/submissions/)

**Enlightenment**: use queue to levelorder traverse the binary tree, then pick the last element from each level. **But why bother?**

Because the right most element could be the left child (if there is no child in that level), or could alternate.

*Example:*

```
right most element is the left child:
		  3
		 /					rightMostElements = [3, 4]
		4

alternate:
		  3
		/  \
	   4    5				rightMostElements = [3, 5, 9]
	  /
	 9
```



#### [E 637. Average of Levels in Binary Tree](https://leetcode.com/problems/average-of-levels-in-binary-tree/)



#### [M 429. N-ary Tree Level Order Traversal](https://leetcode.com/problems/n-ary-tree-level-order-traversal/)

**Note**: this question is poorly designed



#### [M 515. Find Largest Value in Each Tree Row](https://leetcode.com/problems/find-largest-value-in-each-tree-row/)



#### [M 116. Populating Next Right Pointers in Each Node](https://leetcode.com/problems/populating-next-right-pointers-in-each-node)



#### [M 117. Populating Next Right Pointers in Each Node II](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii)



#### [E 104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)



#### [E 111. Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)



## Binary Tree Problems 



### Simple Traversal Problems



#### [E 226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)



#### [E 101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/submissions/)

**Enlightenment**: what is **symmetry**?

```
not symmetry
		  1
		/  \
	   2    2
    	\    \
    	 3    3
```



#### [E 100. Same Tree](https://leetcode.com/problems/same-tree/)



#### [M 513. Find Bottom Left Tree Value](https://leetcode.com/problems/find-bottom-left-tree-value/)

Other than levelorder traversal:

**Enlightenment:** use preorder traversal, keep two global variables: `max_depth` and `left_value`. Update those values when a node has no left and right child, and when the current depth value is greater than the `max_depth`



#### [E 257. Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/)

**Enlightenment:** when the recursion return bool, and when void? 1) When just traverse for on particular path, I can return a bool to indicate I have found the one. 2) When searching for the entire tree and need to deal with the return value, then a return value is needed. 3) When in all other situation, and just searching in the entire tree, no return value is needed.

In this example, I could have a return value, which return True by the time I found "the" path. I could also traverse the entire tree without a return value, but it would take slower. 

The ending conditon for the recursion would be different. And when calling recursion, notice that cannot call by `return recursion(root, cur)`, need to call by `if recursion(root, cur): return True`. This is to prevent returning too soon.



### Hard Traversal Problems 

#### [M 106. Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

**Enlightenment**: use postorder traversal to infer the parent, then use inorder traversal to infer the left and right nodes. 

**Enlightenment**: A function **can** return a TreeNode class instance 



#### [M 105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)



#### [M 654. Maximum Binary Tree](https://leetcode.com/problems/maximum-binary-tree/submissions/)



#### [E 617. Merge Two Binary Trees](https://leetcode.com/problems/merge-two-binary-trees/)



### Height and Depth



Pre/in/post Order Traversal:

Use recursion and unified stack (with iterations):

**Height** is calculated by **postorder** (because need to stack the number from leaf to root)

**Depth** is calculated by **preorder** (because need to stack the number from root to leaf)



Height: 

```python
recursion:
def getdepth(node):
    if (node == None): return 0
	reurn 1 + max(getdepth(node.left), getdepth(node.right))
```




Level Order Traversal (Use Queue):

**Height** **cannot** be calculated in this way, except I know which node to calculate for. *For example, if I want to calculate the height of the root, I could use level order traversal at root*

**Depth** **can** be calculated in this way



#### [E 110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)



### Back Propagation



#### [E 257. Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/)

**Enlightenment**: use preorder traversal, when finish one path, back propagate to the node where can go to the other way 

```
     98
   1d/
    23
  2d/3u \ 4d 
  45    55
in this example: 98->23->45->23->55, when 45 back propogate to 23, remove 45 from the list
```



#### [M 113. Path Sum II](https://leetcode.com/problems/path-sum-ii/)



#### [M 236. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)



### Child Is Parent-Once-More (Recursion)



#### [M 222. Count Complete Tree Nodes](https://leetcode.com/problems/count-complete-tree-nodes)

**Enlightenment**: normal traversal works, but in complete binary tree, I can iterate the tree to the full binary tree. If that is a full binary tree, then the number of nodes is $2^{depth}-1$. 



#### [E 572. Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/)

**Enlightenment**: There are only 3 possbilities, 1) the current root is the same tree as the subRoot, 2) the current root.left is the same tree as the subRoot, 3) the current root.right is the same tree as the subRoot. 

Then goes to the next recursion, such as the root.left is the same tree as the subRoot, the root.left.left is the same tree as the subRoot, the root.left.right is the same tree as the subRoot. 



#### [E 404. Sum of Left Leaves](https://leetcode.com/problems/sum-of-left-leaves/)

**Enlightenment**: I know that left leaf can only be: on the parent's left *and* has no left child *and* has no right child. This rule applies for parent, parent's left, parent's right , parent's left left, etc. 



## BST



### Term/Traverse BST

Valid BST: A **valid BST** is defined as follows:

- The **left subtree** of a node contains only nodes with keys **less than** the parent's key.
- The **right subtree** of a node contains only nodes with keys **greater than** the parent's key.
- Both the left and right subtrees must also be binary search trees.

**So, imagine an BST as a sequenced list**



#### [E 700. Search in a Binary Tree](https://leetcode.com/problems/search-in-a-binary-search-tree)

**Enlightenment**: try to use `while` loop to solve the problem



#### [M 98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)

**Enlightenment**: we can use **inorder** traversal to flatten the BST as a list, and see if it is in a sequence 

Or try to use inorder traversal to validate directly 



#### [E 235. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)



#### [M 538. Convert BST to Greater Tree](https://leetcode.com/problems/convert-bst-to-greater-tree/)



### Use `prev` Pointer to Traverse BST



#### [E 530. Minimum Absolute Difference in BST](https://leetcode.com/problems/minimum-absolute-difference-in-bst/)

**Enlightenment**: keep in mind that the BST is in order, so consider it flatten into a list. 

**Enlightenment**: keep a `prev` pointer to calculate the difference, but the `prev` should not be a parameter in the iteration. The recursion change the `prev` value during one iteration. 



#### [E 501. Find Mode in Binary Search Tree](https://leetcode.com/problems/find-mode-in-binary-search-tree/)



### Edit a BST



#### [M 701. Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/)



#### [M 450. Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/)

**Note**: recursion with `root.left = recusion_function(root)` has some backtrack properties, is equivenlent to having a `prev` variable to keep the last node

**Enlightenment**: when use `while` loop, how to deal with the <u>root</u> node and <u>non-root</u> node, these two situations? We could write a generic `deleteNode` function. When it is the <u>root</u> node, we call `return deleteNode()`. But when it is the <u>non-root</u> node, we call `prev.left= deleteNode` ([see here](https://programmercarl.com/0450.%E5%88%A0%E9%99%A4%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%AD%E7%9A%84%E8%8A%82%E7%82%B9.html#%E8%BF%AD%E4%BB%A3%E6%B3%95)).



#### [M 669. Trim a Binary Search Tree](https://leetcode.com/problems/trim-a-binary-search-tree/)



#### [E 108. Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)



# Back Tracking



## Back Tracking Overview

Back tracking is slow, is enumerating. There are a few problems can solve by back tracking. 

- 组合问题：N个数里面按一定规则找出k个数的集合
- 切割问题：一个字符串按一定规则有几种切割方式
- 子集问题：一个N个数的集合里有多少符合条件的子集
- 排列问题：N个数按一定规则全排列，有几种排列方式
- 棋盘问题：N皇后，解数独等等

组合(set) doesn't consider order, while 排列 does 



Back tracking is tree. All backtracking is searching for subset in a set. The set forms the tree's width, depth

Back tracking use recursion, it has such an pseudocode 

```
void backtracking(para) {
	if (ending-condition){
		store-result
		return 
	}
	
	for (range number-of-child/width){
		deal-with-the-node
		backtracking(para) // recursion
		backtranking-undo-result
	}
}
```

`for` recurse the width, `backtracking()` recurse the depth 

```
level1:								 set(size4)
						/			/			\				\
level2:			set(size3)		set(size2)		set(size1)		set(size0)
				/  |   \         /    \             |
level3:		leaf  leaf  leaf    leaf  leaf        leaf
```



### Combination



#### [77. Combinations](https://leetcode.com/problems/combinations/)

*Question: Given two integers `n` and `k`, return* *all possible combinations of* `k` *numbers out of the range* *`[1, n]`. e.g if n = 4 and k = 2 then output have [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]*

This problem use exactly the pseudocode mentioned above. The `for` loop represent the number that I can choose from in a particular positon (at position $1$, I have $\{1,2,3,4\}$ to choose from). 

The backtracking recursion calling represent I want dive deep into every position (in this quesiton, $k=2$, so I have $2$ positions).

Because this is combinations (not a permutation), so I need to keep a `starting_index` in each of recursion. So, in the next `for` loop of my next `recursion`, I know where to start. 

The solution can be refined by pruning. I can find that if I choose $4$ in the first position, then I can just prune the next recursion, because there won't be enough number of choice for me to compose the solution. This pruning is `n-(k-len(current_sol)+2)` in python

[See more detail](https://programmercarl.com/0077.%E7%BB%84%E5%90%88.html)



#### [M 216. Combination Sum III](https://leetcode.com/problems/combination-sum-iii/)



#### [M 17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)



#### [M 39. Combination Sum](https://leetcode.com/problems/combination-sum/)



#### [M 40. Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)

The trick of this question is that, there are repeat number in `candidates`. To avoid dulicates in the list, if the current value of candidates and the previous value of candiates are the same and we are on the same level of three, I should not use the same value. However, if it was on the same branch (instead of level), then I can use that. 

[See more detail](https://programmercarl.com/0040.%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8CII.html#python)



### Permutation



#### [M 46. Permutations](https://leetcode.com/problems/permutations/)



#### [M 47. Permutations II](https://leetcode.com/problems/permutations-ii/)

**Enlightenment:** because this question has duplicate elements in array, so need to consider more. 1) the number used last time in the same level cannot reuse, 2) every subset needs to have the same elements as the given array. 

To tackle these two problems, 1) sort the array and use `nums[i] != nums[i-1]`, 2) delete the used numbers dynamically (or maintain a `used` list)



### Partition String 



#### [M 131. Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/)



#### [M 93. Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses/)



### Subsets



#### [M 78. Subsets](https://leetcode.com/problems/subsets/)

**Enlightenment**: the subset/power subset requires all the intermeidate steps in the backtrack appends to the returning list. 

**Enlightenment**: to avoid duplicates, sort the given array



#### [M 90. Subsets II](https://leetcode.com/problems/subsets-ii/)



#### [M 491. Increasing Subsequences](https://leetcode.com/problems/increasing-subsequences/)

**Enlightenment**: because cannot sort the question's array, so maintain a `usage` set for every level. When use a number from the question's array, record it in the `usage` set. If in certian level, the number appears in the `usage` set, then it means the number has appeared previously and should not use again. 



### Create An Array, Use in BackTrack



#### [H 332. Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/)

**Enlightenment**: first create an array for backtrac, but in this question, a dictionary is better. This dictionary is similar to the "neighbor list" in 366. Then the startard backtrack could be used. 



#### [H 51. N-Queens](https://leetcode.com/problems/n-queens/)



### 2D BackTracking



#### [H 37. Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)

**Enlightenment**: return `False` to jump out of the inner layer to prevent traverse only on that layer. 





# Greedy 



### Simple Questions 



#### [E 455. Assign Cookies](https://leetcode.com/problems/assign-cookies/)

**Approach**: child who contents by small cookie consume the smallest but content cookie, or revesely, use the biggest cookie to satsified the child who needs the big cookie 

Sub-solution: child satisfied by the smallest but content cookie

Solution: all child satisifed by the smallest but content cookie



#### [M 376. Wiggle Subsequence](https://leetcode.com/problems/wiggle-subsequence/)

Sub-solution: if the previous is negative, the current is positive; vice-versa

Solution: the sign-ness is alternating 



#### [E 53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) 

Sub-solution: the previous `summation` must be positive, so the `summation + now` could be larger than before. If previous is not positive, empty the `summation` and start from now 

Solution: keep track of the `summation` and update the `max`

