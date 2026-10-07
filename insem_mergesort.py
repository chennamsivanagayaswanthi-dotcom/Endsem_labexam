def merge_sort(arr):

    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    merged = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


n = int(input("Enter number of employees: "))
salaries = list(map(int, input("Enter salaries: ").split()))
sorted_salaries = merge_sort(salaries)
print("Sorted salaries:", sorted_salaries)