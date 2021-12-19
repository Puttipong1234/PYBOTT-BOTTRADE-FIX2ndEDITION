# if condition

# IsBitcoin = True

# if IsBitcoin:
#     print("This is bitcoin , Buy 100 USDT")


# Symbol = input("กรุณากรอกตัวย่อชื่อสินค้า : ")

# if Symbol == "ETH":
#     print("This is Ethereum , buy 200 USDT")

# elif Symbol == "BTC":
#     print("This is bitcoin , Buy 100 USDT")

# elif Symbol == "DOGE" or Symbol == "LTC":
#     print("This is " + Symbol + ", Buy 50 USDT")

# else:
#     print("This is not ethereum !")

# while ... การทำงานวนซ้ำ
# รอบที่วิ่ง = 1
# while รอบที่วิ่ง <= 10: # <= >= == 
#     print("ฉันกำลังวิ่งอยู่รอบที่ - " + str(รอบที่วิ่ง))
#     รอบที่วิ่ง = รอบที่วิ่ง + 1

# print("เย่! วิ่งครบรอบแล้ววว")

# จงเขียนโปรแกรม รับค่าคู่เหรียญที่ต้องการซื้อใน binance จาก User จำนวน 5 คู่
# ถ้ามี bitcoin อยู่ใน ลิสที่ user ต้องการซ์้อ เราจะแสดงผลว่า "hello bitcoiner"

# คู่เหรียญทั้งหมด = []
# รอบที่รับข้อมูล = 1
# while รอบที่รับข้อมูล <=5 :
#     คู่เหรียญที่ต้องการซื้อ = input("กรุณากรอกชื่อคู่เหรียญที่ท่านต้องการซื้อ  :  ")
#     คู่เหรียญทั้งหมด.append(คู่เหรียญที่ต้องการซื้อ)
#     if "BTC" in คู่เหรียญที่ต้องการซื้อ: # "BTCUSDT"
#         print("hello bitcoiner")
    
#     รอบที่รับข้อมูล = รอบที่รับข้อมูล + 1

# print(คู่เหรียญทั้งหมด)

คู่เหรียญทั้งหมด = []
while True :
    คู่เหรียญที่ต้องการซื้อ = input("กรุณากรอกชื่อคู่เหรียญที่ท่านต้องการซื้อ  :  ")

    if "EXIT" == คู่เหรียญที่ต้องการซื้อ:
        break

    คู่เหรียญทั้งหมด.append(คู่เหรียญที่ต้องการซื้อ)
    if "BTC" in คู่เหรียญที่ต้องการซื้อ: # "BTCUSDT"
        print("hello bitcoiner")
    
print(คู่เหรียญทั้งหมด)