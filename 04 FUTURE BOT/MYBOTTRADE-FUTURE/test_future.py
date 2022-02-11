from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *
from binance_f.model.constant import *

from config import BINANCE_FUTURE_API_KEY , BINANCE_FUTURE_API_SECRET

# เชื่อมต่อกับ client
request_client = RequestClient(api_key=BINANCE_FUTURE_API_KEY,secret_key=BINANCE_FUTURE_API_SECRET)

# result = request_client.get_account_information()

# เช็คข้อมูล user 
# print(result.totalWalletBalance)
# print(result.totalUnrealizedProfit)
# print(result.totalMarginBalance)
# print(dir(result))

# asset = result.__dict__["assets"][0].asset
# print(asset)
# asset = result.__dict__["assets"][0].unrealizedProfit
# print(asset)

# asset = result.__dict__["assets"][0] # DOT
# print(dir(asset))

# result = request_client.get_open_interest(symbol="BTCUSDT")
# print(result.openInterest)

# result = request_client.get_mark_price(symbol="BTCUSDT")
# print(result.markPrice)

# PrintMix.print_data(result.symbols)

# Function คำนวนจำนวนที่จะซื้อ รับค่าเป็น USDT , SYMBOL => Get stepsize and price precision BINANCE
# from binance.helpers import round_step_size
# SYMBOL = "1000SHIBUSDT"
# AMOUNT_USDT = 100

# result = request_client.get_mark_price(symbol=SYMBOL)
# ราคาปัจจุบัน = float(result.markPrice)

# result = request_client.get_exchange_information()
# for i in result.symbols:
#     if i.symbol == SYMBOL:
#         # print(i.__dict__)
#         print("STEP SIZE : " + i.filters[1]["stepSize"] )
#         STEP_SIZE = float(i.filters[1]["stepSize"])
#         print("pricePrecision : " + str(i.pricePrecision) )
#         จำนวนที่ต้องการซื้อ = AMOUNT_USDT/ราคาปัจจุบัน
#         print(จำนวนที่ต้องการซื้อ)
#         print(round_step_size(จำนวนที่ต้องการซื้อ,STEP_SIZE))


# การทำ Order MARKET ONLY !

# ได้รับสัญญาณมา
ORDER = "OPEN"
SIDE = "LONG"
AMOUNT_USDT = 5
LEVERAGE = 30
SYMBOL = "DOGEUSDT"

# แล้วเราจะต้องเปิด position ที่ size เท่าไหร่ ?
# ( AMOUNT_USDT*LEVERAGE ) / ราคา ณ ปัจจุบัน = quantity
# 1. Get mark price ดึงราคา ณ ปัจจุบัน
result = request_client.get_mark_price(symbol=SYMBOL)

print("======= Mark Price =======")
# ราคาปัจจุบัน = float(result.markPrice)
# quantity = ( AMOUNT_USDT*LEVERAGE ) / ราคาปัจจุบัน
# print(quantity)
from trade import CalculateAmount
quantity = CalculateAmount(AMOUNT_USDT=AMOUNT_USDT, SYMBOL=SYMBOL,LEVERAGE=LEVERAGE)
# 2. Change leverage 
result = request_client.change_initial_leverage(symbol=SYMBOL, leverage=LEVERAGE)


# OPEN LONG
# resultOrder = request_client.post_order(symbol = SYMBOL,
#                                         side = OrderSide.BUY, #เปิด LONG BUY , SHORT SELL
#                                         ordertype = OrderType.MARKET,
#                                         quantity = quantity)

#TPSL LONG
# 3. get position ก่อนปิด position ดึงข้อมูล position ก่อนหน้ามาดูข้อมูล quantity ที่ต้องปิด

def get_position_amount_by_symbol(symbol):
    
    result = request_client.get_position_v2()
    for i in result:
        data = i.__dict__
        if data["symbol"] == symbol:
            print(data["positionAmt"])
            print(data["unrealizedProfit"])
            
            return str(abs(float(data["positionAmt"])))


# TPSLOrder = request_client.post_order(symbol = SYMBOL,
#                                       side = OrderSide.SELL,
#                                       ordertype = OrderType.MARKET,
#                                       quantity=get_position_amount_by_symbol(SYMBOL),
#                                       reduceOnly=True) # ถ้าเป็นการปิด position ต้องใส่ !

# OPEN SHORT
# resultOrder = request_client.post_order(symbol = SYMBOL,
#                                         side = OrderSide.SELL, #เปิด LONG BUY , SHORT SELL
#                                         ordertype = OrderType.MARKET,
#                                         quantity = quantity)

#TPSL SHORT
# TPSLOrder = request_client.post_order(symbol = SYMBOL,
#                                       side = OrderSide.BUY,
#                                       ordertype = OrderType.MARKET,
#                                       quantity=get_position_amount_by_symbol(SYMBOL),
#                                       reduceOnly=True) # ถ้าเป็นการปิด position ต้องใส่ !