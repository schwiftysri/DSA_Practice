def search(nums: list([int]), target: int) -> int:
    left, right = 0, len(nums)-1
    mid = left + (right-left)//2
    while left<=right:
        if nums[mid] == target:
            return mid
        elif nums[mid]<target:
            left = mid+1
        else:
            right = mid-1
    return -1


def search(nums: list([int]), target: int)-> int:
    left,right = 0, len(nums)-1
    mid = left+(right-left)//2
    while left<=right:
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid+1
        else:
            right = mid -1
    return -1

def search(nums:list([int]),target:int)-> int:
    left,right = 0,len(nums)-1
    mid = left(right-left)//2
    while left<=right:
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid+1
        else:
            right = mid -1
    return -1

def search(nums:list([int]), target:int)-> int:
    left,right = 0, len(nums)-1
    mid = left + (right-left)//2
    while left<=right:
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid+1
        else:
            right = mid -1
    return -1

def search(nums, target):
    left, right = 0 ,len(nums)-1
    mid = left+(right-left)//2
    while left<=right:
        if nums[mid] == target:
            return mid
        elif nums[mid]<target:
            left = mid+1
        else:
            right = mid-1
    return -1


def search(nums,target):
    left,right = 0, len(nums)-1
    while left<=right:
        mid = left + (right-left)//2
        if nums[mid] == target:
            return mid
        elif nums[mid]<target:
            left = mid+1
        else:
            right = mid-1
    return -1

def search(nums:list([int]), target:int)-> int:
    left,right = 0, len(nums)-1
    while left<=right:
        mid = left + (right - left)//2
        if nums[mid] == target:
            return mid
        elif nums[mid]< target:
            left = mid+1
        else: 
            right = mid-1
    return -1

def search(nums,target):
    left,right = 0, len(nums)-1
    while left<= right:
        mid = left+(right-left)//2
        if nums[mid] == target:
            return mid
        elif nums[mid]<target:
            left = mid+1
        else:
            right = mid-1
    return -1

def search(nums:list([int]), target:int)-> int:
    left, right = 0, len(nums)-1
    while left<= right:
        mid = left+(right-left)//2
        if nums[mid] == target:
            return mid
        elif nums[mid]<target:
            left = mid +1
        else:
            right = mid-1
    return -1

def search(nums,target):
    left,right = 0, len(nums)-1
    while left<=right:
        mid = left + (right-left)//2
        if nums[mid] == target:
            return mid
        elif nums[mid]<target:
            left = mid+1
        else:
            right = mid-1
    return -1

def search(nums,target):
    left, right = 0,len(nums)-1
    while left<=right:
        mid = left+(right-left)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid+1
        else:
            right = mid-1
    return -1

def left_bound(nums,target):
    left, right = 0, len(nums)-1
    while left<=right:
        mid = left + (right-left)//2
        if nums[mid]<target:
            left = mid+1
        elif nums[mid]>target:
            right = mid-1
        elif nums[mid] == target:
            right = mid -1
    return left

def left_bound(nums,target):
    left, right = 0 , len(nums)-1
    while left<=right:
        mid = left + (right-left)//2
        if nums[mid] < target:
            left = mid +1
        elif nums[mid] > target:
            right = mid -1
        elif nums[mid] == target:
            right = mid -1
    return left

def left_bound(nums,target):
    left, right = 0 ,len(nums)-1
    while left <=right:
        mid = left + (right-left)//2
        if nums[mid] == target:
            right = mid -1
        elif nums[mid]<target:
            left = mid +1
        else:
            right = mid -1
    return left

def left_bound(nums,target):
    left, right = 0 , len(nums)-1
    while left<= right:
        mid = left + (right -left)//2
        if nums[mid] < target:
            left = mid +1
        elif nums[mid] > target:
            right = mid -1
        elif nums[mid] == target:
            right = mid -1
    return left

def left_bound(nums,target):
    left, right = 0, len(nums)-1
    while left<= right:
        mid = left + (right - left)//2
        if nums[mid] >= target:
            right = mid -1
        else:
            left = mid +1
    return left

def left_bound(nums,target):
    left, right = 0 , len(nums)-1
    while left <=right:
        mid = left + (right -left)//2
        if nums[mid]>= target:
            right = mid -1
        else:
            left = mid +1
    return left

def left_bound(nums,target):
    left, right = 0 , len(nums)-1
    while left<= right:
        mid = left+(right-left)//2
        if nums[mid] >= target:
            right = mid -1
        else:
            left = mid +1
    return left


def right_bound(nums,target):
    left, right = 0 , len(nums)-1
    while left<=right:
        mid = left + (right-left)//2
        if nums[mid] <= target:
            left = mid+1
        else:
            right = mid-1
    return right

def right_bound(nums,target):
    left,right = 0 , len(nums)-1
    while left<=right:
        mid = left + (right - left)//2
        if nums[mid] <= target:
            left = mid+1
        else:
            right = mid -1
    return right

def right_bound(nums,target):
    left, right = 0, len(nums)-1
    while left<=right:
        mid = left + (right-left)//2
        if nums[mid] <=target:
            left = mid+1
        else:
            right = mid -1
    return right

def right_bound(nums,target):
    left,right = 0 ,len(nums)-1
    while left<=right:
        mid = left + (right-left)//2
        if nums[mid]<=target:
            left = mid+1
        else:
            right = mid -1
    return right

def right_bound(nums,target):
    left,right = 0 , len(nums)-1
    while left<=right:
        mid = left + (right - left)//2
        if nums[mid]<=target:
            left = mid +1
        else:
            right = mid -1
    return right

def right_bound(nums,target):
    left,right = 0, len(nums)-1
    while left<=right:
        mid = left + (right-left)//2
        if nums[mid]<= target:
            left = mid+1
        else:
            right = mid-1
    return right

def right_bound(nums,target):
    left,right = 0, len(nums)-1
    while left<=right:
        mid = left + (right-left)//2
        if nums[mid]<=target:
            left = mid+1
        else:
            right = mid-1
    return right



def left_bound(nums,target):
    left,right = 0,len(nums)-1
    while left<=right:
        mid = left + (right-left)//2
        if nums[mid] >= target:
            right = mid -1
        else:
            left = mid +1
    if nums[left] != target:
        return -1
    else:
        return left
def right_bound(nums,target):
    left,right = 0, len(nums)-1
    while left<=right:
        mid = left + (right-left)//2
        if nums[mid]<=target:
            left = mid+1
        else:
            right = mid -1
    if nums[right] != target:
        return -1
    else:
        return right
    
def search(nums, target):
    l = left_bound(nums,target)
    r = right_bound(nums,target)
    return [l,r]

def left_bound(nums,target):
    left,right = 0, len(nums)-1
    while left<=right:
        mid = left + (right-left)//2
        if nums[mid] >=target:
            right = mid -1
        else:
            left = mid +1
    if left <0 or left>len(nums)-1:
        return -1
    else:
        if nums[left]!=target:
            return -1
        else:
            return left
def right_bound(nums,target):
    left, right = 0, len(nums)-1
    while left<=right:
        mid = left + (right-left)//2
        if nums[mid] <= target:
            left = mid +1
        else:
            right = mid -1
    if right <0 or right >len(nums)-1:
        return -1
    else:
        if nums[right]!=target:
            return -1
        else:
            return right
def search(nums,target):
    l = left_bound(nums,target)
    r = right_bound(nums,target)
    return [l,r]
