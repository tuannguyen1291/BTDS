def count_occurrences(numbers, counts={}):
    # Nếu counts chưa được khởi tạo, ta sẽ khởi tạo nó
    if not counts:
        counts = dict.fromkeys(numbers, 0)

    # Trường hợp cơ bản của đệ quy: nếu danh sách số rỗng, trả về counts
    if not numbers:
        return counts

    # Đệ quy: đếm số lần xuất hiện của số đầu tiên và cập nhật counts
    counts[numbers[0]] += 1
    return count_occurrences(numbers[1:], counts)


# Nhập dãy số nguyên từ bàn phím
numbers = list(map(int, input("Nhập dãy số nguyên: ").split()))

# Tính số lần xuất hiện của từng số và in kết quả
counts = count_occurrences(numbers)
for num, count in counts.items():
    print(f"{num} xuất hiện {count} lần")
