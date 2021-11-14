def removeElement( nums, val):
    i = 0 
    rp = len(nums)
    while i<rp:
        if nums[i]==val:
            nums[i]= nums[rp-1]
            rp = rp-1
        else:
            i = i+1
    return rp

removeElement([3,2,2,3], 2)