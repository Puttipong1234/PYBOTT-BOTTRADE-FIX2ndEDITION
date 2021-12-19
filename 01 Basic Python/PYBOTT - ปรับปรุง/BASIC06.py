# Function

# x = 5
# y = 6
# z = 8
# result = (x + y)/ z
# print(result)

# define function
# def f(x,y,z):
#     result = (x + y)/ z
#     return result

# result = f(x=5,y=6,z=8)
# print(result)
# result = f(x=10,y=20,z=30)
# print(result)

def คำนวณจำนวนบิทคอยที่ต้องซื้อ(ราคาบิทคอย,ชื่อexchange):
    เงินที่เรามี = float(input("กรุณากรอกจำนวนเงินในหน่วย USD ที่ต้องการซื้อภายใน "+ ชื่อexchange + " : "))
    # เงินที่เรามี หารด้วย ราคา BTC และ ETH ณ ปัจจุบัน
    BTC_price = ราคาบิทคอย

    # คำนวน
    จำนวนBTCที่สามารถซื้อได้ = round(เงินที่เรามี/BTC_price,3)
    จำนวนBTCที่สามารถซื้อได้ = format(จำนวนBTCที่สามารถซื้อได้,'.3f') # override
    print("คำนวณเสร็จสิ้น")

    return จำนวนBTCที่สามารถซื้อได้

if __name__ == "__main__": # ให้การทำงานด้านล่างเกิดขึ้นเฉพาะจากการรันไฟล์นี้เท่านั้น
    # ต้องการจำนวนเงินที่ต้องนำไปซื้อบิทคอยในแพลตฟอมต่างๆ
    # platform มีราคาบิทคอยที่ต่างๆ binance bitkub ftx
    BitcoinInBinance = คำนวณจำนวนบิทคอยที่ต้องซื้อ(ราคาบิทคอย=50100,ชื่อexchange="Binance")
    BitcoinInBitkub = คำนวณจำนวนบิทคอยที่ต้องซื้อ(ราคาบิทคอย=50300,ชื่อexchange="Bitkub")
    BitcoinInftx = คำนวณจำนวนบิทคอยที่ต้องซื้อ(ราคาบิทคอย=50500,ชื่อexchange="ftx")

    print(BitcoinInBinance)
    print(BitcoinInBitkub)
    print(BitcoinInftx)