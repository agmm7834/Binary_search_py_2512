def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def binary_search_first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result


def binary_search_last_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result


def binary_search_insert_position(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


def binary_search_floor(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            result = arr[mid]
            left = mid + 1
        else:
            right = mid - 1
    return result


def binary_search_ceiling(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            result = arr[mid]
            right = mid - 1
        else:
            left = mid + 1
    return result


def binary_search_rotated_array(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


def find_peak_element(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left


def sqrt_binary_search(n):
    if n < 2:
        return n
    left, right = 1, n // 2
    result = 0
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == n:
            return mid
        elif mid * mid < n:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Binary Search:", binary_search(arr, 5))
    
    arr2 = [1, 2, 2, 2, 3, 4, 5]
    print("First Occurrence:", binary_search_first_occurrence(arr2, 2))
    print("Last Occurrence:", binary_search_last_occurrence(arr2, 2))
    
    arr3 = [1, 3, 5, 7, 9]
    print("Insert Position:", binary_search_insert_position(arr3, 6))
    
    arr4 = [1, 2, 4, 6, 8, 10]
    print("Floor:", binary_search_floor(arr4, 5))
    print("Ceiling:", binary_search_ceiling(arr4, 5))
    
    arr5 = [4, 5, 6, 7, 0, 1, 2]
    print("Rotated Array:", binary_search_rotated_array(arr5, 0))
    
    arr6 = [1, 2, 3, 1]
    print("Peak Element:", find_peak_element(arr6))
    
    print("Square Root:", sqrt_binary_search(16))
