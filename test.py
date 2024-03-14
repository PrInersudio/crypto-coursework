from SM4 import SM4

pt = bytes.fromhex("0123456789abcdeffedcba9876543210")
key = pt
print([x.hex() for x in SM4(32, key).encrypt(pt)])