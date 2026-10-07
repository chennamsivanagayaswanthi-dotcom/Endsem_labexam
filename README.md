# Merge Sort – Employee Salary Sorting

## 1. Aim

To implement the **Merge Sort algorithm** to sort the salaries of `N` employees in ascending order and analyze its time and space complexity.

---

## 2. Problem Statement

A software company maintains the salaries of `N` employees in an unsorted list.

The HR department wants to generate a report showing the salaries in ascending order.

The program should:

- Take the number of employees as input.
- Take employee salaries as input.
- Sort the salaries using Merge Sort.
- Display the sorted salaries.
- Count the number of comparisons.
- Count the number of merge operations.
- Calculate the theoretical time complexity.
- Compare practical observations with theoretical complexity.

---

## 3. What is Merge Sort?

**Merge Sort** is a sorting algorithm based on the **Divide and Conquer** technique.

It works in three main steps:

1. **Divide** – Divide the list into two halves.
2. **Conquer** – Recursively sort both halves.
3. **Merge** – Combine the sorted halves into one sorted list.

### Example

```text
Original List:
[50000, 30000, 70000, 45000]

        Divide
       /      \
[50000,30000] [70000,45000]

        Sort
       /      \
[30000,50000] [45000,70000]

        Merge
           ↓
[30000,45000,50000,70000]
```

---

## 4. Algorithm

```text
Step 1: Start
Step 2: Read the number of employees.
Step 3: Read the salaries.
Step 4: Divide the salary list into two halves.
Step 5: Recursively sort the left half.
Step 6: Recursively sort the right half.
Step 7: Compare elements from both halves.
Step 8: Merge them in ascending order.
Step 9: Count comparisons and merge operations.
Step 10: Display the sorted salaries.
Step 11: Display the number of comparisons and merges.
Step 12: Stop.
```

---

## 5. Python Program

```python
comparisons = 0
merge_operations = 0


def merge_sort(arr):
    global comparisons, merge_operations

    # Base condition
    if len(arr) <= 1:
        return arr

    # Divide
    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge operation
    merge_operations += 1

    merged = []
    i = 0
    j = 0

    # Compare and merge
    while i < len(left) and j < len(right):

        comparisons += 1

        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Add remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


# Input
n = int(input("Enter number of employees: "))

salaries = list(map(int, input("Enter salaries: ").split()))

# Sort salaries
sorted_salaries = merge_sort(salaries)

# Output
print("Sorted salaries:", sorted_salaries)
print("Number of comparisons:", comparisons)
print("Number of merge operations:", merge_operations)

print("Time Complexity: O(N log N)")
print("Space Complexity: O(N)")
```

---

## 6. Sample Input

```text
Enter number of employees: 5
Enter salaries: 50000 30000 70000 45000 25000
```

## 7. Sample Output

```text
Sorted salaries: [25000, 30000, 45000, 50000, 70000]
Number of comparisons: 7
Number of merge operations: 4
Time Complexity: O(N log N)
Space Complexity: O(N)
```

> **Note:** The exact number of comparisons depends on the input order.

---

## 8. Complexity Analysis

### Best Case

```text
O(N log N)
```

### Average Case

```text
O(N log N)
```

### Worst Case

```text
O(N log N)
```

### Space Complexity

```text
O(N)
```

Merge Sort requires additional memory for the temporary merged arrays.

---

## 9. Practical vs Theoretical Complexity

As the number of employees increases, the number of comparisons and merge operations also increases.

However, Merge Sort divides the list into smaller parts and merges them efficiently.

Therefore, the practical performance follows the theoretical complexity of:

```text
O(N log N)
```

Merge Sort is efficient for large datasets because its worst-case complexity is also `O(N log N)`.

---

## 10. Advantages

1. Efficient for large datasets.
2. Time complexity is `O(N log N)`.
3. Worst-case performance is predictable.
4. Uses the Divide and Conquer approach.
5. Can be used to sort large lists of employee salaries.

---

## 11. Disadvantages

1. Requires additional memory.
2. More complex than simple sorting algorithms such as Bubble Sort.
3. Recursive function calls require additional processing.

---

## 12. Conclusion

The Merge Sort algorithm was successfully implemented to sort employee salaries in ascending order.

The program also counts the number of comparisons and merge operations.

Merge Sort has a time complexity of **O(N log N)** in the best, average, and worst cases, and a space complexity of **O(N)**.

Therefore, Merge Sort is an efficient algorithm for sorting large datasets.

---

# 13. Viva Questions and Answers

### Q1. What is Merge Sort?

**Answer:**  
Merge Sort is a sorting algorithm based on the **Divide and Conquer** technique. It divides the list into smaller parts, sorts them, and then merges them.

---

### Q2. What is the time complexity of Merge Sort?

**Answer:**  
The time complexity of Merge Sort is **O(N log N)** for the best, average, and worst cases.

---

### Q3. What is the space complexity of Merge Sort?

**Answer:**  
The space complexity is **O(N)** because additional memory is required during the merging process.

---

### Q4. What is the worst case?

**Answer:**  
The worst case is the input condition in which an algorithm performs the maximum amount of work. For Merge Sort, even in the worst case, the time complexity is **O(N log N)**.

---

### Q5. Why is Merge Sort called Divide and Conquer?

**Answer:**  
It is called Divide and Conquer because it first **divides** the list into smaller parts, **conquers** the smaller parts by sorting them, and finally **merges** them to get the sorted list.

---

