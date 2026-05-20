print("=== SỐ LƯỢNG NHÂN SỰ MỚI ===")
count = 0
while count <= 0:
    count = int(input("Vui lòng nhập số lượng nhân sự mới trong tháng này: "))

    if count <= 0:
        print("[LỖI] Số lượng phải là số nguyên dương (>0). Vui lòng nhập lại!\n")

print(f"[THÀNH CÔNG] Đã ghi nhận yêu cầu cấp phát tài sản cho {count} nhân sự mới!")
print("--- CHƯƠNG TRÌNH KẾT THÚC ---")
