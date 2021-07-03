# Merge Sorted Array

# Approach - 1 - O(xlog(x)) where x = n+m
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
n = len(nums2)
nums1 = nums1[:-n] + nums2
nums1.sort()
print(nums1)

# Approach - 2 Use Merge Sort - O(n+m) 