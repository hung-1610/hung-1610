# Bài 5: F-string, thời gian và chương trình tích hợp
from datetime import datetime

# 5.1. Thiết kế dữ liệu nhập
ma_quan_sat = input("Nhập mã quan sát: ")
dai_luong = input("Nhập tên đại lượng: ")
gia_tri_do = float(input("Nhập giá trị đo: "))
don_vi = input("Nhập đơn vị: ")

# 5.2. Gắn thời điểm hiện tại
thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")

# 5.3. Xuất bản ghi bằng f-string
print("\n" + "="*30)
print(f"Mã quan sát : {ma_quan_sat}")
print(f"Đại lượng   : {dai_luong}")
print(f"Giá trị     : {gia_tri_do:.2f} {don_vi}")
print(f"Thời điểm   : {thoi_diem_text}")
print("="*30)
