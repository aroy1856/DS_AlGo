def threeSumClosest(nums, target):
    nums.sort()
    closestSum = 99999999
    n = len(nums)

    for i in range(n-2):
        s = i+1
        e = n-1

        while s < e:
            sum = nums[i] + nums[s] + nums[e]

            if abs(sum - target) < abs(closestSum - target):
                closestSum = sum
            if sum > target:
                e -= 1
            else:
                s += 1
    return closestSum