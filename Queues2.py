def max_subarray_sum(nums):

    max_sum = float('-inf')
    current_sum = 0

    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

def min_subarray_sum(nums):

    min_sum = float('inf')
    current_sum = 0

    for num in nums:
        current_sum = min(num, current_sum + num)
        min_sum = min(min_sum, current_sum)

    return min_sum

def max_subarray_sum_circular(nums):

    max_sum = max_subarray_sum(nums)


    total_sum = sum(nums)
    min_sum = min_subarray_sum(nums)
    max_circular_sum = total_sum - min_sum


    return max(max_sum, max_circular_sum)
nums = [1, -2, 3, -2]
print(max_subarray_sum_circular(nums))

nums = [5, -3, 5]
print(max_subarray_sum_circular(nums))

