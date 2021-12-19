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

    print("ได้รับสัญญาณการซื้อขาย ดังนี้.....")
    print(trade_side)
    print(amount_coin)
    print(leverage)
    print(symbol)
    print("บอทเริ่มทำคำสั่งซื้อขายอัตโนมัติ ไปที่ ไบแนน.....")

    message = f"🤖🤖🤖🤖🤖🤖🤖\n🤖ได้รับสัญญาณการซื้อขาย ดังนี้..... \n🤖รูปแบบการเทรด {trade_side} {symbol}\n🤖จำนวนที่เปิด {amount_coin} \n🤖LEVERAGE {leverage}\n🤖🤖🤖🤖🤖🤖🤖"
    # Line notify Process
    from line_notify import LineNotify
    Access_Token = "bYMefbv4lFK3Bn5esd45e8SqVmw78oHsqL9LrIVQ2DZ" # generate line notify
    notify = LineNotify(Access_Token)
    notify.send(message) # ส่งไปที่ห้องแชท


    return "200"

if __name__=="__main__":
    app.run() # สั่งให้ app run !