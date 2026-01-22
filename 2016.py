def maximumDifference(nums: list[int]) -> int:
    m=-1
    for i in range(len(nums)-1):
        a= [ j for j in nums[i+1:] if j>nums[i]]
        if len(a)!=0:
            if m < max(a)-nums[i]:
                m=max(a)-nums[i]
    return m

print(maximumDifference([10,2,1,3]))