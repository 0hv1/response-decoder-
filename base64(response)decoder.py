import base64
encryptStr = input("Enter encrypted String: ").split("/")
for i in encryptStr: 
    print(format(base64.b64decode(i.format(b""))))


# b'=' * (-len(encryptStr) % 4