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


l1: list = [3,4,2]
l2: list = [4,6,5]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def addTwoNumbers(self, l1, l2):
        num1 = 0
        num2 = 0
        place = 1

        current = l1
        while current:
            num1 += current.val * place
            place *= 10
            current = current.next

        place = 1

        current = l2
        while current:
            num2 += current.val * place
            place *= 10
            current = current.next

        total = num1 + num2

        dummy_head = ListNode(0)
        current = dummy_head

        if total == 0:
            return ListNode(0)

        while total:
            digit = total % 10
            total //= 10
            current.next = ListNode(digit)
            current = current.next

        return dummy_head.next


print(addTwoNumbers(l1, l2))


def findMedianSortedArrays(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums.sort()
        if len(nums) % 2 == 0:
            res1 = nums[int(len(nums) / 2)]
            res2 = nums[int(len(nums) / 2 - 1)]
            return (res1+res2)/2
            
        else:
            
            return nums[int(len(nums)/2)]
        

nums1: list = [1,2]
nums2: list = [3,4]

print(findMedianSortedArrays(nums1, nums2))


def myAtoi(s):
    """
    :type s: str
    :rtype: int
    """
    result = 0
    num_count = []
    for c in s:
        numbers = ["1","2","3","4","5","6","7","8","9","0"]
        if c in numbers:
            c = int(c)
            result += c
            num_count.append(c)
            pass

        else: 
            break
        
    som = 0
    num_count = reversed(num_count)
    for n in num_count:
        i = num_count.index(n)
        som += (n*(i*10))

    return som


print(myAtoi("42"))




def intToRoman(num):
    
    ops: dict = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I" : 1}
    res: str = ""
    while num != 0:
        check = 0
        for op in ops:
            if op * (num // ops[op]) != 0:
                if num != 4:
                    check += 1
                else:
                    res += "IV"
                if num != 9:
                    check += 1
                else:
                    res += "IX"
                if num != 90:
                    check += 1
                else:
                    res += "XC"
                if num != 400:
                    check += 1
                else:
                    res += "CD"
                if num != 40:
                    check += 1
                else:
                    res += "XL"
                if num != 900:
                    check += 1
                else:
                    res += "CM"
                    
                if check != 0:
                    res += (op * (num // ops[op]))

                num -= (ops[op] * (num // ops[op]))
            else: 
                check = 0
                pass
        counter = 0
        for n in res:
            for _ in res[n:]:

                if _ == n:
                    counter += 1
                else:
                    counter = 0
                    continue
        
            
    return res

print(intToRoman(3749))


def intToRoman(num):
    ops: dict = {1000:"M", 500: "D", 100: "C", 50: "L", 10: "X", 5: "V", 1: "I"}
    exs: dict = {4:"IV", 9:"IX", 40:"XL", 90:"XC", 400:"CD", 900:"CM"}
    res: list = []
    while num > 0:
        for op in ops:
            if num // op:
                num -= (num // op) * op 
                res.append((num // op) * ops[op])
            else:
                continue
        for ex in exs:
            if num == ex:
                num -= ex
                res.append((num // ex) * exs[ex])
            else: 
                continue
    return res

print(intToRoman(3749))



def intToRoman(num):
    M = ["","M", "MM", "MMM"]
    C = ["","C","CC", "CCC", "CD", "D", "DC", "DCC", "CCM", "CM"]
    X = ["","X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    I = ["","I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    res = ""
    res = M[num//1000] + C[(num % 1000)//100] + X[num % 100 // 10] + I[num % 10 // 1]
    return res


print(intToRoman(80))



def reverse(x: int) -> int:
    reversed_x = str(x)[::-1]
    reversed_x = int(x)
    if reversed_x < -2**31 or reversed_x > 2**31 - 1:
        return 0
    else:
        reversed_x = str(reversed_x)
        reversed_x = list(reversed_x)
        if reversed_x[-1] == "-":
            reversed_x.pop()
        while reversed_x[-1] == "0":
            reversed_x.pop()
        if "-" in reversed_x:
            reversed_x.remove("-")
        res = ''.join(reversed_x[::-1])
        if x < 0:
            return int(res) * -1
        else:
            return int(res)


    
        

print(reverse(-901000)

'''

# def fourSum(nums: list[int], target: int) -> list[list[int]]:
#     res: list[list[int]] = []
#     l: list[int] = []
#     res.append(l)
#     while len(l) < 4:
#         for i in range(len(nums)):
#             for j in range(len(nums[i+1:])):
#                 if target - nums[i] == nums[j]:
#                     l.append(nums[i])
#                     l.append(nums[j])
#                     pass
#                 else:
#                     pass
#     else:
#         fourSum(nums, target)

#     return res
    
#     a = target - n
#     if a in nums:
#         res.append(n)
#         res.append(a)
#         nums.remove(n)
#         nums.remove(a)

# print(fourSum(nums = [1,0,-1,0,-2,2], target = 0))


'''




def longestCommonPrefix(v: list[str]) -> str:
    ans=""
    v=sorted(v)
    first=v[0]
    last=v[-1]
    for i in range(min(len(first),len(last))):
        if(first[i]!=last[i]):
            return ans
        ans+=first[i]
    return ans 




print(longestCommonPrefix(["flower", "flow", "flight"]))



def lengthOfLongestSubstring(s: str) -> int:
    counter: int = 0
    subs: dict [int : list] = {}
    if s:
        for c in s:
            if counter not in subs.keys():
                    subs[counter] = []
            if c not in subs[counter]:
                subs[counter].append(c)
            else:
                if counter != 0:
                    if subs[counter-1][-1] == c:
                        subs[counter].pop(0)
                        subs[counter].append(c)
                        pass
                else:
                    counter += 1
                    subs[counter] = []
                    subs[counter].append(subs[counter-1][-1])
                    subs[counter].append(c)
                
                pass
    else: 
        return 0
    return max(len(set(list)) for list in subs.values())


print(lengthOfLongestSubstring("anviaj"))





def removeDuplicates(nums: list[int]) -> int:
        nums1: list[int] = []
        for i in range(len(nums)):
            if nums[i] not in nums1:
                  nums1.append(nums[i])
            
        return nums1

print(removeDuplicates([1, 2, 3, 3]))



def threeConsecutiveOdds(arr: list[int]) -> bool:
        streak: int = 0
        res: bool = False
        i : int = 0
        while i in range(len(arr)) and streak < 3:
            if arr[i] % 2 > 0:
                streak += 1
                i += 1
            else:
                streak = 0
                i += 1
        return streak == 3

lista: list[int] = [2,6,4,1, 7, 9]
print(threeConsecutiveOdds(lista))


''''



# def maxNumEdgesToRemove(n: int, edges: list[list[int]]) -> int:
#         touchedNodes: list = []
#         checkEdgesA : list[int] = []
#         checkEdgesB : list[int] = []

#         i: int = 0
#         for l in edges:
#             i: int = 0
#             # list of all touched nodes
#             while i <= 4:
#                 if i == 1:
#                     touchedNodes.append(l[i])
#                     i += 1
#                 elif i == 2:
#                     touchedNodes.append(l[i])
#                     i += 1
#                 else:
#                     i += 1
#                     continue


#         #dictionary of all nodes {A: [touchedNodesByA], B:[touchedNodesByB]}
#         for l in edges:
#             if l[0] == 1:
#                 checkEdgesA.append(l[1])
#                 checkEdgesA.append(l[2])
#             elif l[0] == 2:
#                 checkEdgesB.append(l[1])
#                 checkEdgesB.append(l[2])
#             elif l[0] == 3:
#                 checkEdgesA.append(l[1])
#                 checkEdgesA.append(l[2])
#                 checkEdgesB.append(l[1])
#                 checkEdgesB.append(l[2])

        


#         #check if all nodes are touched by all both a and b
#         for node in touchedNodes:
#             if node in checkEdgesA and node in checkEdgesB :
#                 continue
#             else:
#                 return -1

#         res: int = 0

#         for node in touchedNodes:
#             for node in checkEdgesA:
#                 counter: int = 0
#                 counter: int = checkEdgesA.count(node)
#                 if counter > 1:
#                     res += counter - 1
#             for node in checkEdgesB:
#                 counter: int = checkEdgesB.count(node)
#                 if counter > 1:
#                     res += counter - 1
#         return res



# lista: list[int] = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
# print(maxNumEdgesToRemove(4, lista))

