from config import BINANCE_API_KEY , BINANCE_API_SECRET

from binance.client import Client
from binance.helpers import round_step_size

client = Client(BINANCE_API_KEY, BINANCE_API_SECRET)

# myaccount_info = client.get_account()
# print(myaccount_info)

# balance = client.get_asset_balance(asset="USDT")
# print(balance["free"])

# if float(balance["free"]) < 15:
#     print("คุณมีจำนวนเงินไม่พอ")

# else:
#     print("จำนวนเงินมากพอสำหรับการซื้อขาย")

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


if __name__ == "__main__":
    amount = 0.0004
    sym = "BTCUSDT"
    # buy(symbol=sym,amount_coin=amount)
    # sell(symbol=sym,amount_coin=amount)