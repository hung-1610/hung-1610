# Bài 4: Nhập dữ liệu và chuyển đổi kiểu

# 4.1. Nhập ba trường dữ liệu
ma_quan_sat = input("Nhập mã quan sát: ")
so_lan_do = int(input("Nhập số lần đo: "))
gia_tri_do = float(input("Nhập giá trị đo: "))
don_vi = input("Nhập đơn vị: ")

# 4.2. Tính giá trị dẫn xuất (đổi C sang F)
gia_tri_f = gia_tri_do * 9 / 5 + 32

print(f"\nMã quan sát: {ma_quan_sat}")
print(f"Số lần đo: {so_lan_do} (Kiểu: {type(so_lan_do)})")
print(f"Giá trị C: {gia_tri_do} (Kiểu: {type(gia_tri_do)})")
print(f"Đơn vị: {don_vi}")
print(f"Giá trị F: {gia_tri_f}")

so_lan_do_text = str(so_lan_do)
print(f"so_lan_do_text: '{so_lan_do_text}' (Kiểu: {type(so_lan_do_text)})")
