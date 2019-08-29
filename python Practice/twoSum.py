def toSum(nums,target):
    map = {}
    for i in range(len(nums)):
        num = nums[i]
        if(target-num in map):
            answer = [map[target-num],i]
            return answer
        else:
            map[num]=i
    return None


print(toSum([2, 11, 15],9))