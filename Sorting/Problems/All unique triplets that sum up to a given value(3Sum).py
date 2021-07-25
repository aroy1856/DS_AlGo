def threeSum(nums, targetSum):
    nums.sort()
    a = []
    n = len(nums)

    for i in range(n-2):
        if (i == 0) or (nums[i] > nums[i-1]):
            s = i+1
            e = n-1
            target = targetSum - nums[i] #remaing Sum

            while s < e:
                if ((s > i+1) and (nums[s] == nums[s-1])):
                    s += 1
                    continue

                if ((e < n-1) and (nums[e] == nums[e+1])):
                    e -= 1
                    continue
                
                if nums[s] + nums[e] == target:
                    a.append([nums[i], nums[s], nums[e]])
                    s += 1
                    e -= 1
                elif nums[s] + nums[e] > target:
                    e -= 1
                else:
                    s += 1
    
    return a

a = [12, 3, 6, 1, 6, 9]
targetSum = 24
threeSum(a,targetSum)
