def remove_duplicates(nums: list([int])) -> int:
    if not nums:
        return 0
    slow,fast = 0,0
    while fast<len(nums):
        if nums[slow] != nums[fast]:
            slow+=1
            nums[slow]=nums[fast]
        fast+=1
    return slow+1


def remove_duplicates(nums: list([int])) -> int:
    if not nums:
        return 0
    slow,fast = 0,0
    while fast< len(nums):
        if nums[slow] != nums[fast]:
            slow+=1
            nums[slow]=nums[fast]
        fast+=1
    return slow+1


def remove_duplicates(nums: list([int])) -> int:
    if not nums:
        return 0
    slow,fast = 0,0
    while fast<len(nums):
        if nums[slow] != nums[fast]:
            slow+=1
            nums[slow]=nums[fast]
        fast+=1
    return slow+1


def remove_duplicates(nums : list([int])) -> int:
    if not nums:
        return 0
    slow, fast = 0,0
    while fast<len(nums):
        if nums[slow] != nums[fast]:
            slow+=1
            nums[slow]=nums[fast]
        fast+=1
    return slow+1


def remove_element(nums: list([int])) -> int:
    if not nums:
        return 0
    slow, fast = 0,0
    while fast< len(nums):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow+=1
        fast+=1
    return slow


def remove_element(nums: list([int])) -> int:
    if not nums:
        return 0
    slow, fast = 0,0
    while fast< len(nums):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow+=1
        fast+=1
    return slow


def remove_element(nums: list([int])) -> int:
    if not nums:
        return 0
    slow, fast = 0,0
    while fast< lent(nums):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow+=1
        fast+=1
    return slow



def remove_elemment(nums: list([int]), val: int) -> int:
    if not nums:
        return 0
    slow, fast = 0,0
    while fast < len(nums):
        if nums[fast] 1= val:
            nums[slow] = nums[fast]
            slow+=1
        fast+=1
    return slow


def remove_element(nums: list([int]), val: int) -> int:
    if not nums:
        return 0 
    slow, fast = 0,0
    while fast < len(nums):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow+=1
        fast+=1
    return slow


def remove_element(nums: list([int]), val: int) -> int:
    if not nums:
        return 0
    slow, fast = 0,0
    while fast < len(nums)
        if nums[fast]!= val:
            nums[slow] = nums[fast]
            slow+=1
        fast+=1
    return slow


def remove_element(nums: list(nums[int]), val: int) -> int:
    if not nums:
        return 0
    slow, fast = 0,0
    while fast < len(nums):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow+=1
        fast+=1
    return slow

def remove_elemnt(nums:list([int]), val:int) -> int:
    if not nums:
        return 0
    slow,fast = 0,0
    while fast< len(nums):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow+=1
        fast+=1
    return slow

def remove_element(nums: list([int]), val: int) -> int:
    if not nums:
        return 0 
    slow, fast = 0,0
    while fast < len(nums):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow+=1
        fast+=1
    return slow



def remove_element(nums: list([int]), val: int) -> int:
    if not nums:
        return 0
    slow, fast = 0,0
    while fast< len(nums):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow+=1
        fast+=1
    return slow


def remove_element(nums: list([int]), val: int) -> int:
    if not nums:
        return 0 
    slow, fast = 0,0
    while fast < len(nums):
        nums[slow] = nums[fast]
        slow+=1
    fast+=1
    return slow



def remove_element(nums: list([int]), val: int) -> int:
    if not nums:
        return 0
    slow, fast = 0,0
    while fast < len(nums):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow+=1
        fast+=1
    return slow


def remove_element(nums: list([int]), val: int) -> int:
    if not nums: 
        return 0
    slow, fast = 0,0
    while fast < len(nums):
        if nums[fast]!= val:
            nums[slow] = nums[fast]
            slow+=1
        fast+=1
    return slow

def remove_element(nums: list([int]), val: int) -> int:
    if not nums:
        return 0
    slow, fast = 0,0
    while fast< len(nums):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow+=1
        fast+=1
    return slow


def two_sum(nums: list([int]), target: int) -> list([int]):
    left, right = 0, len(nums)-1
    while left< right:
        total = nums[left] + nums[right]
        if total == target:
            return [left,right]
        elif total<target:
            left+=1
        else:
            right-=1
    return [-1,-1]


def two_sum(nums: list([int]), target: int) -> list([int]):
    left, right = 0, len(nums) -1:
    while left< right:
        total = nums[left] + nums[right]
        if total == target:
            return [left, right]
        elif total< target:
            left+=1
        else:
            right-=1
    return [-1,-1]


def two_sum(nums: list([int]), targetL int)-> list(int[]):
    left, right = 0, len(nums)-1
    while left < right :
        total = nums[left] + nums[right]
        if total == target:
            return [left, right]
        elif total < target:
            left+=1
        else:
            right -=1
    return [-1,-1]



def two_sum( nums: list(int[]), target: int) -> list([int]):
    left, right = 0, len(nums)-1
    while left< right:
        total = nums[left] = nums[right]
        if total == target:
            return [left, right]
        elif total< target:
            left+=1
        else:
            right-=1
    return [-1,-1]


def two_sum(nums: list([int]), target: int) -> list(int[]):
    left, right = 0, len(nums)-1
    while left< right:
        total = nums[left] + nums[right]
        if total == target:
            return [left, right]
        elif total< target:
            left+=1
        else:
            right-=1
    return [-1,-1]

def two_sum(nums: list(int[]), target: int) -> list[int]:
    left,right = 0, len(nums)-1
    while left<right:
        total nums[left] + nums[right]
        if total == target:
            return [left, right]
        elif total < target:
            left+=1
        else:
            right-=1
    return [-1,-1]


def two_sum(nums: list(int[]), target: int)  -> list(int[]):
    left, right = 0, len(nums)-1
    while left<right:
        total = nums[left] + nums[right]
        if total == target:
            return [left, right]
        elif total < target:
            left+=1
        else:
            right-=1
    return [-1,-1]


def two_sum(nums: list(int[]), target: int) -> list(int[]):
    left,right = 0, len(nums)-1
    while left< right:
        total = nums[left] + nums[right]
        if total == target:
            return [left, right]
        elif total< target:
            left+=1
        else:
            right-=1
    return [-1,-1]

def two_sum(nums:list([int]), target:int) -> list([int]):
    left,right = 0, len(nums)-1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [left,right]
        elif total< target:
            left+=1
        else:
            right-=1
    return [-1,-1]


def two_sum(nums: list([int]), target:int) -> list([int]):
    left, right = 0, len(nums)-1
    while left<right:
        total = nums[left] + nums[right]
        if otal == target:
            return [left, right]
        elif total< target:
            left+=1
        else:
            right-=1
    return [-1,-1]


def two_sum (nums: list([int]) , val: int) -> list([int]):
    left, right = 0, len(nums)-1
    while left< right:
        total = nums[left] + nums[right]
        if total == val:
            return [left, right]
        elif total< val:
            left +=1
        else:
            right-=1
    return [-1,-1]

def two_sum ( nums: list([int]), target: int) -> list([int]):
    left, right = 0, len(nums) -1
    while left< right:
        total= nums[left] + nums[right]
        if total == target:
            return [left, right]
        elif total< target:
            left+=1
        else:
            right -=1
    return [-1,-1]


def two_sum(nums: list([int]), target: int) -> list([int]):
    left, right =0, len(nums)-1
    while left< right:
        total = nums[left] + nums[right]
        if total == target:
            return [left, right]
        elif total< target:
            left+=1
        else:
            right-=1
    return [-1,-1]



def two_sum(nums: list([int]), target: int) -> list([int]):
    left,right=0, len(nums)-1
    while left< right:
        total = nums[left] + nums[right]
        if total == target:
            return [left,right]
        elif total<target:
            left+=1
        else:
            right-=1
    return [-1,-1]


def two_sum(nums: list([int]), target: int) -> list([int]):
    left, right = 0, len(nums)-1
    while left< right:
        total = nums[left] + nums[right]
        if total == target:
            return [left, right]
        elif total< target:
            left +=1
        else:
            right-=1
    return [-1,-1]

def palindrome(s: str, l: int, r: int) -> str:
    while l>=0 and r< len(s) and s[l] == s[r]:
        l-=1
        r+=1
    return s[l+1:r]


def palindrome(s: str, l: int, r: int) -> str:
    while l>=0 and r<len(s) and s[l] == s[r]:
        l-=1
        r+=1
    return s[l+1:r]

def palindrom(s:str, l:int, r:int) -> str:
    while l>=0 and r<len(s) and s[l] == s[r]:
        l-=1
        r+=1
    return s[l+1:r]


def palindrome(s:str, l:int, r:int) -> str:
    while l>=0 and r< len(s) and s[l] == s[r]:
        l-=1
        r+=1
    return s[l+1:r]


def palindrome(s:str, l:int, r:int) -> str:
    while l>=0 and r<len(s) and s[l] == s[r]:
        l-=1
        r+=1
    return s[l+1:r]


def palindrome(s:str, l:int, r:int) -> str:
    while l>=0 and r<len(s) and s[l] == s[r]:
        l-=1
        r+=1
    return s[l+1:r]



def move_zeroes(nums:list([int])) -> int:
    if not nums:
        return 0
    l,r = 0,0
    while r<len(nums):
        if nums[r]!=0:
            nums[l]=nums[r]
            l+=1
        r+=1
    return l


def valid_palindrome(s:str) -> bool:
    l,r=0,len(s)-1
    while l<r:
        if s[l] != s[r]
            return False
        else:
            l+=1
            r-=1
    return True


def palindrome(s:str, l:int, r:int)-> str:
    while l>=0 and r<len(s) and s[l] ==s[r]:
        l-=1
        r+=1
    return s[l+1:r]

def longestPalindrome(s:str)-> str:
    if not s:
        return ""
    longest = ""
    for i in range(len(s)):
        odd=palindrome(s,i,i)
        even=palindrome(s,i,i+1)
        longest = max(longest,odd,even)
    return longest


def move_zeroes(nums:list([int])) -> int:
    if not nums:
        return 0
    slow, fast = 0,0
    while fast<len(nums):
        if nums[fast] !=0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow+=1
        fast+=1
    return slow

def valid_palindrome(s:str)-> str:
    l,r = 0, len(nums) -1
    while l<r:
        if not s[l].isalnum():
            l+=1
        elif not s[r].isalnum():
            r-=1
        elif s[l].lower() != s[r].lower():
            return False
        else:
            l+=1
            r-=1
    return True

def palindrome(s:str, l:int, r: int) -> str:
    while l>=0 and r<len(s) and s[l] ==s[r]:
        l-=1
        r+=1
    return s[l+1:r]

def longest_palindrome(s:str) -> str:
    if not s:
        return ""
    longest = ""
    for i in range(len(s)):
        odd = palindrome(s,i,i)
        even = palindrome(s,i,i+1)
        longest = max(longest,even,odd,key=len)
    return longest



def valid_palindrome(s:str) -> bool:
    l,r = 0, len(s)-1
    while l< r:
        if not s[l].isalnum():
            l+=1
        elif not s[r].isalnum():
            r-=1
        elif s[l].lower() != s[r].lower():
            return False
        else:
            l+=1
            r-=1
    return True
        