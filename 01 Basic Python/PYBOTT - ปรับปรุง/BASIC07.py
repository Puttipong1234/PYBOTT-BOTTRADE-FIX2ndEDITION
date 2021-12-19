# package

from get_crypto_price import get_crypto_price
from BASIC06 import คำนวณจำนวนบิทคอยที่ต้องซื้อ

price = get_crypto_price(source = "bitstamp", crypto="btc", pair = "usdt")
จำนวน = คำนวณจำนวนบิทคอยที่ต้องซื้อ(ราคาบิทคอย=float(price),ชื่อexchange="bitstamp")
print(จำนวน)