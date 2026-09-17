def backtrack(path, choices):
    if termination_condition:
        result.append(path.copy())
        return
    for choice in choices:
        path.append(choice)
        backtrack(path, updated_choices)
        path.pop()

def backtrack(path, choices):
    if termination_condition:
        result.append(path.copy())
        return
    for choice in choices:
        path.append(choice)
        backtrack(path, updated_choices)
        path.pop()

def backtrack(path,choices):
    if termination_condition:
        result.append(path.copy())
        return
    for choice in choices:
        path.append(choice)
        backtrack(path, updated_choices)
        path.pop()

def backtrack(path, choices):
    if termination_condition:
        result.append(path.copy())
        return
    for choice in choices:
        path.append(choice)
        backtrack(path, updated_choices)
        path.pop()

def backtrack(path, choices):
    if termination_condition:
        result.append(path.copy())
        return
    for choice in choices:
        path.append(choice)
        backtrack(path,updated_choices)
        path.pop()

def permute(nums):
    result = []
    path = []
    used = [False] * len(nums)

    def backtrack():
        if len(path) == len(nums):
            result.append(path.copy())
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            path.append(nums[i])
            used[i] = True
            backtrack()
            path.pop()
            used[i] = False
    backtrack()
    return result

def permute(nums):
    result = []
    path = []
    used = [False] * len(nums)

    def backtrack():
        if len(nums) == len(path):
            result.append(path.copy())
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            path.append(nums[i])
            used[i] = True
            backtrack()
            path.pop()
            used[i] = False
    backtrack()
    return result


def permute(nums):
    result = []
    path = []
    used = [False] * len(nums)

    def backtrack():
        if len(nums) == len(path):
            result.append(path.copy())
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            path.append(nums[i])
            used[i] = True
            backtrack()
            path.pop()
            used[i] = False
    backtrack()
    return result

def permute(nums):
    result = []
    used = [False] * len(nums)
    path = []

    def backtrack():
        if len(path) == len(nums):
            return
        for i in range(len(nums)):
            path.append(nums[i])
            used[i] = True
            backtrack()
            used[i] = False
            path.pop()
    backtrack()
    return result

def permute(nums):
    result = []
    used = [False] * len(nums)
    path = []

    def backtrack():
        if len(nums) == len(path):
            return
        for i in range(len(nums)):
            path.append(nums[i])
            used[i] = True
            backtrack()
            path.pop()
            used[i] = False
    backtrack()
    return result

def permute(nums):
    result = []
    path = []
    used = [False] * len(nums)
    def backtrack():
        if len(path) == len(nums):
            return
        for i in range(len(nums)):
            path.append(nums[i])
            used[i] = True
            backtrack()
            path.pop()
            used[i] = False
    backtrack()
    return result


def permute(nums):
    result = []
    path =[]
    used = [False] * len(nums)

    def backtrack():
        if len(nums) == len(path):
            result.append(path.copy())
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            path.append(nums[i])
            used[i] = True
            backtrack()
            used[i] = False
            path.pop()

    backtrack()
    return result

def permute(nums):
    result = []
    path = []
    used = [False] * len(nums)

    def backtrack():
        if len(nums) == len(path):
            result.append(path.copy())
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            path.append(nums[i])
            used[i] = True
            backtrack()
            used[i] = False
            path.pop()
    backtrack()
    return result

def permute(nums):
    result =[]
    path = []
    used = [False] * len(nums)

    def backtrack():
        if len(nums) == len(path):
            result.append(path.copy())
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack()
            path.pop()
            used[i] = False
    backtrack()
    return result
