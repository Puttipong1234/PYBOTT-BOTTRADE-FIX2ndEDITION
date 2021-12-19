# try except

result = ""

try:
    a = "TEST"
    b = 10
    result = a + b
except Exception as e:
    print("มีบางอย่างผิดพลาด โปรแกรมหยุดทำงาน")
    print(e)