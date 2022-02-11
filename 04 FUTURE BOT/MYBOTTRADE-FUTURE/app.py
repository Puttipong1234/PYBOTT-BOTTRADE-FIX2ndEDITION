from flask import Flask , request

app = Flask(__name__)

@app.route("/") # add path url
def hello_world():
    return "Hello, World!"

@app.route("/webhook")
def webhook():
    return "This is url for webhook!"

@app.route("/signals",methods=['POST'])
def signals():
    print("Someone Post Signals to me !")
    signal = request.data.decode("utf-8")
    import json
    signal = json.loads(signal) # เปลี่ยนจาก json ให้เป็น dictionary

    trade_side = signal["ACTION"]
    amount_coin = float(signal["AMOUNT_COIN"])
    leverage = int(signal["LEV"])
    symbol = signal["SYMBOL"]
    password = signal["PASSWORD"]
    
    if password != "xxxxxx":
        print("WRONG PASSWORD")
        return "403"

    print("ได้รับสัญญาณการซื้อขาย ดังนี้.....")
    print(trade_side)
    print(amount_coin)
    print(leverage)
    print(symbol)
    print("บอทเริ่มทำคำสั่งซื้อขายอัตโนมัติ ไปที่ ไบแนน.....")

    message = f"🤖🤖🤖🤖🤖🤖🤖\n🤖ได้รับสัญญาณการซื้อขาย ดังนี้..... \n🤖รูปแบบการเทรด {trade_side} {symbol}\n🤖จำนวนที่เปิด {amount_coin} \n🤖LEVERAGE {leverage}\n🤖🤖🤖🤖🤖🤖🤖"
    # Line notify Process
    from line_notify import LineNotify
    Access_Token = "xxxxx" # generate line notify
    notify = LineNotify(Access_Token)
    notify.send(message) # ส่งไปที่ห้องแชท

    # รับสัญญาณ SPOT 
    from trade import buy , sell
    if trade_side == "OPEN LONG" and leverage == 0: # if leverage = 0 => trade spot
        buy(symbol=symbol,amount_coin=amount_coin) # ซื้อแบบ market
    
    elif trade_side == "TPSL LONG" and leverage == 0: # if leverage = 0 => trade spot
        sell(symbol=symbol,amount_coin=amount_coin) # ขายแบบ takeprofit stoploss
    
    # รับสัญญาณ FUTURE
    from trade import OPEN_LONG , OPEN_SHORT , TPSL_LONG , TPSL_SHORT
    # INPUT ของเรา จะเทรดที่ไม้ละกี่ดอล
    AMOUT_USDT = 10 # USER SETTING FUTURE 
    
    # open long
    if trade_side == "OPEN LONG" and leverage > 0:
        OPEN_LONG(symbol=symbol, amount_usdt=AMOUT_USDT, leverage=leverage)
    
    # tpsl long
    elif trade_side == "TPSL LONG" and leverage > 0:
        TPSL_LONG(symbol=symbol)
    
    # open short
    elif trade_side == "OPEN SHORT" and leverage > 0:
        OPEN_SHORT(symbol=symbol, amount_usdt=AMOUT_USDT, leverage=leverage)
    
    # tpsl short
    elif trade_side == "TPSL SHORT" and leverage > 0:
        TPSL_SHORT(symbol=symbol)

    return "200"

if __name__=="__main__":
    app.run() # สั่งให้ app run !