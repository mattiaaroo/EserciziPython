'''
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    couple = []
    i = 0
    for n in nums:
        for a in nums[i+1:]:
            if n + a == target:
                couple.append(nums.index(n))
                couple.append(nums.index(a, 1))
                break
            else:
                pass
        i += 1
    return couple
 '''   
def findMedianSortedArrays(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums.sort()
        if len(nums) % 2 == 0:
            return int(nums[len(nums)%2])
        else:
            res1 = nums[len(nums) % 2]
            res2 = nums[len(nums) % 2 + 1]
            return (res1+res2)/2
        
nums1 = [1,2]
nums2 = [3,4]
print(findMedianSortedArrays(nums1, nums2))