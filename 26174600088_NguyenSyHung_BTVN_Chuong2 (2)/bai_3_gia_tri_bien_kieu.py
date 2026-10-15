# Bài 3: Giá trị, biến và kiểu dữ liệu

# 3.1. Khởi tạo một bản quan sát
ma_quan_sat = "OBS025"
so_lan_do = 4
gia_tri_do = 31.5
hop_le = True
ghi_chu = None

print("ma_quan_sat:", ma_quan_sat, "-> Kiểu:", type(ma_quan_sat))
print("so_lan_do:", so_lan_do, "-> Kiểu:", type(so_lan_do))
print("gia_tri_do:", gia_tri_do, "-> Kiểu:", type(gia_tri_do))
print("hop_le:", hop_le, "-> Kiểu:", type(hop_le))
print("ghi_chu:", ghi_chu, "-> Kiểu:", type(ghi_chu))

# 3.2. Gán lại giá trị
gia_tri_do = 31.5
print("Lần 1 gia_tri_do:", gia_tri_do)

gia_tri_do = 29.8
print("Lần 2 gia_tri_do:", gia_tri_do)
# Giải thích: Sau phép gán thứ hai, biến gia_tri_do được cập nhật và truy cập giá trị mới là 29.8

# 3.3. None và các giá trị khác
print("None == 0:", None == 0)        # Dự đoán: False
print("None == '':", None == "")      # Dự đoán: False
print("None == False:", None == False)# Dự đoán: False
