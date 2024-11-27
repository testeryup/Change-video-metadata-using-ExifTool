import random
import re

# Mẫu của UUID gốc
original_uuids = [
    "31e7c5d4-cd2b-40c8-9eb6-43c4512f54f5",
    "3dc3e039-5ed0-432c-99d3-9e3b38e49dbd",
    "29264a29-a919-4538-9f3f-74ef2c55c34f",
    "31fdb3a6-d170-4a38-8980-eec1c21ac7a3",
    "1376e225-534d-4ea6-a092-f2cd45554ca7",    
    # Thêm các UUID gốc khác của bạn ở đây nếu cần
]

# Hàm để phân tích mẫu của các UUID gốc
def analyze_uuids(uuids):
    structure = re.compile(r"([a-f0-9]{8})-([a-f0-9]{4})-([a-f0-9]{4})-([a-f0-9]{4})-([a-f0-9]{12})")
    parts = {'part1': [], 'part2': [], 'part3': [], 'part4': [], 'part5': []}
    for u in uuids:
        match = structure.match(u)
        if match:
            parts['part1'].append(match.group(1))
            parts['part2'].append(match.group(2))
            parts['part3'].append(match.group(3))
            parts['part4'].append(match.group(4))
            parts['part5'].append(match.group(5))
    return [len(part[0]) for part in parts.values()]

# Phân tích mẫu
part_lengths = analyze_uuids(original_uuids)

# Hàm để tạo một phần của UUID mới
def create_new_uuid_part(part_lengths):
    return '-'.join(''.join(random.choices('0123456789abcdef', k=length)) for length in part_lengths)

# Tạo nhiều UUID mới
def create_multiple_uuids(part_lengths, number_of_uuids):
    return [create_new_uuid_part(part_lengths) for _ in range(number_of_uuids)]

# Hỏi người dùng muốn tạo bao nhiêu UUID
number_of_uuids = int(input("Nhập số lượng UUID bạn muốn tạo: "))

# Kiểm tra và đảm bảo số lượng UUID là một số hợp lệ
if number_of_uuids > 0:
    # Tạo số lượng UUID đã yêu cầu
    new_uuids = create_multiple_uuids(part_lengths, number_of_uuids)

    # Tên file để lưu UUID
    filename = "new_uuids.txt"

    # Mở file và ghi UUID
    with open(filename, 'w') as file:
        for uuid in new_uuids:
            file.write(uuid + "\n")

    print(f"Đã xuất {number_of_uuids} UUID mới vào file '{filename}'")
else:
    print("Vui lòng nhập một số lượng hợp lệ.")
