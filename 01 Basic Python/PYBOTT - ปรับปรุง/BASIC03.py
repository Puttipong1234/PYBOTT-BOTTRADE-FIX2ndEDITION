# Dictionary 

# พจนานุกรม
# หมา - dog
# แมว - cat
# เป็ด - duck

# คำแปลไทยอังกฤษ = {
#     "หมา" : "dog" ,
#     "แมว" : "cat" ,
#     "เป็ด" : "duck"
# }

# print(คำแปลไทยอังกฤษ["หมา"])
# print(คำแปลไทยอังกฤษ["แมว"])

DataExample = {
   "code":200, 
   "msg":"", 
   "snapshotVos":[
      {
         "data":{
            "balances":[
               {
                  "asset":"BTC",
                  "free":"0.09905021",
                  "locked":"0.00000000"
               },
               {
                  "asset":"USDT",
                  "free":"1.89109409",
                  "locked":"0.00000000"
               }
            ],
            "totalAssetOfBtc":"0.09942700"
         },
         "type":"spot",
         "updateTime":1576281599000
      }
   ]
}

# test access data
# print(DataExample["code"])

# get balance of account
# print(DataExample["snapshotVos"][0]["data"]["balances"])
AllAsset = DataExample["snapshotVos"][0]["data"]["balances"]

for asset in AllAsset:
    # symbol - asset
    print(asset["asset"])
    # value
    print(asset["free"])

print("YOUR TOTAL ASSET IN BTC")
print(DataExample["snapshotVos"][0]["data"]["totalAssetOfBtc"])

HasBitcoinInAccount = True # False