# Nhập vốn ban đầu và sau khi bán ra

initial = float(input("vốn ban đầu: "))

final = float(input("tiền sau khi bán ra: "))

# Lãi nhuận ròng

profit = final - initial

# Roi và xuất ra kết quả

roi = (profit / initial) * 100

print(f"Lãi nhuận ròng: {profit:.2f} VNĐ")

print(f"ROI: {roi:.2f}%")