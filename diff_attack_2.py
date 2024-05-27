from SM4 import SM4, bytes_xor
from os import urandom
from decimal import Decimal

a1 = 0xf3f30033.to_bytes(4)
a2 = 0xf3000030.to_bytes(4)
a3 = 0x00f30003.to_bytes(4)
a4 = 0x00cf0033.to_bytes(4)
a5 = 0xf33c0000.to_bytes(4)
a6 = 0x3f0000cf.to_bytes(4)
a7 = 0xccf300fc.to_bytes(4)
encryptor = SM4(19, urandom(16))
DiffSet = [int(num).to_bytes(4) for num in open("DiffSetCPP.txt", "r").read().split("\n")]
Omega = [bytes_xor(x, a3) for x in DiffSet]
stats = []
pts = [urandom(16) for _ in range(10)]
cts = [b''.join(encryptor.encrypt(pt)[-4:]) for pt in pts]
for a0 in Omega:
    for pt,ct in zip(pts,cts):
        dif_pt = bytes_xor(pt, a0+a1+a1+a2)
        dif_ct = b''.join(encryptor.encrypt(dif_pt)[-4:])
        output_dif = bytes_xor(ct, dif_ct)
        comp = bytes_xor(output_dif, a6+a7+a1+a1)
        stats.append(bin(int.from_bytes(comp))[2:].count('0'))
for i in range(15):
    print(Decimal(sum(stats[i*10000:(i+1)*10000])) / Decimal(1280000))
print(Decimal(sum(stats[150000:])) / Decimal(len(stats[150000:])*128))
print(len(stats[150000:]))