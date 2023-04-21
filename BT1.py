def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quick_sort(left) + [pivot] + quick_sort(right)

# Nhập dãy số từ bàn phím
arr = input("Nhập dãy số nguyên, cách nhau bởi khoảng trắng: ").split()
arr = [int(x) for x in arr]

# Sắp xếp dãy số bằng thuật toán Quick Sort
sorted_arr = quick_sort(arr)

# In ra dãy số đã được sắp xếp
print("Dãy số đã được sắp xếp theo thứ tự tăng dần:")
print(sorted_arr)
