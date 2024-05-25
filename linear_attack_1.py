from SM4 import SM4
from SM4 import T as pure_T
from Bytes import Bytes
from os import urandom
from decimal import Decimal

def T(block: Bytes) -> Bytes:
    return Bytes(pure_T(block.to_bytes()))

output = open("linear_attack_1.txt", "w")
key = urandom(16)
output.write("key=0x"+key.hex()+"\n\n")
encryptor = SM4(22, key)
print(encryptor.key_schedule, file=output)
output.write("\n")
pt = [urandom(16) for _ in range(100000)]
ct = [encryptor.encrypt(x) for x in pt]
print(ct[0], file=output)
output.write("\n")
G = Bytes(b'\x00\x64\x6f\xfe')
stats = []
rk = [Bytes(x) for x in encryptor.key_schedule]
for i in range(100000):
    X_0 = Bytes(ct[i][0])
    X_1 = Bytes(ct[i][1])
    X_2 = Bytes(ct[i][2])
    X_3 = Bytes(ct[i][3])
    C_0 = Bytes(ct[i][22])
    C_1 = Bytes(ct[i][23])
    C_2 = Bytes(ct[i][24])
    C_3 = Bytes(ct[i][25])
    left_side = G&X_0^G&C_1^G&T(X_1^X_2^X_3^rk[0])^G&T(C_0^C_2^C_3^rk[19]^T(C_0^C_1^C_2^rk[21])^T(C_0^C_1^C_3^rk[20]^T(C_0^C_1^C_2^rk[21])))
    right_side = G&rk[4]^G&rk[5]^G&rk[9]^G&rk[14]^G&rk[15]
    equation = left_side ^ right_side
    stats.append(bin(int.from_bytes(equation.b))[2:].count('0'))
for i in range(10):
        print(Decimal(sum(stats[10000*i : 10000*(i+1)])) / Decimal(320000), file=output)