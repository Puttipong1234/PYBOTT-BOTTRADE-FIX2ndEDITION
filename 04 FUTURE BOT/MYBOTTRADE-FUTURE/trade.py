from config import BINANCE_API_KEY , BINANCE_API_SECRET

from binance.client import Client
from binance.helpers import round_step_size

from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *
from binance_f.model.constant import *

from config import BINANCE_FUTURE_API_KEY , BINANCE_FUTURE_API_SECRET

client = Client(BINANCE_API_KEY, BINANCE_API_SECRET)
future_client = RequestClient(api_key=BINANCE_FUTURE_API_KEY,secret_key=BINANCE_FUTURE_API_SECRET)
# myaccount_info = client.get_account()
# print(myaccount_info)

# balance = client.get_asset_balance(asset="USDT")
# print(balance["free"])

# if float(balance["free"]) < 15:
#     print("คุณมีจำนวนเงินไม่พอ")

# else:
#     print("จำนวนเงินมากพอสำหรับการซื้อขาย")

def CalculateAmount(AMOUNT_USDT,SYMBOL,LEVERAGE):

    result = future_client.get_mark_price(symbol=SYMBOL)
    ราคาปัจจุบัน = float(result.markPrice)
    AMOUNT_USDT = AMOUNT_USDT * LEVERAGE # Override ตัวแปร

    result = future_client.get_exchange_information()
    for i in result.symbols:
        if i.symbol == SYMBOL:
            # print(i.__dict__)
            print("STEP SIZE : " + i.filters[1]["stepSize"] )
            STEP_SIZE = float(i.filters[1]["stepSize"])
            print("pricePrecision : " + str(i.pricePrecision) )
            จำนวนที่ต้องการซื้อ = AMOUNT_USDT/ราคาปัจจุบัน
            print(จำนวนที่ต้องการซื้อ)
            print(round_step_size(จำนวนที่ต้องการซื้อ,STEP_SIZE))
            
            return round_step_size(จำนวนที่ต้องการซื้อ,STEP_SIZE) # amount_coin ที่คำนวนจาก amount USDT



# เปิด BUY AT MARKET Order !
def buy(symbol,amount_coin):
    # ราคาเหรียญตอนนี้ = client.get_avg_price(symbol="BTCUSDT")
    # ราคาเหรียญตอนนี้ = float(ราคาเหรียญตอนนี้["price"])
    # จำนวนที่ต้องการซื้อ = 20/ราคาเหรียญตอนนี้
    จำนวนที่ต้องการซื้อ = amount_coin
    ข้อมูลเหรียญ = client.get_symbol_info(symbol)
    stepSize = float(ข้อมูลเหรียญ["filters"][2]["stepSize"])
    จำนวนที่ต้องการซื้อ = round_step_size(จำนวนที่ต้องการซื้อ,stepSize)
    # print(จำนวนที่ต้องการซื้อ)

    order = client.order_market_buy(
        symbol=symbol,
        quantity=จำนวนที่ต้องการซื้อ)


 #==================================================
# sell At market
def sell(symbol,amount_coin):
    # balance = float(client.get_asset_balance(asset="BTC")["free"])
    # print(balance)
    จำนวนที่ต้องการขาย = amount_coin
    ข้อมูลเหรียญ = client.get_symbol_info(symbol)
    stepSize = float(ข้อมูลเหรียญ["filters"][2]["stepSize"])
    จำนวนที่ต้องการขาย = round_step_size(จำนวนที่ต้องการขาย,stepSize) - stepSize # 0.00046 - 0.00001 => 0.00045
    # print(จำนวนที่ต้องการขาย)
    order = client.order_market_sell(
        symbol=symbol,
        quantity=จำนวนที่ต้องการขาย)


#======================FUTURE============================
def get_position_amount_by_symbol(symbol):
    
    result = future_client.get_position_v2()
    for i in result:
        data = i.__dict__
        if data["symbol"] == symbol:
            print(data["positionAmt"])
            print(data["unrealizedProfit"])
            
            return str(abs(float(data["positionAmt"])))

def TPSL_LONG(symbol):
    TPSLOrder = future_client.post_order(symbol = symbol,
                                      side = OrderSide.SELL,
                                      ordertype = OrderType.MARKET,
                                      quantity=get_position_amount_by_symbol(symbol),
                                      reduceOnly=True) # ถ้าเป็นการปิด position ต้องใส่ !

def TPSL_SHORT(symbol):
    TPSLOrder = future_client.post_order(symbol = symbol,
                                      side = OrderSide.BUY,
                                      ordertype = OrderType.MARKET,
                                      quantity=get_position_amount_by_symbol(symbol),
                                      reduceOnly=True) # ถ้าเป็นการปิด position ต้องใส่ !
    
def OPEN_LONG(symbol,amount_usdt,leverage):
    quantity = CalculateAmount(AMOUNT_USDT=amount_usdt, SYMBOL=symbol,LEVERAGE=leverage)
    
    try:
        TPSL_SHORT(symbol) # ปิด short ก่อนทุกกรณี
    
    except Exception as e:
        print(e)
    
    result = future_client.change_initial_leverage(symbol=symbol, leverage=leverage)
    resultOrder = future_client.post_order(symbol = symbol,
                                        side = OrderSide.BUY, #เปิด LONG BUY , SHORT SELL
                                        ordertype = OrderType.MARKET,
                                        quantity = quantity)
    
    return

def OPEN_SHORT(symbol,amount_usdt,leverage):
    quantity = CalculateAmount(AMOUNT_USDT=amount_usdt, SYMBOL=symbol,LEVERAGE=leverage)
    
    try:
        TPSL_LONG(symbol) # ปิด short ก่อนทุกกรณี
    
    except Exception as e:
        print(e)
    
    result = future_client.change_initial_leverage(symbol=symbol, leverage=leverage)
    resultOrder = future_client.post_order(symbol = symbol,
                                        side = OrderSide.SELL, #เปิด LONG BUY , SHORT SELL
                                        ordertype = OrderType.MARKET,
                                        quantity = quantity)

    
#======================FUTURE============================

if __name__ == "__main__":
    amount = 0.0004
    sym = "BTCUSDT"
    # buy(symbol=sym,amount_coin=amount)
    # sell(symbol=sym,amount_coin=amount)
    
    # res = CalculateAmount(1000,"BNBUSDT")
    # print(res)
    
    # OPEN_LONG(symbol="DOGEUSDT", amount_usdt=5, leverage=50)
    # TPSL_LONG(symbol="DOGEUSDT")
    # OPEN_SHORT(symbol="DOGEUSDT", amount_usdt=5, leverage=50)
    # TPSL_SHORT(symbol="DOGEUSDT")