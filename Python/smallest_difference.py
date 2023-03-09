from typing import List, Tuple

def smallest_difference(nums: List[int]) -> Tuple[int, int]:
    diff = max(nums)
    found = tuple()

    nums.sort()
    for i in range(len(nums)-1):
        d = nums[i+1] - nums[i]
        if (d < diff):
            diff = d
            found = (nums[i], nums[i+1])

    return found

        
