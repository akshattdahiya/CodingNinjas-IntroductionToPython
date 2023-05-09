def search(nums: [int], target: int):
    flag = 0
    l = 0
    u = len(nums)
    m = (l +u)//2
    flag = 0
    for x in range(len(nums)):
        if nums[x]==target:
            flag = x
            return flag
            break
    while l<=u and nums[m]!=target:
        if target<nums[m]:
            u = m+1
        else:
            u = m-1
        if nums[m]==target:
            return m
        else:
            return "-1"
    pass
