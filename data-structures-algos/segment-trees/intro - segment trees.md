
***usecase*** - for minimizing time complexity for range queries in an array

-> It's tree - binary tree 
-> Tree Representation of an Array
-> size of Segment Tree = **4 x length(Array)**

populate the segmentTree:

										**[start, end, currentIndex]**
	[start, end // 2, (2*currentIndex + 1)]      [end // 2 + 1, end, (2*currentIndex + 2)]

```
nums = [2, 5, 4, 1, 7, 3]

segmentTree = [0] * (len(nums) * 4)
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

leftChild = 2 * i + 1 (i = currentIndex)
rightChild = 2 * i + 1

"""
repeat this until you get the smallest possible interval between (start - end), which 
will be when start == end.
"""
```

	populate the segmentTree:
											[start = 0, end = 6, currentIndex = 0]
																			[0, 6, 0]
									[0, 3, 1]                                      [4, 6, 2]
			[0, 1, 3]               [2, 3, 4]                     [4, 5, 5]       [6, 6, 6]
	[0, 0, 7]  [1, 1, 8]     [2, 2, 9] [3, 3, 10]       [4, 4, 11]    [5, 5, 12]

```
segmentTree[currentIndex] = sum(nums[start:end])

segmentTree = [30, 12, 18, 9, 5, 16, 2, 2, 5, 4, 1, 7, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

Ref: https://leetcode.com/problems/range-sum-query-mutable/

