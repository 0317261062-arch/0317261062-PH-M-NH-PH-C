# Chia tiền hoá đơn

tongbill = float(input("Nhập tổng tiền hóa đơn: "))

y        = float(input("Nhập phần trăm tip: "))

tip      = tongbill * y / 100

songuoi = int(input("Nhập số người chia: ")) 

tien_moi_nguoi = (tongbill + tip) / songuoi

print(f"Số tiền mỗi người phải trả: {tien_moi_nguoi:.2f} VNĐ")